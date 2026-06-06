import sys, re, json, urllib.request

KEY="dfk_HFyaak33DxoUGiXd0PV0ehonsX_VK-QFxSEX6oS-6xE"
BASE="https://datafer.analytics-e0d.workers.dev"

def md_to_html(md):
    # strip frontmatter
    if md.startswith('---'):
        md = md.split('---',2)[2]
    lines = md.split('\n')
    html=[]; i=0; intable=False
    def inline(t):
        t=re.sub(r'!\[(.*?)\]\((.+?)\)', r'<img src="\2" alt="\1">', t)
        t=re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t=re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', t)
        return t
    title=None
    while i < len(lines):
        l=lines[i].rstrip()
        if not l.strip():
            i+=1; continue
        if l.startswith('## '):
            html.append('<h2>'+inline(l[3:])+'</h2>')
        elif l.startswith('### '):
            html.append('<h3>'+inline(l[4:])+'</h3>')
        elif l.startswith('# '):
            html.append('<h1>'+inline(l[2:])+'</h1>')
        elif l.startswith('|'):
            # table block
            rows=[]
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append(lines[i].strip()); i+=1
            html.append('<table>')
            for ri,r in enumerate(rows):
                cells=[c.strip() for c in r.strip('|').split('|')]
                if set(''.join(cells))<=set('-: '): continue
                tag='th' if ri==0 else 'td'
                html.append('<tr>'+''.join('<%s>%s</%s>'%(tag,inline(c),tag) for c in cells)+'</tr>')
            html.append('</table>')
            continue
        elif l.startswith('- '):
            html.append('<ul>')
            while i < len(lines) and lines[i].lstrip().startswith('- '):
                html.append('<li>'+inline(lines[i].lstrip()[2:])+'</li>'); i+=1
            html.append('</ul>')
            continue
        else:
            html.append('<p>'+inline(l)+'</p>')
        i+=1
    return '\n'.join(html)

def get_title(md):
    m=re.search(r'^title:\s*"?(.+?)"?\s*$', md, re.M)
    return m.group(1) if m else ''

mdfile=sys.argv[1]; brief_id=sys.argv[2]
md=open(mdfile,encoding='utf-8').read()
title=get_title(md)
body=md_to_html(md)
html='<h1>'+title+'</h1>\n'+body
data=json.dumps({"editorHtml":html}).encode()
req=urllib.request.Request(BASE+"/api/v1/briefs/"+brief_id+"/content", data=data, method='POST',
    headers={"Authorization":"Bearer "+KEY,"Content-Type":"application/json"})
try:
    r=urllib.request.urlopen(req, timeout=60)
    res=json.load(r)
    comp=res.get('competitors') or {}
    print(f"SCORE={res.get('score')}  best={comp.get('best')}  avg={comp.get('avg')}")
    bd=res.get('breakdown') or {}
    if bd: print("breakdown:", json.dumps(bd)[:500])
    # words
    txt=re.sub(r'<[^>]+>',' ',html); print("words=", len(txt.split()))
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode()[:300])
