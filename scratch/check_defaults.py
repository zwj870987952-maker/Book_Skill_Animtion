# -*- coding: utf-8 -*-
import maya.cmds as cmds

print("RootX_M parent:", cmds.listRelatives("RootX_M", parent=True))
print("Root_M parent:", cmds.listRelatives("Root_M", parent=True))
print("RootX_M children:", cmds.listRelatives("RootX_M", children=True))

# 检查默认属性值（default value）
for node in ["RootX_M", "Root_M", "IKLeg_L", "IKLeg_R"]:
    for attr in ["translateX", "translateY", "translateZ"]:
        full = f"{node}.{attr}"
        def_val = cmds.attributeQuery(attr, node=node, listDefault=True)
        cur_val = cmds.getAttr(full)
        print(f"{full}: cur={cur_val}, default={def_val}")
