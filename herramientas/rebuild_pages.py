import os, sys
here = os.path.dirname(os.path.abspath(__file__))
local_path = sys.argv[1]
t = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
t = t.replace('__SYMBOLS__', open(os.path.join(here, 'sf', 'symbols.json'), encoding='utf-8').read())
t = t.replace('__SETS__', open(os.path.join(here, 'sf', 'sets.json'), encoding='utf-8').read().replace('<', '\\u003c'))
os.makedirs(os.path.join(here, 'site'), exist_ok=True)
open(os.path.join(here, 'site', 'index.html'), 'w', encoding='utf-8').write(t.replace('__DATA__', 'null'))
# Keep the data already embedded in the local page; only swap its code.
# A path that doesn't exist yet gets a page with no decks (same savedAt as build2.py, so a browser draft still applies).
tag = '<script type="application/json" id="deck-data">'
if os.path.exists(local_path):
    old = open(local_path, encoding='utf-8').read()
    a = old.index(tag) + len(tag)
    data = old[a:old.index('</script>', a)]
else:
    data = '{"savedAt":"2026-10-27T12:00:00Z","decks":[],"meta":{}}'
page = t.replace('__DATA__', data)
open(local_path, 'w', encoding='utf-8').write(
    '<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    '<style>body{margin:0}[hidden]{display:none!important}</style></head><body>\n' + page + '\n</body></html>')
print('ok', len(data))
