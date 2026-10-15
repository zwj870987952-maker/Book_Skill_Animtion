import os
import json
import yaml

base_dir = r"c:\Users\zwj87\Documents\Book_Skill\books\hayama-character-design"
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
        "prompt": f"在动画角色设计或原画动态绘制中，{cap['intents'][0]}，有哪些关键作画规范与解剖体块法则？",
        "expected_triggers": [cap_id],
        "forbidden_triggers": [],
        "context": {
            "keywords": keywords[:3]
        }
    })
    trigger_cases.append({
        "case_id": f"eval-{slug}-trigger-2",
        "description": f"Trigger eval for {title} via diagnostic query",
        "prompt": f"原画绘制或作画监督修形时遇到了相关问题：{cap['intents'][2]}，如何根据羽山淳一的工业标准进行纠偏排障？",
        "expected_triggers": [cap_id],
        "forbidden_triggers": [],
        "context": {
            "keywords": keywords[1:4] if len(keywords) > 3 else keywords
        }
    })

suite = {
    "version": "1.0.0",
    "suite_id": "hayama-character-design-eval-suite",
    "book_id": "hayama-anime-drawing-masterclass",
    "split_seed": 42,
    "train_ratio": 0.6,
    "trigger_cases": trigger_cases
}

with open(eval_suite_path, "w", encoding="utf-8") as f:
    json.dump(suite, f, indent=2, ensure_ascii=False)

print(f"Generated eval-suite.json for hayama-character-design with {len(trigger_cases)} trigger cases.")
