import json
import shutil
from pathlib import Path

ask_dir = Path(r"c:\Users\zwj87\Documents\Book_Skill\books\animators-survival-kit")
cap_dir = ask_dir / ".cangjie" / "capabilities"
book_dir = cap_dir / "book"
book_dir.mkdir(parents=True, exist_ok=True)

# 复制 overview.md 和 glossary.md
shutil.copy(ask_dir / "BOOK_OVERVIEW.md", book_dir / "overview.md")
shutil.copy(ask_dir / "candidates" / "glossary.md", book_dir / "glossary.md")

# 12 项能力映射
caps = [
    ("timing-spacing-charts", "时空双轴标尺与原画轨目表设计 (Timing, Spacing & Inbetweening Charts)", "精确区分耗时物理帧数与空间位移幅度，设计慢入慢出与偏心插值轨目表。"),
    ("keys-extremes-breakdowns", "关键帧、极值帧与过渡原画层级工程 (Keys, Extremes & Breakdowns)", "以关键帧立意、极值帧定界、过渡原画（Breakdown）决定弧线与优先倾向的分级工程。"),
    ("standard-walk-locomotion", "人类标准行走四大黄金关键帧与步频标尺 (Standard Human Walk)", "接触位、下沉缓冲位、越过位与抬起最高位，配合 24/16/12/8 帧节奏与骨盆代偿。"),
    ("runs-jumps-airborne", "奔跑、腾空滞空与跳跃受力全周期 (Runs, Jumps & Airborne Dynamics)", "以完全离地腾空悬浮期为核心，编排蹲伏蓄力、推离、腾空滞空与受压挤压全周期。"),
    ("weight-gravity-settle", "重量感传递、重力沉降与多级阻尼缓冲 (Weight, Inertia & Settle Mechanics)", "遵循重力落体与冲量动量守恒，在落地撞击中展现恒定容积挤压形变与多级沉降。"),
    ("anticipation-overshoot-recoil", "动作预感反冲与超量阻尼振荡 (Anticipation, Overshoot & Recoil)", "爆发前向反方向蓄力预感，刹车急停时利用惯性冲过目标位并进行弹簧衰减缓冲。"),
    ("arcs-waves-whips", "弧线运动轨迹与多级柔性鞭打动力学 (Arcs of Action, Waves & The Whip)", "消除生硬折线，沿圆滑弧线滑行，运用正弦波反转实现多级能量传递与鞭梢爆裂。"),
    ("overlapping-action-drag", "动作重叠、多级滞后拖尾与松弛组织运动 (Overlapping Action & Drag)", "主动力源先行，柔性附属物与松弛肌肉参差延迟滞后，杜绝全身体块同帧起止。"),
    ("dialogue-phonemes-accents", "对白口型视素同步、2-4帧超前量与身体重音 (Dialogue, Phonemes & Bodily Accents)", "口型视素比声学音频提前 2-4 帧开启，身体动作重音与台词发音爆破点同频共振。"),
    ("character-walks-personality", "潜行、跛足与个性化行走步态演化 (Sneaks, Struts, Limps & Personality Walks)", "调整四大黄金帧相对高低与受力时间，演化出蹑手蹑脚潜行、醉汉摇晃与跛脚等个性。"),
    ("fast-runs-smears-multiples", "高速奔跑残影、多重肢体与飞轮腿涂抹 (Smears, Multiples & Whirlwind Runs)", "单帧拉伸干刷涂抹、多重手臂腿部残影与圆环飞轮腿化解极端高速频闪与跳帧。"),
    ("flipping-inbetween-diagnostics", "五指翻页法、中间画排障与动画工程自检 (Flipping & Inbetween Diagnostics)", "掌握五指翻页法对比帧间流动性，排查穿模、抖动、体积失真与弧线断裂缺陷。")
]

destinations = {
    "book_slug": "animators-survival-kit",
    "book_title": "The Animator's Survival Kit",
    "author": "Richard Williams",
    "target_pack_slug": "animators-survival-kit",
    "capabilities": []
}

for slug, title, desc in caps:
    destinations["capabilities"].append({
        "capability_id": f"cap.animators-survival-kit.{slug}",
        "display_name": title,
        "target_skill_slug": "animators-survival-kit",
        "action": "create",
        "description": desc
    })

(cap_dir / "destinations.json").write_text(json.dumps(destinations, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Created destinations.json with {len(caps)} capabilities and initialized book overview/glossary!")
