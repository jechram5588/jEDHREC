import base64, json, re, urllib.request, os, time
here = os.path.dirname(os.path.abspath(__file__))
H = {'User-Agent': 'Jedhrec/1.0', 'Accept': 'application/json'}
meta = json.load(open(os.path.join(here, 'sf', 'meta.json'), encoding='utf-8'))
used = set()
for m in meta.values(): used.update(re.findall(r'\{[^}]+\}', m.get('m', '')))
want = used | {'{W}', '{U}', '{B}', '{R}', '{G}', '{C}', '{X}'} | {'{%d}' % i for i in range(0, 17)}
req = urllib.request.Request('https://api.scryfall.com/symbology', headers=H)
syms = json.load(urllib.request.urlopen(req, timeout=60))['data']
out = {}
for s in syms:
    if s['symbol'] in want and s.get('svg_uri'):
        r = urllib.request.Request(s['svg_uri'], headers={'User-Agent': H['User-Agent']})
        svg = urllib.request.urlopen(r, timeout=60).read()
        out[s['symbol']] = 'data:image/svg+xml;base64,' + base64.b64encode(svg).decode()
        time.sleep(0.05)
json.dump(out, open(os.path.join(here, 'sf', 'symbols.json'), 'w'), separators=(',', ':'))
print(len(out), 'symbols', sum(len(v) for v in out.values()), 'bytes; missing:', sorted(want - set(out)))
