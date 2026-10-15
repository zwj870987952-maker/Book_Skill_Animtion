import json
import os

eval_set = {
    "suite_id": "suite.story-and-screenplay-engineering",
    "book_id": "story-and-screenplay-engineering",
    "trigger_cases": [
        {
            "case_id": "eval-01",
            "query": "如何在三幕八序列架构中规划激励事件、情节点I、中点危机与第二情节点的标准时序？",
            "expected_capability": "cap.story-and-screenplay-engineering.story-structure-and-three-act-architecture",
            "type": "positive"
        },
        {
            "case_id": "eval-02",
            "query": "故事第二幕进行到第60页时，如何通过中点危机（Midpoint）实现攻守立场的彻底翻转并启动倒计时时钟？",
            "expected_capability": "cap.story-and-screenplay-engineering.story-structure-and-three-act-architecture",
            "type": "positive"
        },
        {
            "case_id": "eval-03",
            "query": "如何确立剧本的主导论题（Controlling Idea）？如何构建正论与反论辩证交锋的价值对抗矩阵？",
            "expected_capability": "cap.story-and-screenplay-engineering.controlling-idea-and-thematic-truth",
            "type": "positive"
        },
        {
            "case_id": "eval-04",
            "query": "如何避免剧本沦为说教布道？为什么说主导论题的终极真理必须由高潮中主角的物理决绝行动来验证？",
            "expected_capability": "cap.story-and-screenplay-engineering.controlling-idea-and-thematic-truth",
            "type": "positive"
        },
        {
            "case_id": "eval-05",
            "query": "如何设计主角显性欲望（Want）与隐性精神需求（Need）的根本性错位？心理幽灵创伤如何孕育致命缺陷？",
            "expected_capability": "cap.story-and-screenplay-engineering.character-arc-and-inner-flaw",
            "type": "positive"
        },
        {
            "case_id": "eval-06",
            "query": "在全片最低谷的灵魂暗夜（All Hope Is Lost）中，主角如何迎来顿悟（Epiphany）完成人物弧光蜕变？",
            "expected_capability": "cap.story-and-screenplay-engineering.character-arc-and-inner-flaw",
            "type": "positive"
        },
        {
            "case_id": "eval-07",
            "query": "微观场景设计中如何实现开场至结尾的价值正负极性翻转（+/-）？现实残酷反弹产生的断层（Gap）如何运作？",
            "expected_capability": "cap.story-and-screenplay-engineering.scene-design-and-conflict-beats",
            "type": "positive"
        },
        {
            "case_id": "eval-08",
            "query": "场景微观力学中为什么必须遵循晚进早出（Late In, Early Out）？如何切除毫无实质冲突的寒暄废戏？",
            "expected_capability": "cap.story-and-screenplay-engineering.scene-design-and-conflict-beats",
            "type": "positive"
        },
        {
            "case_id": "eval-09",
            "query": "台词对白如何运用海明威冰山理论实现言外之意与潜台词？如何将世界观背景信息转化为交锋中的弹药投放？",
            "expected_capability": "cap.story-and-screenplay-engineering.dialogue-subtext-and-exposition-delivery",
            "type": "positive"
        },
        {
            "case_id": "eval-10",
            "query": "如何避免“正如你所知（As you know, Bob）”式直白向观众交代世界观？如何通过遮名测试杜绝千人一面？",
            "expected_capability": "cap.story-and-screenplay-engineering.dialogue-subtext-and-exposition-delivery",
            "type": "positive"
        },
        {
            "case_id": "eval-11",
            "query": "如何塑造动机自洽、智商战力始终压制主角30%的反派角色？四级矛盾对抗方阵（矛盾-对立-否定之否定）如何升级？",
            "expected_capability": "cap.story-and-screenplay-engineering.antagonist-and-forces-of-antagonism",
            "type": "positive"
        },
        {
            "case_id": "eval-12",
            "query": "为什么反派在其自身世界观中必须是正义主角？如何杜绝脸谱化降智恶棍？",
            "expected_capability": "cap.story-and-screenplay-engineering.antagonist-and-forces-of-antagonism",
            "type": "positive"
        },
        {
            "case_id": "eval-13",
            "query": "动画剧本特化语法中如何体现纯视觉优先（Show Don't Tell）？四步视觉笑料（Visual Gag）结构力学如何展开？",
            "expected_capability": "cap.story-and-screenplay-engineering.animation-screenplay-and-visual-gag",
            "type": "positive"
        },
        {
            "case_id": "eval-14",
            "query": "动画角色拟人化（Anthropomorphism）中如何平衡其自然生物物理特性与人类心智情感？",
            "expected_capability": "cap.story-and-screenplay-engineering.animation-screenplay-and-visual-gag",
            "type": "positive"
        },
        {
            "case_id": "eval-15",
            "query": "故事危机（Crisis）如何设计为两害相权取其轻或不可兼得两种善的道德绝境？终极高潮如何带来不可逆重构？",
            "expected_capability": "cap.story-and-screenplay-engineering.pacing-crisis-climax-and-resolution",
            "type": "positive"
        },
        {
            "case_id": "eval-16",
            "query": "为什么说高潮执行必须坚决杜绝零代价廉价大团圆？结局收束如何达成深刻的情感宣泄（Catharsis）？",
            "expected_capability": "cap.story-and-screenplay-engineering.pacing-crisis-climax-and-resolution",
            "type": "positive"
        },
        {
            "case_id": "eval-17",
            "query": "A线主情节与B线/C线副线如何实现有机呼吸交织？副线如何从多角度切面辩证回响主旨？",
            "expected_capability": "cap.story-and-screenplay-engineering.sub-plot-and-character-ensemble",
            "type": "positive"
        },
        {
            "case_id": "eval-18",
            "query": "群像角色网络中如何为导师、弄臣、怀疑者与镜子分配互斥性格极端并实现高潮物理合流？",
            "expected_capability": "cap.story-and-screenplay-engineering.sub-plot-and-character-ensemble",
            "type": "positive"
        },
        {
            "case_id": "eval-19",
            "query": "好莱坞标准剧本格式（Courier 12pt）中场景标题Slugline、角色名、台词与动作行有何排版规范？",
            "expected_capability": "cap.story-and-screenplay-engineering.screenplay-formatting-and-action-lines",
            "type": "positive"
        },
        {
            "case_id": "eval-20",
            "query": "动作行写作如何践行留白法则（Whitespace Rule）？为什么必须坚决消灭We See与不可拍摄内容（Unfilmables）？",
            "expected_capability": "cap.story-and-screenplay-engineering.screenplay-formatting-and-action-lines",
            "type": "positive"
        },
        {
            "case_id": "eval-21",
            "query": "动画剧集企划圣经（Show Bible）标准七大工业模块包含哪些？商业提案Logline黄金公式如何撰写？",
            "expected_capability": "cap.story-and-screenplay-engineering.animation-series-bible-and-pitching",
            "type": "positive"
        },
        {
            "case_id": "eval-22",
            "query": "如何为动画长篇或季播剧集设计源源不断的剧集产生引擎（Episode Generator Engine）与商业衍生品可行性？",
            "expected_capability": "cap.story-and-screenplay-engineering.animation-series-bible-and-pitching",
            "type": "positive"
        },
        {
            "case_id": "eval-23",
            "query": "剧本医生如何排查慢启动病、被动主角综合征、第二幕泥潭塌陷与机械降神等致命病灶？",
            "expected_capability": "cap.story-and-screenplay-engineering.screenplay-troubleshooting-and-rewrite-doctor",
            "type": "positive"
        },
        {
            "case_id": "eval-24",
            "query": "好莱坞四轮降维重写流水线（骨架重构→角色弧光→场景张力→台词抛光）的具体实操步骤是什么？",
            "expected_capability": "cap.story-and-screenplay-engineering.screenplay-troubleshooting-and-rewrite-doctor",
            "type": "positive"
        },
        {
            "case_id": "eval-25",
            "query": "如何在三维软件中对双足角色进行蒙皮权重平滑与关节骨骼绑定？",
            "expected_capability": "out_of_scope",
            "type": "negative"
        },
        {
            "case_id": "eval-26",
            "query": "动画逐帧绘制中下落小球的弹跳接触与挤压拉伸帧数计算如何进行？",
            "expected_capability": "out_of_scope",
            "type": "negative"
        },
        {
            "case_id": "eval-27",
            "query": "分镜头脚本绘制中如何划定180度轴线并规划广角长焦镜头景别？",
            "expected_capability": "out_of_scope",
            "type": "negative"
        },
        {
            "case_id": "eval-28",
            "query": "如何在Maya中编写MEL脚本批量导出动画相机的FBX缓存？",
            "expected_capability": "out_of_scope",
            "type": "negative"
        },
        {
            "case_id": "eval-29",
            "query": "人体解剖学中三角肌与胸大肌在锁骨处的附着点三维形态如何塑造？",
            "expected_capability": "out_of_scope",
            "type": "negative"
        },
        {
            "case_id": "eval-30",
            "query": "在水体自然特效模拟中浅水碎浪与黏度阻力系数如何设置？",
            "expected_capability": "out_of_scope",
            "type": "negative"
        }
    ]
}

os.makedirs("books/story-and-screenplay-engineering/candidates", exist_ok=True)
out_path = "books/story-and-screenplay-engineering/candidates/eval-sets.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(eval_set, f, ensure_ascii=False, indent=2)

print(f"Generated {out_path} with {len(eval_set['trigger_cases'])} cases.")
