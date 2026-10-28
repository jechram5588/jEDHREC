import csv, glob, json, os, sys, time, urllib.request
src, outdir = sys.argv[1], sys.argv[2]
H = {'User-Agent': 'Jedhrec/1.0', 'Accept': 'application/json'}
def get(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None, headers={**H, **({'Content-Type': 'application/json'} if body else {})})
    with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)
sets = {s['name'].lower(): s['code'] for s in get('https://api.scryfall.com/sets')['data']}
pairs = {}
for f in glob.glob(os.path.join(src, '*.csv')):
    with open(f, encoding='utf-8-sig') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            if r.get('Name'): pairs.setdefault(r['Name'].strip(), (r['Edition'] or '').strip())
def lookup_name(n): return n.split(' // ')[0] if ' // ' in n else n
def query(idents):
    found = {}
    for i in range(0, len(idents), 75):
        res = get('https://api.scryfall.com/cards/collection', {'identifiers': [x[1] for x in idents[i:i+75]]})
        time.sleep(0.12)
        # results come back in request order minus not_found
        nf = {json.dumps(x, sort_keys=True) for x in res.get('not_found', [])}
        it = iter(res['data'])
        for key, ident in idents[i:i+75]:
            if json.dumps(ident, sort_keys=True) in nf: continue
            found[key] = next(it)
    return found
idents = []
for n, ed in pairs.items():
    ident = {'name': lookup_name(n)}
    if ed.lower() in sets: ident['set'] = sets[ed.lower()]
    idents.append((n, ident))
found = query(idents)
missing = [(n, {'name': lookup_name(n)}) for n in pairs if n not in found]
found.update(query(missing))
print('found', len(found), 'of', len(pairs), 'missing:', [n for n in pairs if n not in found])
meta = {}
for n, c in found.items():
    face = (c.get('card_faces') or [c])[0]
    img = (c.get('image_uris') or face.get('image_uris') or {}).get('normal', '')
    meta[n] = {'t': face.get('type_line') or c.get('type_line', ''), 'm': face.get('mana_cost', c.get('mana_cost', '')),
               'cmc': c.get('cmc', 0), 'ci': ''.join(c.get('color_identity', [])), 'img': img, 'u': c.get('scryfall_uri', '').split('?')[0]}
    faces = c.get('card_faces') or []
    if len(faces) > 1 and faces[1].get('image_uris'): meta[n]['b'] = faces[1]['image_uris']['normal']  # back of a double-faced card
json.dump(meta, open(os.path.join(outdir, 'meta.json'), 'w', encoding='utf-8'), ensure_ascii=False)
os.makedirs(os.path.join(outdir, 'img'), exist_ok=True)
for i, (n, m) in enumerate(sorted(meta.items())):
    p = os.path.join(outdir, 'img', '%d.jpg' % abs(hash(n) % 10**12))
    m['file'] = os.path.basename(p)
    if m['img'] and not os.path.exists(p):
        req = urllib.request.Request(m['img'], headers={'User-Agent': H['User-Agent']})
        with urllib.request.urlopen(req, timeout=60) as r, open(p, 'wb') as o: o.write(r.read())
        time.sleep(0.08)
json.dump(meta, open(os.path.join(outdir, 'meta.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('images done')
