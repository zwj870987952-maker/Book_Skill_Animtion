import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch/clean_inventory.txt", encoding='utf-8') as f:
    lines = [l.strip() for l in f if l.strip()]

completed_keywords = [
    "Animators Survival Kit", "动画师生存手册",
    "Cartoon Animation", "ADVANCED_ANIMATION",
    "Drawn to Life", "迪士尼动画黄金圣典", "Drawn to life 2",
    "Force Animal Drawing",
    "Force Character Design",
    "Force_ Dynamic Life Drawing",
    "Physics for animators",
    "Stop.Staring",
    "The illusion of life", "生命的幻象",
    "anatomy for sculptors",
    "Framed ink",
    "电影语言的语法",
    "面部表情艺用解剖",
    "开拍之前：故事板的艺术",
    "超人气动画角色设计攻略羽山淳一",
    "动画的时间掌握",
    "运动规律PPT版",
    "图说动画规律",
    "角色的运动和动作",
    "psoe设计基础篇",
    "Pose to Pose 之后的生活",
    "storyboarding分镜头脚本设计",
    "准备分镜图",
    "分镜头脚本设计教程",
    "电影镜头入门",
    "镜头的语法",
    "剪辑的语法",
    "大师镜头",
    "镜头在说话",
    "Pro Shot Builder"
]

remaining = []
for l in lines:
    parts = l.split(" | ", 1)
    if len(parts) == 2:
        size, path = parts
        matched = False
        for kw in completed_keywords:
            if kw in path:
                matched = True
                break
        if not matched:
            remaining.append((size, path))

for s, p in remaining:
    print(f"{s} | {p}")
