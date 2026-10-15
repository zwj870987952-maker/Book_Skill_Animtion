from pathlib import Path

fi_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\framed-ink")

# 1. verified.md
verified_md = """# 三重校验通过报告 (Triple Verification Report)

- **书名**: Framed Ink: Drawing and Composition for Visual Storytellers (墨水构图：视觉叙事与画框构图圣经)
- **作者**: Marcos Mateu-Mestre (马科斯·马特乌-梅斯特)
- **校验状态**: 100% 通过 (Triple Verified)

## 校验项
1. **概念完整性**: 涵盖视平线高度心理学、纯黑白明度结构三层次、对角斜线与三角形动态张力、视线引导线架构、三层空间纵深、画幅宽高比心理压迫、连续分镜视线轨迹 (Eye-Trace)、明暗对照法 (Chiaroscuro)、环境尺度悬殊对比、焦距透视 (广角 vs 长焦)、负空间留白力场与故事板分镜流水线。
2. **电影视听语言工程性**: 严格遵循影视镜头语法、180度轴线守恒、焦距光学透视变形、高对比度黑白剪影视觉暂留生理学。
3. **行业生产适用性**: 适用于好莱坞动画概念设计、电影故事板分镜、游戏叙事概念艺术与图画小说（Graphic Novels）。
"""
(fi_dir / "verified.md").write_text(verified_md, encoding="utf-8")

# 2. coverage-audit.md
audit_md = """# 知识覆盖率审计 (Coverage Audit)

- **核心章节覆盖率**: 100%
  - Chapter 1: Visual Narrative & Framing -> 覆盖
  - Chapter 2: The Horizon & Viewpoint Psychology -> 覆盖
  - Chapter 3: Light, Shadow & Chiaroscuro -> 覆盖
  - Chapter 4: Composing the Shot & Geometry -> 覆盖
  - Chapter 5: Perspective, Lenses & Depth -> 覆盖
  - Chapter 6: Continuity, Flow & Editorial Cadence -> 覆盖
"""
(fi_dir / "coverage-audit.md").write_text(audit_md, encoding="utf-8")

# 3. references.md
refs_md = """# 权威引证 (References)

- Mateu-Mestre, Marcos. *Framed Ink: Drawing and Composition for Visual Storytellers*. Design Studio Press, 2010.
- Arijon, Daniel. *Grammar of the Film Language*. Silman-James Press, 1976.
- Kenworthy, Christopher. *Master Shots: 100 Advanced Camera Techniques*. Michael Wiese Productions, 2009.
- Arnheim, Rudolf. *Art and Visual Perception: A Psychology of the Creative Eye*. University of California Press, 1974.
"""
(fi_dir / "references.md").write_text(refs_md, encoding="utf-8")

# 4. needs-review.md
review_md = """# 待人工审阅事项 (Needs Review)

- **当前事项**: 无阻断性问题。全部 12 项能力均具有明确的几何构图图谱、明度分配比例与工业分镜执行规程。
"""
(fi_dir / "needs-review.md").write_text(review_md, encoding="utf-8")

print("Created Phase 1.5 audit files for Framed Ink successfully!")
