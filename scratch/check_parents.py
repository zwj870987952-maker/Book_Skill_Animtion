# -*- coding: utf-8 -*-
import maya.cmds as cmds

print("RootExtraX_M t:", cmds.getAttr("RootExtraX_M.translate"))
print("RootExtraX_M r:", cmds.getAttr("RootExtraX_M.rotate"))
print("RootExtraX_M ws:", cmds.xform("RootExtraX_M", q=True, ws=True, t=True))

print("IKExtraLeg_L ws:", cmds.xform("IKExtraLeg_L", q=True, ws=True, t=True))
print("IKExtraLeg_R ws:", cmds.xform("IKExtraLeg_R", q=True, ws=True, t=True))
