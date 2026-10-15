# -*- coding: utf-8 -*-
import maya.cmds as cmds

# 测试左肩各轴向旋转对手部位置的影响
cmds.currentTime(1)
pos_0 = cmds.xform("FKWrist_L", q=True, ws=True, t=True)

# 绕 X
cmds.setAttr("FKShoulder_L.rotate", 20, 0, 0)
pos_x = cmds.xform("FKWrist_L", q=True, ws=True, t=True)

# 绕 Y
cmds.setAttr("FKShoulder_L.rotate", 0, 20, 0)
pos_y = cmds.xform("FKWrist_L", q=True, ws=True, t=True)

# 绕 Z
cmds.setAttr("FKShoulder_L.rotate", 0, 0, 20)
pos_z = cmds.xform("FKWrist_L", q=True, ws=True, t=True)

cmds.setAttr("FKShoulder_L.rotate", 0, 0, 0)

print("Base Wrist:", [round(v, 2) for v in pos_0])
print("+20 on X (diff):", [round(pos_x[i]-pos_0[i], 2) for i in range(3)])
print("+20 on Y (diff):", [round(pos_y[i]-pos_0[i], 2) for i in range(3)])
print("+20 on Z (diff):", [round(pos_z[i]-pos_0[i], 2) for i in range(3)])
