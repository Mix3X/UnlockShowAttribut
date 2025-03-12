# Maya Script: Unlock and Show Attributes for Controllers

This Python script for Autodesk Maya unlocks and makes keyable the transform attributes (translate, rotate, and scale) of all NURBS curve controllers whose parent names end with `_ctrl` or `_Ctrl`. It is useful for riggers and animators who need to quickly expose locked attributes for animation purposes.

## Features

- **Automatic Controller Detection:** Identifies controllers based on NURBS curves whose parent names end with `_ctrl` or `_Ctrl`.
- **Attribute Unlocking:** Unlocks and sets keyable the following attributes for each detected controller:
  - Translate: `translateX`, `translateY`, `translateZ`
  - Rotate: `rotateX`, `rotateY`, `rotateZ`
  - Scale: `scaleX`, `scaleY`, `scaleZ`
- **Batch Processing:** Processes all relevant controllers in the scene at once.
- **Console Feedback:** Displays the number of controllers modified.

## Requirements

- Autodesk Maya 2022 or newer

## Usage

1. Open your Maya scene.
2. Run the script in the Maya Script Editor.
3. The transform attributes of all controllers (ending in `_ctrl` or `_Ctrl`) will be unlocked and keyable.

## Example

If you have controllers named:

- `arm_ctrl`
- `leg_Ctrl`
- `spine_ctrl`

The script will unlock and show the translate, rotate, and scale attributes for each of these controllers.

## Code

```python
import maya.cmds as cmds

def unlock_and_show_attrs():
    # Get all nurbsCurve objects in the scene
    all_curves = cmds.ls(type="nurbsCurve", long=True)
    
    controllers = []
    
    # Filter curves with parent names ending in _ctrl or _Ctrl
    for curve in all_curves:
        parent = cmds.listRelatives(curve, parent=True, fullPath=True)
        if parent:
            parent_name = parent[0].split('|')[-1]
            if parent_name.endswith("_ctrl") or parent_name.endswith("_Ctrl"):
                controllers.append(parent[0])

    # Unlock and show attributes for each controller
    attrs = ["translateX", "translateY", "translateZ",
             "rotateX", "rotateY", "rotateZ",
             "scaleX", "scaleY", "scaleZ"]

    for ctrl in controllers:
        for attr in attrs:
            full_attr = f"{ctrl}.{attr}"
            cmds.setAttr(full_attr, lock=False, channelBox=True)
            cmds.setAttr(full_attr, keyable=True)

    print(f"{len(controllers)} controllers have been modified.")

# Run the function
unlock_and_show_attrs()
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

