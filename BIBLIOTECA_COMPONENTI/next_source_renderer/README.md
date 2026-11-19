# RXN-glowing-send-input — genuine Next.js source fixture

Only for reference screenshots. Next.js runs the **unmodified archived** Ruixen source `BIBLIOTECA_COMPONENTI/sorgenti/ruixen/glowing-send-input.tsx` (`a7a0d3dd2785d9a708a5d8a654637547af2fa235` Git blob at pinned Ruixen commit `f6b20860623fa39122ac2b5f0e5bd29a9eb10941`).

The original imports `next/font/google` with Poppins 500. Unlike the isolated Vite renderer, this fixture compiles it through the actual Next.js webpack loader. It does **not** alter source, spoof fonts, or claim a screenshot when the font cannot load.

`python BIBLIOTECA_COMPONENTI/capture_next_font_preview.py` starts the isolated Next dev server, checks the exact original Git blob and real font style, captures the component itself, and records SHA256/provenance. This is documentary evidence only: visual QA and Flutter consumer status stay UNREVIEWED / NOT_VERIFIED. The runner may need internet to fetch the official Poppins font during compilation; if the fetch fails the capture must fail without inventing an image.
