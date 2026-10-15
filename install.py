#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Book_Skill_Animtion 技能一键安装器
====================================================================
支持将本仓库中提炼好的 22 个动画与影视视听 Skills 一键安装到：
1. Google Antigravity 全局/配置目录 (~/.gemini/antigravity/skills/ 或 ~/.gemini/config/skills/)
2. Claude Code 全局目录 (~/.claude/skills/)
3. Cursor 全局目录 (~/.cursor/skills/)
4. 任意自定义指定目录 (--target / -t)
5. 当前目标工程目录

使用方法：
  python install.py                   # 交互式菜单安装
  python install.py --all             # 自动安装到所有检测到的支持平台
  python install.py --target <path>   # 安装到指定目录
  python install.py --link            # 使用软链接/符号链接模式（节省空间，实时同步修改）
  python install.py --list            # 查看全部可用 Skills
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

# 获取仓库根目录与 skills 源目录
REPO_ROOT = Path(__file__).resolve().parent
SKILLS_SRC = REPO_ROOT / ".agents" / "skills"


def get_available_skills():
    """获取所有可用的技能"""
    if not SKILLS_SRC.exists():
        print(f"[!] 找不到技能目录: {SKILLS_SRC}")
        return []
    
    skills = []
    for item in sorted(SKILLS_SRC.iterdir()):
        if item.is_dir() and (item / "SKILL.md").exists():
            skills.append(item)
    return skills


def detect_target_platforms():
    """检测当前电脑上存在的 AI 平台目录"""
    home = Path.home()
    targets = {}

    # 1. Antigravity 默认技能目录
    antigravity_paths = [
        home / ".gemini" / "antigravity" / "skills",
        home / ".gemini" / "config" / "skills",
    ]
    for p in antigravity_paths:
        if p.parent.exists():
            targets["Antigravity (" + str(p) + ")"] = p
            break
    if not any("Antigravity" in k for k in targets):
        # 即使目录尚未创建，提供默认推荐路径
        default_agy = home / ".gemini" / "antigravity" / "skills"
        targets["Antigravity (默认路径)"] = default_agy

    # 2. Claude Code 目录
    claude_path = home / ".claude" / "skills"
    targets["Claude Code (" + str(claude_path) + ")"] = claude_path

    # 3. Cursor 目录
    cursor_path = home / ".cursor" / "skills"
    targets["Cursor (" + str(cursor_path) + ")"] = cursor_path

    return targets


def copy_or_link_skill(src_dir: Path, dest_dir: Path, use_symlink: bool = False, force: bool = True):
    """安装单个 skill 到目标目录"""
    skill_name = src_dir.name
    target_skill_dir = dest_dir / skill_name

    dest_dir.mkdir(parents=True, exist_ok=True)

    if target_skill_dir.exists() or target_skill_dir.is_symlink():
        if not force:
            print(f"  [-] 跳过已存在: {skill_name}")
            return False
        # 删除旧版
        if target_skill_dir.is_symlink() or target_skill_dir.is_file():
            target_skill_dir.unlink()
        else:
            shutil.rmtree(target_skill_dir)

    if use_symlink:
        try:
            target_skill_dir.symlink_to(src_dir, target_is_directory=True)
            print(f"  [+] 链接成功: {skill_name} -> {target_skill_dir}")
            return True
        except (OSError, NotImplementedError):
            print(f"  [*] 符号链接权限不足，自动降级为复制模式: {skill_name}")
            shutil.copytree(src_dir, target_skill_dir)
            print(f"  [+] 复制成功: {skill_name} -> {target_skill_dir}")
            return True
    else:
        shutil.copytree(src_dir, target_skill_dir)
        print(f"  [+] 复制成功: {skill_name} -> {target_skill_dir}")
        return True


def install_skills(selected_skills, dest_dir: Path, use_symlink: bool = False):
    """批量安装技能"""
    print(f"\n========================================================")
    print(f"正在安装到目标目录: {dest_dir}")
    print(f"模式: {'符号链接 (Symlink)' if use_symlink else '文件拷贝 (Copy)'}")
    print(f"安装数量: {len(selected_skills)} 个 Skills")
    print(f"========================================================")

    success_count = 0
    for s in selected_skills:
        if copy_or_link_skill(s, dest_dir, use_symlink=use_symlink, force=True):
            success_count += 1

    print(f"\n[✓] 安装完成！成功安装 {success_count}/{len(selected_skills)} 个 Skills 到: {dest_dir}")
    return success_count


def get_skill_description(skill_dir: Path) -> str:
    """提取 skill 的简短描述"""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ""
    with open(skill_md, "r", encoding="utf-8", errors="ignore") as f:
        in_desc = False
        desc_lines = []
        for line in f:
            stripped = line.strip()
            if stripped.startswith("description:"):
                val = stripped.replace("description:", "").strip()
                if val and val != "|":
                    return val
                in_desc = True
                continue
            if in_desc:
                if line.startswith("  ") or line.startswith("\t"):
                    desc_lines.append(stripped)
                    if len(" ".join(desc_lines)) > 80:
                        break
                elif stripped.startswith("---") or (stripped and not line.startswith(" ")):
                    break
        if desc_lines:
            return " ".join(desc_lines)
    return ""


def list_skills():
    """打印技能列表"""
    skills = get_available_skills()
    print(f"\n当前仓库共有 {len(skills)} 个转化好的 Skills:")
    print("-" * 80)
    for i, s in enumerate(skills, 1):
        desc = get_skill_description(s)
        desc_preview = (desc[:50] + "...") if len(desc) > 50 else desc
        print(f" {i:2d}. {s.name:<38} | {desc_preview}")
    print("-" * 80)


def interactive_menu():
    """交互式安装向导"""
    skills = get_available_skills()
    if not skills:
        print("[!] 没有找到可安装的技能。")
        return

    platforms = detect_target_platforms()

    print("\n" + "=" * 60)
    print("      Book_Skill_Animtion 动画/影视 Skills 安装向导")
    print("=" * 60)
    print("检测到以下可用目标路径：")
    platform_list = list(platforms.items())
    for idx, (name, path) in enumerate(platform_list, 1):
        status = "[已存在]" if path.parent.exists() else "[可新建]"
        print(f"  [{idx}] {name} {status}")
    print(f"  [{len(platform_list) + 1}] 自定义目标目录")
    print(f"  [{len(platform_list) + 2}] 全部安装到以上所有平台")

    try:
        choice = input(f"\n请选择目标平台 (1-{len(platform_list) + 2}, 默认 1): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n已取消。")
        return

    if not choice:
        choice = "1"

    dest_paths = []
    try:
        c_num = int(choice)
        if 1 <= c_num <= len(platform_list):
            dest_paths.append(platform_list[c_num - 1][1])
        elif c_num == len(platform_list) + 1:
            custom = input("请输入自定义目标完整路径: ").strip()
            if custom:
                dest_paths.append(Path(custom).expanduser().resolve())
            else:
                print("[!] 路径为空，取消操作。")
                return
        elif c_num == len(platform_list) + 2:
            dest_paths.extend([p for _, p in platform_list])
        else:
            print("[!] 无效选项。")
            return
    except ValueError:
        print("[!] 请输入有效数字。")
        return

    use_symlink = False
    symlink_choice = input("\n是否使用符号链接模式(软链接，修改即生效)? (y/N, 默认 N 复制): ").strip().lower()
    if symlink_choice in ("y", "yes"):
        use_symlink = True

    for dest in dest_paths:
        install_skills(skills, dest, use_symlink=use_symlink)

    print("\n恭喜！所有选中的动画 AI 技能已就绪，可在对应 AI 客户端中即刻调用！\n")


def main():
    parser = argparse.ArgumentParser(
        description="Book_Skill_Animtion: 动画与影视视听 AI Skills 快速安装器"
    )
    parser.add_argument("--list", "-l", action="store_true", help="列出所有可用的 Skills")
    parser.add_argument("--target", "-t", type=str, help="指定安装目标目录")
    parser.add_argument("--all", "-a", action="store_true", help="自动安装到所有检测到的平台目录")
    parser.add_argument("--link", action="store_true", help="使用软链接模式进行安装")
    parser.add_argument("--skills", nargs="+", help="指定要安装的 skill 名称（默认全部）")

    args = parser.parse_args()

    if args.list:
        list_skills()
        return

    all_skills = get_available_skills()
    if not all_skills:
        print("[!] 未找到任何 Skills。")
        sys.exit(1)

    selected = all_skills
    if args.skills:
        wanted = set(args.skills)
        selected = [s for s in all_skills if s.name in wanted]
        if not selected:
            print(f"[!] 找不到匹配的 skills: {args.skills}")
            sys.exit(1)

    if args.target:
        target_path = Path(args.target).expanduser().resolve()
        install_skills(selected, target_path, use_symlink=args.link)
        return

    if args.all:
        platforms = detect_target_platforms()
        for _, path in platforms.items():
            install_skills(selected, path, use_symlink=args.link)
        return

    # 无参数时进入交互式向导
    interactive_menu()


if __name__ == "__main__":
    main()
