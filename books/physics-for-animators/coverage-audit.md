# 原书核心任务与覆盖度审计 (Coverage Audit) — 《动画师物理学》

## 核心任务覆盖审计表

| 任务编号 | 原书核心设计/工程任务 | 映射能力卡 (Capability ID) | 覆盖状态 |
|---|---|---|---|
| T-01 | 恒定推力作用下的物体启动加速排布 | `odd-rule-acceleration` | 100% 覆盖 |
| T-02 | 高空坠落、悬崖跌落与半时位置判定 | `gravity-projectile-timing` | 100% 覆盖 |
| T-03 | 投掷、开炮等抛物线运动的正交轨迹排布 | `gravity-projectile-timing` | 100% 覆盖 |
| T-04 | 人物单脚站立、弯腰、举重时的平衡与防倾覆 | `center-of-gravity-balance` | 100% 覆盖 |
| T-05 | 物体在不同地面材质上的滑动摩擦制动 | `friction-drag-resistance` | 100% 覆盖 |
| T-06 | 跳伞与高空自由落体的终端下落速度封顶 | `friction-drag-resistance` | 100% 覆盖 |
| T-07 | 人体各关节生物杠杆效能与发力爆发 | `torque-lever-joints` | 100% 覆盖 |
| T-08 | 花样滑冰、空中翻滚时的收腿自转加速 | `torque-lever-joints` | 100% 覆盖 |
| T-09 | 格斗打斗中的重击受力时间、击退与后坐力 | `action-reaction-impact` | 100% 覆盖 |
| T-10 | 人物立定跳远、垂直起跳的推地与着地缓冲 | `character-jump-mechanics` | 100% 覆盖 |
| T-11 | 行走循环中动能与势能转换及肩髋扭转 | `character-walk-energy` | 100% 覆盖 |
| T-12 | 头发、尾巴、披风按长度与表面积延迟摆动 | `drag-follow-through-physics` | 100% 覆盖 |
| T-13 | 液体倒出（水 vs 油 vs 蜂蜜）的形态与海浪碎浪 | `liquid-fluid-dynamics` | 100% 覆盖 |
| T-14 | 火球蘑菇云热浮力涡流与物体受击脆性碎裂 | `fire-explosion-fracture` | 100% 覆盖 |
| T-15 | 3D 灯光平方反比衰减与半影柔和度调整 | `light-shadow-optics` | 100% 覆盖 |

**审计结论**: 15 项核心任务全部被 12 项高内聚能力卡完整覆盖，无任何关键物理机制遗漏或断层。
