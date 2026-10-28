import csv, glob, json, os, re, sys, unicodedata
from PIL import Image
src, outdir, local_out = sys.argv[1:4]
here = os.path.dirname(os.path.abspath(__file__))
COLS, ROWS, W, H = 10, 6, 300, 418
def norm(s): return unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode()
meta = json.load(open(os.path.join(here, 'sf', 'meta.json'), encoding='utf-8'))
decks = []
for i, f in enumerate(sorted(glob.glob(os.path.join(src, '*.csv')))):
    name = os.path.basename(f).split('_')[0]
    cards = []
    with open(f, encoding='utf-8-sig') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            if not r.get('Name'): continue
            cards.append({'q': int(re.sub(r'\D', '', r['QuantityX']) or 1), 'n': r['Name'].strip(), 'e': (r['Edition'] or '').strip(),
                          'f': 'foil' in (r['Foil'] or '').lower(), 'p': float(re.sub(r'[^0-9.]', '', r['Price'] or '') or 0)})
    cmd = [c['n'] for c in cards if norm(c['n']).startswith(norm(name))][:1]
    decks.append({'id': 'd%d' % i, 'name': name, 'cmd': cmd, 'cards': cards})
# sprite sheets, packed deck by deck so a deck touches few sheets
order = []
for d in decks:
    for c in d['cards']:
        if c['n'] in meta and meta[c['n']].get('file') and c['n'] not in order: order.append(c['n'])
os.makedirs(os.path.join(outdir, 'img'), exist_ok=True)
per = COLS * ROWS
for s in range(0, len(order), per):
    sheet = Image.new('RGB', (COLS * W, ROWS * H), (40, 40, 40))
    for k, n in enumerate(order[s:s + per]):
        im = Image.open(os.path.join(here, 'sf', 'img', meta[n]['file'])).convert('RGB').resize((W, H), Image.LANCZOS)
        sheet.paste(im, ((k % COLS) * W, (k // COLS) * H))
        meta[n]['sp'] = [s // per, k]
    sheet.save(os.path.join(outdir, 'img', 's%d.jpg' % (s // per)), quality=80, optimize=True, progressive=True)
clean = {n: {k: v for k, v in m.items() if k != 'file'} for n, m in meta.items()}
data = {'savedAt': '2026-10-27T12:00:00Z', 'decks': decks, 'meta': clean}
t = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
json.dump(data, open(os.path.join(outdir, 'decks.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
open(os.path.join(outdir, 'index.html'), 'w', encoding='utf-8').write(t.replace('__DATA__', 'null'))
local_data = {**data, 'meta': {n: {k: v for k, v in m.items() if k != 'sp'} for n, m in clean.items()}}
page = t.replace('__DATA__', json.dumps(local_data, ensure_ascii=False, separators=(',', ':')).replace('<', '\u003c'))
open(local_out, 'w', encoding='utf-8').write('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}[hidden]{display:none!important}</style></head><body>\n' + page + '\n</body></html>')
print('sheets', -(-len(order) // per), 'cards', len(order))
