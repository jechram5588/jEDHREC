import json, os, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
req = urllib.request.Request('https://api.scryfall.com/sets', headers={'User-Agent': 'Jedhrec/1.0', 'Accept': 'application/json'})
sets = json.load(urllib.request.urlopen(req, timeout=60))['data']
out = {s['name'].lower(): s['code'].upper() for s in sets}
json.dump(out, open(os.path.join(here, 'sf', 'sets.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'sets', os.path.getsize(os.path.join(here, 'sf', 'sets.json')), 'bytes')
