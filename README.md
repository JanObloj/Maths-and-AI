# Mathematics and AI

A personal page by Jan Obłój (Oxford Mathematics in conversation on AI). It has three views:
- **Storylines:** a timeline of how mathematics made modern AI possible and how AI is changing mathematics, from Turing to today.
- **Reading room:** a curated list of statements, letters, essays, films and more.
- **ToolKit:** a curated, fact-checked directory of AI models, provers and tools for doing mathematics, with sources and the date each entry was last checked.

The selection, the milestones and the curator's notes are personal. They do not represent the Mathematical Institute or the University of Oxford.

The published page is `index.html`, served by GitHub Pages. It is generated, so don't edit it by hand.

## How it is updated
- The working copy lives in a private page in Claude. That page holds a small database of reading-room entries (`resources`) and page text (`site/text`).
- Each morning a scheduled Claude task does the following:
  - looks for new material;
  - reviews visitor proposals and recommends them to Jan, who approves what is added;
  - exports the entries to `data/resources/`;
  - rebuilds `index.html` with `tools/build_public.py`;
  - commits the result here.

## Files
- `index.html`: the public page. It is self-contained; the only external calls are for fonts.
- `src/maths-ai.html`: the page source shared with the Claude version. The Storylines and ToolKit data are embedded in it.
- `tools/build_public.py`: builds `index.html` from `data/`. Run `python3 tools/build_public.py data/resources index.html data/site-text.json data/form.json`.
- `data/resources/*.json`: one file per reading-room entry.
- `data/form.json`: where the proposals form sends submissions.

## Copyright
© 2026 Jan Obłój. All rights reserved. You are welcome to link to the page and to quote short passages with credit. The linked articles, papers and posts belong to their authors and publishers.
