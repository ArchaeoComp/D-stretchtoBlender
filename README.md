# Texture Switcher

**Texture Switcher** is a Blender addon designed to streamline texture management using 3D format .obj with `.mtl` file modifications. It provides an intuitive way to load and switch textures generated with D-Stretch addon for ImageJ. Whole script works on the blender import operator of .obj files, tat loads both 3D model and defined textures.  

---

## Features

### Texture Management
- **Switch Textures**: Quickly cycle through available textures in the active material using a simple UI button.
- **Material Compatibility**: Ensures compatibility with node-based materials in Blender.

### `.mtl` File Editing
- **Automated Editing**: Modifies `.mtl` files to include texture maps for diffuse, specular, roughness, normal, and alpha channels.
- **Conditional Logic**: Automatically selects between alternate file names based on existing textures in the folder.

### User Interface
- Integrated into Blender's 3D Viewport (`N` panel) under the **Tool** tab.
- Simple controls for texture switching and `.mtl` file folder selection.

---

## Installation

1. Download the `texture_switcher.py` file.
2. Open Blender and go to `Edit > Preferences > Add-ons > Install`.
3. Select the `texture_switcher.py` file and click **Install Add-on**.
4. Enable the addon in the Add-ons menu.

---

## Usage

### `.mtl` File Editing and `.obj` File Importing
1. Before importing .obj files into blender, please put your images from D-stretch into same folder as your .obj files and diffuse texture. 
2. Click **Select Folder** to select a folder containing `.mtl` files and your 3D model.
3. Ensure `.mtl` files and related textures are in the selected folder.
4. Click **Change .mtl** to apply modifications.
5. Import your .obj files into blender by standard operator, or drag and drop

### Texture Switching
1. Select a mesh object with a material.
2. Open the **Tool** tab in the `N` panel.
3. Click **Switch Texture** to cycle through textures in the active material.

---

## Requirements

- **Blender Version**: 3.0 or higher.
- **File Format**: `.obj` files; `.mtl` files and associated texture images.

---

## Limitations

- Works only with `.obj` files and `.mtl` files.
- Assumes texture files follow a specific naming convention (`.jpg`, `_lre.jpg`, `_yre.jpg`, etc.).
- Only supports `.jpg` files with specific color spaces from D-stretch. List of supported color spaces: lre, yre, crgb, ybk **Note** Could be changed in code itself (lines 70-81 of code), with limitation to four colourspaces. 

---

## License

Released under the CC BY 3.0 License, encouraging modifications and adaptations for academic and research purposes.

---

## Developer Notes

### Key Components:
- **Texture Switching**: Utilizes Python's global variables and Blender's active material API.
- **`.mtl` Modification**: Edits `.mtl` files with conditional checks for texture file existence.
- **UI Integration**: Custom operators and panels for easy accessibility.

For more details, feel free to contribute or raise issues on the GitHub repository.
