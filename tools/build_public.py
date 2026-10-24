"""Build the public, self-contained page "Mathematics and AI": Storylines and the Reading room.
Usage: python3 build_public.py <resources_dir> <out.html> [site_text.json] [form.json]
- resources_dir: folder of <doc_id>.json files exported from the artifact's "resources" collection
- site_text.json: optional export of the "site/text" document (page-text edits)
- form.json: optional {"action": "...formResponse", "fields": {"url": "entry.X", "title": "...", "cat": "...", "why": "..."}}
"""
import json, sys, glob, os, re, datetime
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "maths-ai.html")).read()
res_dir, out = sys.argv[1], sys.argv[2]
text = {}
if len(sys.argv) > 3 and os.path.exists(sys.argv[3]):
    d = json.load(open(sys.argv[3])); d = d.get('data', d); d.pop('_updated', None); text = d
form = None
if len(sys.argv) > 4 and os.path.exists(sys.argv[4]):
    form = json.load(open(sys.argv[4]))
items = []
for f in sorted(glob.glob(os.path.join(res_dir, '*.json'))):
    d = json.load(open(f)); data = d.get('data', d)
    data['id'] = d.get('id', os.path.basename(f)[:-5])
    items.append(data)
payload = {"items": items, "text": text, "form": form,
           "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}
src = src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
inject = '<script>window.READING_ROOM_PUBLIC = ' + json.dumps(payload, ensure_ascii=False).replace('</', '<\\/') + ';</script>\n'
src = src.replace('<script>\nconst CATS', inject + '<script>\nconst CATS', 1)
assert 'READING_ROOM_PUBLIC =' in src
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="description" content="Mathematics makes modern AI possible. AI is revolutionising mathematics. Two intertwined storylines from Turing to today, and a reading room of statements, letters, essays, films and more. A personal page by Jan Obłój.">\n'
        '<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">\n'
        '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">\n'
        '<meta property="og:type" content="website">\n'
        '<meta property="og:site_name" content="Mathematics and AI">\n'
        '<meta property="og:title" content="Mathematics and AI">\n'
        '<meta property="og:description" content="Mathematics makes modern AI possible. AI is revolutionising mathematics. Two intertwined storylines from Turing to today, and a reading room of statements, letters, essays, films and more. A personal page by Jan Obłój.">\n'
        '<meta property="og:url" content="https://janobloj.github.io/Maths-and-AI/">\n'
        '<meta property="og:image" content="https://janobloj.github.io/Maths-and-AI/og-image.png">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta property="og:image:alt" content="A Penrose-tiling mark beside the title Mathematics and AI">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:image" content="https://janobloj.github.io/Maths-and-AI/og-image.png">\n'
        '<style>html,body{margin:0}</style>\n</head>\n<body>\n' + src + '\n</body>\n</html>\n')
open(out, 'w').write(page)
print(out, len(items), 'entries', 'form' if form else 'no form', len(page)//1024, 'KB')
