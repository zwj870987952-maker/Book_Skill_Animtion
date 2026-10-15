import os
import json
import yaml

base_dir = r"c:\Users\zwj87\Documents\Book_Skill\books\storyboard-art"
verified_yaml_path = os.path.join(base_dir, ".cangjie", "capabilities", "verified.yaml")
evals_dir = os.path.join(base_dir, ".cangjie", "evals")
eval_suite_path = os.path.join(evals_dir, "eval-suite.json")

with open(verified_yaml_path, "r", encoding="utf-8") as f:
    bundle = yaml.safe_load(f)

trigger_cases = []

for cap in bundle["capabilities"]:
    cap_id = cap["capability_id"]
    slug = cap["slug"]
    title = cap["title"]
    keywords = cap["keywords"]

    trigger_cases.append({
        "case_id": f"eval-{slug}-trigger-1",
        "description": f"Trigger eval for {title} via primary intent",
        "prompt": f"在影视或动画分镜设计中，{cap['intents'][0]}，有哪些关键工业标准与技术规范？",
        "expected_triggers": [cap_id],
        "forbidden_triggers": [],
        "context": {
            "keywords": keywords[:3]
        }
    })
    trigger_cases.append({
        "case_id": f"eval-{slug}-trigger-2",
        "description": f"Trigger eval for {title} via diagnostic query",
        "prompt": f"故事板绘制与镜头衔接时遇到了相关问题：{cap['intents'][2]}，如何根据好莱坞标准进行纠偏排障？",
        "expected_triggers": [cap_id],
        "forbidden_triggers": [],
        "context": {
            "keywords": keywords[1:4] if len(keywords) > 3 else keywords
        }
    })

suite = {
    "version": "1.0.0",
    "suite_id": "storyboard-art-eval-suite",
    "book_id": "the-art-of-the-storyboard",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": trigger_cases
}

with open(eval_suite_path, "w", encoding="utf-8") as f:
    json.dump(suite, f, indent=2, ensure_ascii=False)

print(f"Generated eval-suite.json for storyboard-art with {len(trigger_cases)} trigger cases.")
