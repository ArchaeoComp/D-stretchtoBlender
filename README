# Texture Switcher

**Texture Switcher** is a Blender addon designed to streamline texture management and `.mtl` file modifications. It provides an intuitive way to switch between textures in a material and edit `.mtl` files directly from Blender.

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

### Texture Switching
1. Select a mesh object with a material.
2. Open the **Tool** tab in the `N` panel.
3. Click **Switch Texture** to cycle through textures in the active material.

### `.mtl` File Editing
1. Click **Vybrat složku** to select a folder containing `.mtl` files.
2. Ensure `.mtl` files and related textures are in the selected folder.
3. Click **Change .mtl** to apply modifications.

---

## Requirements

- **Blender Version**: 3.0 or higher.
- **File Format**: `.mtl` files and associated texture images.

---

## Limitations

- Works only with mesh objects and materials using node-based setups.
- Assumes texture files follow a specific naming convention (`.jpg`, `_lre.jpg`, `_yre.jpg`, etc.).

---

## License

Released under the **MIT License**, allowing free use, modification, and distribution.

---

## Developer Notes

### Key Components:
- **Texture Switching**: Utilizes Python's global variables and Blender's active material API.
- **`.mtl` Modification**: Edits `.mtl` files with conditional checks for texture file existence.
- **UI Integration**: Custom operators and panels for easy accessibility.

For more details, feel free to contribute or raise issues on the GitHub repository.
