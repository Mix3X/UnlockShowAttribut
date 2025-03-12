import maya.cmds as cmds

def unlock_and_show_attrs():
    # Récupérer tous les objets de type nurbsCurve dans la scène
    all_curves = cmds.ls(type="nurbsCurve", long=True)
    
    controllers = []
    
    # Filtrer les courbes ayant un parent dont le nom se termine par "_ctrl" ou "_Ctrl"
    for curve in all_curves:
        parent = cmds.listRelatives(curve, parent=True, fullPath=True)
        if parent:
            parent_name = parent[0].split('|')[-1]  # Récupérer juste le nom de l'objet
            if parent_name.endswith("_ctrl") or parent_name.endswith("_Ctrl"):
                controllers.append(parent[0])  # Stocker le chemin complet pour éviter les conflits

    # Déverrouiller et afficher les attributs pour chaque contrôleur
    attrs = ["translateX", "translateY", "translateZ",
             "rotateX", "rotateY", "rotateZ",
             "scaleX", "scaleY", "scaleZ"]

    for ctrl in controllers:
        for attr in attrs:
            full_attr = f"{ctrl}.{attr}"
            
            # Afficher l'attribut
            cmds.setAttr(full_attr, lock=False, channelBox=True)
            cmds.setAttr(full_attr, keyable=True)

    print(f"{len(controllers)} contrôleurs ont été modifiés.")

# Exécuter la fonction
unlock_and_show_attrs()
