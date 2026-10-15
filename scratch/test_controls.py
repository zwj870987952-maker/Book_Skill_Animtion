# -*- coding: utf-8 -*-
import maya.cmds as cmds

def test_controls():
    # 测试 roll 属性
    # 先读取默认
    default_roll = cmds.getAttr("IKLeg_L.roll")
    print("Default roll:", default_roll)
    
    # 测试 FKShoulder_L 旋转轴向对应手臂前后摆动的方向
    # Advanced Skeleton 中肩膀向前摆动通常是 rotateZ 还是 rotateX 还是 rotateY？
    # 查看 jointOrient 或 rotationOrder
    rot_order = cmds.getAttr("FKShoulder_L.rotateOrder")
    print("FKShoulder_L rotateOrder:", rot_order)
    
    # 查看 PoleLeg_L 坐标
    pv_l = cmds.xform("PoleLeg_L", q=True, ws=True, t=True)
    print("PoleLeg_L Pos:", pv_l)
    
    # 查看 RootX_M 的属性
    root_attrs = cmds.listAttr("RootX_M", keyable=True)
    print("RootX_M keyable attrs:", root_attrs)

test_controls()
