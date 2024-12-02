bl_info = {
    "name": "Texture Switcher",
    "blender": (3, 0, 0),
    "category": "Object",
}

import bpy
import os

current_texture_index = 0
folder_path = ""

def switch_texture(self, context):
    global current_texture_index
    
    obj = context.active_object
    if not obj or obj.type != 'MESH':
        self.report({'WARNING'}, "Please select an object of type Mesh.")
        return
    
    mat = obj.active_material
    if not mat or not mat.use_nodes:
        self.report({'WARNING'}, "The active material does not have nodes enabled.")
        return
    
    nodes = mat.node_tree.nodes
    image_textures = [node for node in nodes if node.type == 'TEX_IMAGE']
    
    if not image_textures:
        self.report({'WARNING'}, "The material does not contain any Image Texture nodes.")
        return
    
    current_texture_index = (current_texture_index + 1) % len(image_textures)
    image_texture_node = image_textures[current_texture_index]
    bpy.context.scene.tool_settings.image_paint.canvas = image_texture_node.image

    for node in image_textures:
        node.select = False
    image_texture_node.select = True
    mat.node_tree.nodes.active = image_texture_node

    self.report({'INFO'}, f"Switched to texture: {image_texture_node.image.name}")

def modify_mtl_files():
    global folder_path
    
    if not folder_path:
        print("No path was specified.")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith('.mtl'):
            mtl_path = os.path.join(folder_path, filename)
            print(f"Processing: {filename}")

            with open(mtl_path, 'r') as file:
                lines = file.readlines()

            new_lines = []
            second_material_found = False
            first_material_skipped = False

            for line in lines:
                new_lines.append(line)

                if line.startswith('newmtl'):
                    if first_material_skipped:
                        if second_material_found:
                            break
                        second_material_found = True
                        material_name = line.split()[1].strip()
                        diffuse_texture = f"{material_name}.jpg"
                        specular_texture = f"{material_name}_lre.jpg"
                        roughness_texture = f"{material_name}_yre.jpg"
                        normal_texture = f"{material_name}_crgb.jpg"
                        alpha_texture = f"{material_name}_ybk.jpg"
                        
                        specular_texture2 = f"{material_name}+lre.jpg"
                        roughness_texture2 = f"{material_name}+yre.jpg"
                        normal_texture2 = f"{material_name}+crgb.jpg"
                        alpha_texture2 = f"{material_name}+ybk.jpg"

                        new_lines.append(f'map_Ks {specular_texture if os.path.exists(os.path.join(folder_path, specular_texture)) else specular_texture2}\n')
                        new_lines.append(f'map_Ke {roughness_texture if os.path.exists(os.path.join(folder_path, roughness_texture)) else roughness_texture2}\n')
                        new_lines.append(f'map_Bump {normal_texture if os.path.exists(os.path.join(folder_path, normal_texture)) else normal_texture2}\n')
                        new_lines.append(f'map_d {alpha_texture if os.path.exists(os.path.join(folder_path, alpha_texture)) else alpha_texture2}\n')
                    else:
                        first_material_skipped = True if "Solid" in line else first_material_skipped

            if second_material_found:
                with open(mtl_path, 'w') as file:
                    file.writelines(new_lines)
                print(f"Successfully modified: {filename}")
            else:
                print(f"No modifications found for: {filename}")

class TEXTURE_OT_select_folder(bpy.types.Operator):
    bl_idname = "texture.select_folder"
    bl_label = "Select Folder"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype="DIR_PATH")

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        global folder_path
        
        folder_path = bpy.path.abspath(self.filepath)
        context.scene.folder_path = folder_path
        print(f"Selected folder: {folder_path}")
        return {'FINISHED'}

class TEXTURE_PT_switcher(bpy.types.Panel):
    bl_label = "Texture Switcher"
    bl_idname = "TEXTURE_PT_switcher"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator("texture.switch", text="Switch Texture")
        layout.prop(context.scene, "folder_path", text="Path to .mtl")
        layout.operator("texture.change_mtl", text="Change .mtl")
        layout.operator("texture.select_folder", text="Select Folder")

class TEXTURE_OT_switch(bpy.types.Operator):
    bl_idname = "texture.switch"
    bl_label = "Switch Texture"

    def execute(self, context):
        switch_texture(self, context)
        return {'FINISHED'}

class TEXTURE_OT_change_mtl(bpy.types.Operator):
    bl_idname = "texture.change_mtl"
    bl_label = "Change .mtl"

    def execute(self, context):
        global folder_path
        folder_path = context.scene.folder_path
        modify_mtl_files()
        return {'FINISHED'}

def register():
    bpy.types.Scene.folder_path = bpy.props.StringProperty(
        name="Folder Path",
        description="Path to .mtl files",
        default=""
    )
    
    bpy.utils.register_class(TEXTURE_PT_switcher)
    bpy.utils.register_class(TEXTURE_OT_switch)
    bpy.utils.register_class(TEXTURE_OT_change_mtl)
    bpy.utils.register_class(TEXTURE_OT_select_folder)

def unregister():
    bpy.utils.unregister_class(TEXTURE_PT_switcher)
    bpy.utils.unregister_class(TEXTURE_OT_switch)
    bpy.utils.unregister_class(TEXTURE_OT_change_mtl)
    bpy.utils.unregister_class(TEXTURE_OT_select_folder)
    del bpy.types.Scene.folder_path

if __name__ == "__main__":
    register()
