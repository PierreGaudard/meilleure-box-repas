#!/bin/zsh
# usage: sc.sh <mdfile> <briefId> <dataJsonName>
KEY="dfk_HFyaak33DxoUGiXd0PV0ehonsX_VK-QFxSEX6oS-6xE"
BASE="https://datafer.analytics-e0d.workers.dev"
md="$1"; id="$2"; dj="$3"
cd ~/Desktop/SEO-Claude/PBN/meilleure-box-repas
python3 - "$md" <<'PY'
import re,json,sys
exec(open('.datafer/score.py').read().split('mdfile=')[0])
md=open(sys.argv[1],encoding='utf-8').read()
html='<h1>'+get_title(md)+'</h1>\n'+md_to_html(md)
json.dump({"editorHtml":html}, open('.datafer/payload.json','w'))
print("words=",len(re.sub(r'<[^>]+>',' ',html).split()),"imgs=",html.count('<img'))
PY
curl -s --max-time 90 -X POST "$BASE/api/v1/briefs/$id/content" -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" --data @.datafer/payload.json | python3 -c "import sys,json;d=json.load(sys.stdin);c=d.get('competitors') or {};b=d.get('breakdown') or {};print('SCORE=',d.get('score'),'best=',c.get('best'),'avg=',c.get('avg'));print('  len',(b.get('contentLength') or {}).get('score'),'/7  img',(b.get('images') or {}).get('score'),'/4  head',(b.get('headings') or {}).get('score'),'/13  place',(b.get('placement') or {}).get('score'),'/13  kw',(b.get('keyword') or {}).get('score'),'/15  nlp',(b.get('nlpCoverage') or {}).get('score'),'/27')"
if [ -n "$dj" ]; then
python3 - "$md" ".datafer/data/$dj" <<'PY'
import json,unicodedata,sys
art=open(sys.argv[1],encoding='utf-8').read().lower()
d=json.load(open(sys.argv[2]))
def norm(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn')
artn=norm(art)
miss=[t['term'] for t in (d.get('targetTerms') or []) if norm(t['term'].lower()) not in artn]
print("MANQUANTS("+str(len(miss))+"):", ', '.join(miss))
PY
fi
