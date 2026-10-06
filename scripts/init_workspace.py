#!/usr/bin/env python3
"""Copy a language's starter templates into a NEW private directory. No network."""
import argparse
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def initialize(destination: Path, language: str) -> Path:
    locales = json.loads((ROOT / 'locales.json').read_text())['locales']
    if language not in locales:
        raise ValueError('Unsupported language: ' + language)
    raw = destination.expanduser()
    if raw.exists() or raw.is_symlink():
        raise ValueError('Destination already exists; choose a new directory. Nothing was changed.')
    dest = raw.resolve()
    if dest == ROOT or ROOT in dest.parents:
        raise ValueError('Keep personal work outside this public repository; choose another destination.')
    source = ROOT / locales[language]['templates']
    files = list(source.iterdir())
    if not files or any(p.is_symlink() or not p.is_file() for p in files):
        raise ValueError('Templates must be regular files; source is incomplete or contains a symlink.')
    # Exclusive creation is the overwrite guard; no force flag or merge mode.
    dest.mkdir(parents=True, exist_ok=False)
    (dest / 'coordination').mkdir()
    (dest / 'receipts').mkdir()
    (dest / 'templates').mkdir()
    for p in files:
        shutil.copyfile(p, dest / 'templates' / p.name)
    for src, target in [('AGENTS.example.md', 'AGENTS.md'),
                        ('AGENTS.example.md', 'CLAUDE.md'),
                        ('CONTRACT.example.md', 'coordination/CONTRACT.md'),
                        ('routing.example.json', 'coordination/routing.json')]:
        shutil.copyfile(source / src, dest / target)
    chinese = language == 'zh-TW'
    (dest / 'tasks.md').write_text(
        '# 私人任務表\n\n依 templates/task-card.md 新增任務；目前沒有任務。\n' if chinese else
        '# Private task list\n\nAdd tasks using templates/task-card.md. No tasks yet.\n', encoding='utf-8')
    (dest / 'receipts' / 'dispatch-log.md').write_text(
        '# 派工紀錄\n\n| 時間 | 需求 | 判斷 | 對象 | 督導 |\n|---|---|---|---|---|\n' if chinese else
        '# Dispatch log\n\n| Time | Request | Decision | Target | Supervisor |\n|---|---|---|---|---|\n', encoding='utf-8')
    (dest / '.gitignore').write_text('*\n!.gitignore\n', encoding='utf-8')
    readme = (
        '# 你的私人總控工作區\n\n1. 替換 AGENTS.md、CLAUDE.md、coordination/CONTRACT.md 與 routing.json 中的佔位字。\n'
        '2. 兩份代理規則保持一致，指定不同督導／核對者。\n3. 用 templates/ 登記任務、派工與回報。\n'
        '4. 自行在此目錄開啟代理；工具沒有啟動任何服務或連線。\n\n此資料夾預設全部被 Git 忽略，以免公開私人資料。\n' if chinese else
        '# Your private coordinator workspace\n\n1. Replace placeholders in AGENTS.md, CLAUDE.md, coordination/CONTRACT.md and routing.json.\n'
        '2. Keep both agent rules aligned; choose distinct supervisors/reviewers.\n3. Use templates/ for tasks, dispatch and reports.\n'
        '4. Start your agents here yourself; this helper started no service or connection.\n\nGit ignores this folder contents by default to avoid accidental personal-data publication.\n')
    (dest / 'README.md').write_text(readme, encoding='utf-8')
    return dest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True, type=Path)
    parser.add_argument('--language', default='en')
    args = parser.parse_args()
    try:
        dest = initialize(args.dest, args.language)
    except (OSError, ValueError) as e:
        parser.exit(2, f'Cannot initialize: {e}\n')
    print(f'Created private workspace: {dest}\nRead its README.md and replace placeholders before starting agents.')


if __name__ == '__main__':
    main()
