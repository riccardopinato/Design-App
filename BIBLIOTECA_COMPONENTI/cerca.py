#!/usr/bin/env python3
"""Query the locally indexed App Factory Design-App component library.

Does not fetch remote files, infer licenses, or claim consumer implementation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

CATALOG = Path(__file__).with_name("CATALOGO.json")


def simplify(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(value or "").casefold()).strip("-")


def load_catalog(path: Path = CATALOG) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("unsupported component catalog schema")
    return data


def search(data: dict, *, id: str | None = None, testo: str | None = None,
           app: str | None = None, linguaggio: str | None = None,
           categoria: str | None = None, fonte: str | None = None,
           stato: str | None = None, tag: str | None = None,
           solo_sorgente: bool = False) -> list[dict]:
    if id:
        alias = data.get("aliases", {}).get(id.upper())
        id = alias["canonical_id"] if alias else id.upper()
    rows = []
    for item in data["components"]:
        if id and item["id"] != id:
            continue
        if app and simplify(app) not in (simplify(x) for x in item["apps"]):
            continue
        if linguaggio and simplify(linguaggio) not in simplify(item["language"]):
            continue
        if categoria and simplify(categoria) not in simplify(item["category"]):
            continue
        if fonte and simplify(fonte) not in simplify(item["source_site"]):
            continue
        if stato and item["archive_state"] != stato:
            continue
        if solo_sorgente and item["archive_state"] != "ARCHIVED_SOURCE":
            continue
        if tag and simplify(tag) not in (simplify(x) for x in item.get("tags", [])):
            continue
        if testo:
            haystack = " ".join(str(item.get(k) or "") for k in
                                ("id", "name", "category", "source_site",
                                 "language", "source_url", "notes"))
            if testo.casefold() not in haystack.casefold():
                continue
        rows.append(item)
    return rows


def main() -> None:
    p = argparse.ArgumentParser(description="Ricerca componenti Design-App")
    p.add_argument("--id", help="ID canonico o alias storico (es. UIV-107)")
    p.add_argument("--testo", help="Testo libero")
    p.add_argument("--app", help="App associata, es. annas-diary")
    p.add_argument("--linguaggio", "--lang", dest="linguaggio",
                   help="Flutter, TSX, HTML/CSS, SVG ...")
    p.add_argument("--categoria", help="Categoria")
    p.add_argument("--fonte", help="Ruixen, Uiverse, FCL, DevLibraries...")
    p.add_argument("--stato", choices=["ARCHIVED_SOURCE", "REFERENCE_ONLY"])
    p.add_argument("--tag", help="Tag semantico")
    p.add_argument("--solo-sorgente", action="store_true",
                   help="Solo elementi con codice originale archiviato")
    p.add_argument("--formato", choices=["markdown", "json"], default="markdown")
    p.add_argument("--limite", type=int, default=40,
                   help="Max risultati (0 = tutti)")
    args = p.parse_args()
    if args.limite < 0:
        p.error("--limite non puo' essere negativo")
    data = load_catalog()
    matches = search(data, id=args.id, testo=args.testo, app=args.app,
                     linguaggio=args.linguaggio, categoria=args.categoria,
                     fonte=args.fonte, stato=args.stato, tag=args.tag,
                     solo_sorgente=args.solo_sorgente)
    rows = matches if args.limite == 0 else matches[:args.limite]
    if args.formato == "json":
        print(json.dumps({"total": len(matches), "shown": len(rows),
                          "matches": rows}, ensure_ascii=False, indent=2))
        return
    print(f"Trovati {len(matches)} componenti. Visualizzati {len(rows)}.\n")
    print("| ID | Nome | Fonte | Linguaggio | Stato | Percorso sorgente |")
    print("|---|---|---|---|---|---|")
    for x in rows:
        values = [x["id"], x["name"], x["source_site"], x["language"],
                  x["archive_state"], x["archive_path"] or "-"]
        values = [str(v).replace("|", "\\|").replace("\n", " ") for v in values]
        print("| " + " | ".join(values) + " |")


if __name__ == "__main__":
    main()
