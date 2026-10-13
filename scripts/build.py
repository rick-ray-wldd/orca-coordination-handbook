#!/usr/bin/env python3
"""Build self-contained locale HTML; optional PDF with an isolated Chrome profile."""
import argparse
import html
import json
from pathlib import Path
import re
import subprocess
import tempfile
import time
from urllib.parse import urlsplit

import markdown

ROOT=Path(__file__).resolve().parents[1]
REPO_URL='https://github.com/rick-ray-wldd/orca-coordination-handbook'
CSS='''
:root{color-scheme:light;--ink:#162e36;--muted:#52676e;--accent:#006e67;--line:#d4e1df;--paper:#fcfdfb;--soft:#eef4f1}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:5rem}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.75 system-ui,-apple-system,"PingFang TC","Noto Sans CJK TC","Microsoft JhengHei",sans-serif}
a{color:var(--accent);text-underline-offset:3px}a:focus-visible{outline:3px solid #df9900;outline-offset:4px}header{padding:32px max(20px,calc((100vw - 1140px)/2));background:#122e36;color:#f8fff9}header h1{font-size:clamp(2rem,5vw,3.5rem);line-height:1.12;max-width:800px;margin:16px 0}header p{max-width:750px;color:#cee0da}.eyebrow{font-size:12px;letter-spacing:.16em;text-transform:uppercase}.languages{display:flex;gap:18px;margin:16px 0}.languages a{color:#b9eedc}.layout{display:grid;grid-template-columns:230px minmax(0,1fr);gap:48px;max-width:1180px;margin:auto;padding:32px 20px 80px}aside{position:sticky;top:20px;align-self:start;max-height:90vh;overflow:auto;font-size:13px}aside ol{list-style:none;padding:0}aside li{margin:0 0 9px}aside a{text-decoration:none}main{min-width:0;max-width:850px}section{margin:0 0 64px;scroll-margin-top:24px}h1{font-size:1.95rem;line-height:1.3}h2{margin:32px 0 12px;font-size:1.35rem}h3{margin:24px 0 10px;font-size:1.08rem}p,li,td{overflow-wrap:anywhere}table{border-collapse:collapse;width:100%;font-size:14px;margin:20px 0;display:block;overflow-x:auto}th,td{border:1px solid var(--line);padding:9px 11px;text-align:left;vertical-align:top}th{background:var(--soft)}code{font:0.86em/1.6 ui-monospace,Menlo,Consolas,monospace;background:var(--soft);padding:2px 4px}pre{background:var(--soft);border:1px solid var(--line);border-radius:8px;padding:16px;white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}pre code{padding:0;background:none}blockquote{border-left:3px solid #b89048;margin:20px 0;padding:1px 18px;background:#f9f3e6}figure{margin:28px 0}figure svg{display:block;width:100%;height:auto;background:white;border:1px solid var(--line);border-radius:10px}figcaption{font-size:12px;color:var(--muted);margin-top:8px}.notice{border:1px solid var(--line);padding:18px;background:var(--soft);border-radius:8px}.chapter-switch{font-size:13px;border-bottom:1px solid var(--line);padding-bottom:12px}.template{padding-top:12px}footer{border-top:1px solid var(--line);padding:24px;color:var(--muted);text-align:center;font-size:13px}
@media(max-width:800px){.layout{display:block;padding:24px 16px}aside{position:static;max-height:none;padding-bottom:16px;border-bottom:1px solid var(--line);margin-bottom:32px}aside ol{columns:2;column-gap:20px}aside li{break-inside:avoid}table{font-size:13px}header{padding:30px 20px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{@page{size:A4;margin:16mm 14mm;@bottom-right{content:counter(page) " / " counter(pages);font:8pt Arial;color:#667}}body{font-size:10pt;background:white;color:#111}header{background:white;color:#111;padding:8mm 0 10mm}header h1{font-size:30pt}header p{color:#444}.languages,.chapter-switch,.notice{display:none}header{break-after:page}.layout{display:block;padding:0}aside{position:static;max-height:none;font-size:10pt;break-after:page}aside ol{columns:2}aside li{break-inside:avoid}main{max-width:none}section{break-before:page;margin-bottom:0}h1{font-size:20pt}h2{font-size:13pt}h3{font-size:11pt}h1,h2,h3{break-after:avoid}p{orphans:3;widows:3}table{display:table;font-size:8.5pt;table-layout:fixed;margin:10px 0 0}thead{display:table-header-group}tr{break-inside:avoid}th,td{padding:6px;overflow-wrap:anywhere}pre{font-size:8.4pt;line-height:1.55;break-inside:auto}figure{break-inside:avoid}figure svg{max-height:220mm}a{color:inherit;text-decoration:none}.template{break-before:page}.template:first-of-type{break-before:auto}footer{font-size:8pt}}
'''


def slug(name):return re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')


def build_html(locale,config,locales,out):
    # The capability matrix keeps its stable filename but is printed last, as Appendix A.
    docs=sorted((ROOT/config['docs']).glob('*.md'),key=lambda p:(p.stem.endswith('capability-matrix'),p.name))
    templates=sorted((ROOT/config['templates']).iterdir())
    chinese=locale=='zh-TW'
    title='Orca 個人雙總控工作流程手冊' if chinese else 'Orca Coordination Handbook'
    sub='清楚分工、單一 writer、證據與驗收。' if chinese else 'Clear ownership. One writer. Evidence before acceptance.'
    notice=('教學、模板與安全複製工具。私人參考部署的助理程式與資料庫未隨附。' if chinese else
            'Handbook, templates and a safe copy helper. The reference deployment’s private assistant runtime and database are not included.')
    sections=[];toc=[]
    def fix_href(match):
        ref=html.unescape(match.group(1))
        u=urlsplit(ref)
        if u.scheme or ref.startswith('#'):return match.group(0)
        target=(current.parent/u.path).resolve()
        if target.is_relative_to(ROOT/'docs'):
            targetlocale=target.parent.name
            prefix='' if targetlocale==locale else f'handbook-{targetlocale}.html'
            return f'href="{prefix}#{slug(target.stem)}"'
        if target.is_relative_to(ROOT/'templates'):
            targetlocale=target.parent.name
            prefix='' if targetlocale==locale else f'handbook-{targetlocale}.html'
            return f'href="{prefix}#template-{slug(target.name)}"'
        if target.name.startswith('README'):return 'href="#top"'
        return f'href="{html.escape(REPO_URL+"/blob/main/"+target.relative_to(ROOT).as_posix())}"'
    for current in docs:
        text=current.read_text()
        text=re.sub(r'^\[English\].*\[Home\].*\n','',text,flags=re.M)
        body=markdown.markdown(text,extensions=['tables','fenced_code','sane_lists'])
        def inline_svg(m):
            src=html.unescape(m.group(2));p=(current.parent/src).resolve()
            if not p.is_relative_to(ROOT/'diagrams'):raise ValueError('Diagram outside approved directory')
            svg=p.read_text()
            return f'<figure>{svg}<figcaption>{m.group(1)}</figcaption></figure>'
        body=re.sub(r'<p><img alt="([^"]*)" src="([^"]+\.svg)"\s*/?></p>',inline_svg,body)
        body=re.sub(r'href="([^"]+)"',fix_href,body)
        chapterid=slug(current.stem)
        heading=re.search(r'<h1>(.*?)</h1>',body).group(1)
        toc.append(f'<li><a href="#{chapterid}">{heading}</a></li>')
        switches=' · '.join(f'<a href="handbook-{tag}.html#{chapterid}" lang="{tag}">{html.escape(c["label"])}</a>' for tag,c in locales.items())
        sections.append(f'<section id="{chapterid}"><div class="chapter-switch">{switches}</div>{body}</section>')
    label='附錄 B：模板全文' if chinese else 'Appendix B. Full templates'
    toc.append(f'<li><a href="#templates">{label}</a></li>')
    appendix=[f'<section id="templates"><h1>{label}</h1>']
    for p in templates:
        appendix.append(f'<div class="template" id="template-{slug(p.name)}"><h2>{html.escape(p.name)}</h2><pre><code>{html.escape(p.read_text())}</code></pre></div>')
    appendix.append('</section>');sections.append(''.join(appendix))
    nav=''.join(f'<a href="handbook-{tag}.html" lang="{tag}">{html.escape(c["label"])}</a>' for tag,c in locales.items())
    content=f'''<!doctype html><html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head><body><header id="top"><div class="eyebrow">Independent community edition · 2026-10 · MIT</div><h1>{title}</h1><p>{sub}</p><nav class="languages" aria-label="Language">{nav}</nav></header><div class="layout"><aside aria-label="Contents"><strong>{'目錄' if chinese else 'CONTENTS'}</strong><ol>{''.join(toc)}</ol></aside><main><p class="notice">{notice}</p>{''.join(sections)}</main></div><footer>Orca CLI 1.4.220 reference · Offline reader · Markdown sources in docs/{locale}/</footer></body></html>'''
    target=out/f'handbook-{locale}.html';target.write_text(content,encoding='utf-8');return target


def print_pdf(source,browser):
    from pypdf import PdfReader,PdfWriter
    from pypdf.generic import ArrayObject,NameObject
    with tempfile.TemporaryDirectory(prefix='handbook-print-') as tmp:
        raw=Path(tmp)/'raw.pdf'
        command=[str(browser),'--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check',f'--user-data-dir={Path(tmp)/"profile"}',
                 '--no-pdf-header-footer',f'--print-to-pdf={raw}',source.as_uri()]
        proc=subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        deadline=time.monotonic()+120;last=-1;stable=0
        while time.monotonic()<deadline:
            size=raw.stat().st_size if raw.exists() else -1
            stable=stable+1 if size>0 and size==last else 0;last=size
            if stable>=3 or (proc.poll() is not None and size>0):break
            if proc.poll() is not None:break
            time.sleep(1)
        if proc.poll() is None:
            proc.terminate()
            try:proc.wait(timeout=8)
            except subprocess.TimeoutExpired:proc.kill();proc.wait()
        if not raw.exists() or raw.stat().st_size==0:raise RuntimeError('Browser produced no PDF; check executable and sandbox support')
        reader=PdfReader(raw);writer=PdfWriter();writer.clone_document_from_reader(reader)
        writer.metadata=None
        writer.add_metadata({'/Title':source.stem,'/Author':'Orca Handbook Contributors','/Creator':'Handbook build','/Producer':'Handbook build'})
        writer._root_object.pop('/Metadata',None)
        for page in writer.pages:
            annotations=[]
            for reference in page.get('/Annots',[]):
                annotation=reference.get_object();action=annotation.get('/A',{})
                if str(action.get('/URI','')).startswith('file:'):continue
                annotations.append(reference)
            if '/Annots' in page:page[NameObject('/Annots')]=ArrayObject(annotations)
        writer.write(source.with_suffix('.pdf'))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf',action='store_true')
    parser.add_argument('--browser',type=Path)
    args=parser.parse_args()
    if args.pdf and (not args.browser or not args.browser.is_file()):parser.error('--pdf requires --browser pointing to a Chrome/Chromium executable')
    locales=json.loads((ROOT/'locales.json').read_text())['locales'];out=ROOT/'dist';out.mkdir(exist_ok=True)
    for locale,config in locales.items():
        target=build_html(locale,config,locales,out)
        if args.pdf:print_pdf(target,args.browser.resolve())
        print(target.name + (' + PDF' if args.pdf else ''))


if __name__=='__main__':main()
