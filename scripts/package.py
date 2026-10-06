#!/usr/bin/env python3
"""Package only explicitly approved public source directories and built editions."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT=Path(__file__).resolve().parents[1]
TOP={'README.md','README.zh-TW.md','LICENSE','CONTRIBUTING.md','TRANSLATIONS.md','SECURITY.md','locales.json','requirements-build.txt','.gitignore'}
DIRECTORIES=('docs','templates','diagrams','scripts','tests','.github')


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--version',required=True);args=parser.parse_args()
    if not re.fullmatch(r'v\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?',args.version):parser.error('Use a version such as v1.0.0')
    out=ROOT/'dist';out.mkdir(exist_ok=True)
    files=[ROOT/n for n in sorted(TOP)]
    for name in DIRECTORIES:
        files.extend(p for p in (ROOT/name).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
    built=[]
    for locale in json.loads((ROOT/'locales.json').read_text())['locales']:
        for suffix in ('html','pdf'):
            p=out/f'handbook-{locale}.{suffix}'
            if not p.is_file():raise SystemExit(f'Missing {p.name}; build both HTML and PDF before packaging')
            built.append(p)
    files=sorted(set(files+built))
    if any(p.is_symlink() for p in files):raise SystemExit('Refusing symlink in package')
    manifest=''.join(f'{digest(p)}  {p.relative_to(ROOT).as_posix()}\n' for p in files)
    archive=out/f'orca-coordination-handbook-{args.version}.zip'
    prefix=f'orca-coordination-handbook-{args.version}/'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in files:z.write(p,prefix+p.relative_to(ROOT).as_posix())
        z.writestr(prefix+'SHA256SUMS',manifest)
    release_files=[archive]+built
    (out/'SHA256SUMS').write_text(''.join(f'{digest(p)}  {p.name}\n' for p in release_files))
    print(json.dumps({'archive':archive.name,'files':len(files)+1,'sha256':digest(archive)},indent=2))


if __name__=='__main__':main()
