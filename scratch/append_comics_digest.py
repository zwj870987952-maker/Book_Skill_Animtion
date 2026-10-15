# -*- coding: utf-8 -*-
import os

appendix = """

---

# 第十五篇：漫画家数字工业管线与工程参数规范

## 15.1 工业出版级文件分辨率与色彩配置标准
在进入现代数字化绘制（Clip Studio Paint / Photoshop）时，物理出版与移动端呈现对技术参数有着严酷的硬门指标：
1. **黑白黑白二值漫画（Monochrome Manga）**：
   - **分辨率**：必须设定为 **600 DPI** 或 **1200 DPI**（1-bit 黑白二值，无灰色抗锯齿）；
   - **网点纸防摩尔纹（Moiré Prevention）铁律**：网点线数严格控制在 50L - 65L 之间。两个叠加的网点纸必须旋转不同角度（如相差 30°），或者网点尺寸相同且绝对对齐，严禁不同线数网点随意重叠引发视觉波纹干涉灾难。
2. **全彩漫画与欧美图像小说（Full Color Comics）**：
   - **分辨率**：标准设定为 **350 DPI**（CMYK 印刷色彩空间，如 Japan Color 2001 Coated 或 US Web Coated SWOP）。
3. **出血框（Bleed Box）与裁剪标记（Trim Marks）**：
   - **内框（Live Area / Safe Zone）**：所有对白气泡与核心人物必须保留在内框以内，距裁剪线至少 10mm；
   - **裁切线（Trim Line）**：最终成品物理裁切尺寸（如标准 B5 尺寸 182mm × 257mm）；
   - **出血线（Bleed Margin）**：向外多画出 3mm - 5mm，确保印刷裁切轻微移位时不露出白边。

---

## 15.2 Clip Studio Paint (CSP) 标准分层架构
一套标准的工业级漫画数字工程文件，图层结构必须严格分级：

```text
├── [Folder] 01_TEXT_&_BALLOONS (对白文字与矢量气泡层)
├── [Folder] 02_SFX_LETTERING (手绘拟音字与拟态词图层)
├── [Folder] 03_PANEL_FRAMES (分格矢量蒙版与边框线)
├── [Folder] 04_FOREGROUND_INKS (前景角色主轮廓线稿，G笔压感)
├── [Folder] 05_BACKGROUND_INKS (背景透视与机械建筑线稿)
├── [Folder] 06_SCREEN_TONES (网点纸图层：阴影、材质与渐变)
├── [Folder] 07_FLAT_COLORS / GRAYS (基础平涂灰度或固有色)
└── [Layer]  08_DRAFT_PENCIL (草图分镜台本层，天蓝色，设为草稿属性)
```

遵循这一严密的层级结构，分镜、线稿、贴网点与排印各工种才能在数字化管线中实现无缝协同与光速返修。
"""

with open("books/comics-grammar-and-sequential-art/DIGEST.md", "a", encoding="utf-8") as f:
    f.write(appendix.strip() + "\n")

print("Appended successfully!")
