#!/usr/bin/env python3
"""Check source parity, local links, example routing and generic privacy hazards."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.git','.venv','dist','tmp','__pycache__'}


def source_files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(x in EXCLUDED for x in p.relative_to(ROOT).parts))


def validate():
    errors=[]
    locales=json.loads((ROOT/'locales.json').read_text())
    if locales['default']!='en':errors.append('English must remain the primary edition')
    expected={}
    for kind in ('docs','templates','diagrams'):
        expected[kind]={p.name for p in (ROOT/locales['locales']['en'][kind]).iterdir() if p.is_file()}
    for locale,config in locales['locales'].items():
        for kind in expected:
            actual={p.name for p in (ROOT/config[kind]).iterdir() if p.is_file()}
            if actual!=expected[kind]:errors.append(f'{locale}/{kind}: file parity mismatch')
        route=json.loads((ROOT/config['templates']/'routing.example.json').read_text())
        if route['precedence']!=['task_overrides','project_rules','keyword_rules','default_domain']:errors.append(f'{locale}: routing precedence')
        for name,d in route['domains'].items():
            if d['primary']==d['reviewer']:errors.append(f'{locale}/{name}: supervisor equals reviewer')
        cap=(ROOT/config['docs']/'13-capability-matrix.md').read_text()
        if len(re.findall(r'^\| \d+ \|',cap,re.M))!=70:errors.append(f'{locale}: expected 70 capability rows')
    if len(expected['docs'])!=18 or len(expected['templates'])!=14 or len(expected['diagrams'])!=10:
        errors.append('Expected 18 chapter files, 14 templates and 10 diagrams per locale')
    patterns={
        'private home path':r'/(?:Users|home)/[A-Za-z0-9_.-]+/',
        'private cloud URL':r'https?://(?:drive|mail|docs)\.google\.com/[^\s]+',
        'real runtime ID':r'\b(?:term|run|dispatch|msg)_[a-f0-9]{12,}\b',
        'credential-like string':r'\b(?:gh[pousr]_[A-Za-z0-9]{25,}|sk-(?:proj-|ant-)?[A-Za-z0-9_-]{25,})',
        'private key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    }
    checked=0
    for p in source_files():
        name=p.relative_to(ROOT).as_posix()
        if p.is_symlink():errors.append(name+': symlink');continue
        try:text=p.read_text(encoding='utf-8')
        except UnicodeDecodeError:errors.append(name+': unreviewed binary');continue
        checked+=1
        for kind,pattern in patterns.items():
            if re.search(pattern,text):errors.append(name+': '+kind)
        if p.suffix=='.json':
            try:json.loads(text)
            except ValueError:errors.append(name+': invalid JSON')
        if p.suffix=='.svg':
            try:svg=ET.fromstring(text)
            except ET.ParseError:errors.append(name+': invalid SVG');continue
            if not any(e.tag.endswith('title') for e in svg.iter()):errors.append(name+': SVG needs accessible title')
        if p.suffix=='.md':
            for ref in re.findall(r'\]\(([^)]+)\)',text):
                u=urlsplit(unquote(ref.strip('<>')))
                if u.scheme or u.netloc:continue
                target=(p.parent/u.path).resolve() if u.path else p
                if not target.is_relative_to(ROOT) or not target.exists():errors.append(name+': broken relative link '+ref)
            if name.startswith('docs/') and ('[English]' not in text or '[繁體中文]' not in text):errors.append(name+': missing language links')
    return checked,errors


if __name__=='__main__':
    count,errors=validate()
    print(json.dumps({'source_files':count,'errors':errors,'ok':not errors},ensure_ascii=False,indent=2))
    sys.exit(bool(errors))
