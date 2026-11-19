#!/usr/bin/env python3
"""Exhaustive, auditable outcome report for the frozen 119 missing preview UIDs.

A checked source or error is not a preview. The only captured state requires a
physical PNG plus an original-specific provenance record with SHA256.
"""
from __future__ import annotations
import hashlib,json,re
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"BIBLIOTECA_COMPONENTI"
BASE=HERE/"BASELINE_119_ANTEPRIME_2026-11-19.json"
CAT=HERE/"CATALOGO.json"
MAN=HERE/"ANTEPRIME.json"
UIDS=HERE/"UID_REGISTRY.json"
RU=HERE/"ANTEPRIME_ORIGINI.json"
GF=HERE/"ANTEPRIME_ORIGINI_GENTLEFACE.json"
FUI=HERE/"ANTEPRIME_ORIGINI_FORUI.json"
SEC=HERE/"ANTEPRIME_ORIGINI_SECONDARIE.json"
FCL=HERE/"FCL_CAPTURE_REPORT.json"
TSX=HERE/"RENDER_ARCHIVED_TSX_BATCH_REPORT.json"
REPORT=HERE/"RECUPERO_119_ESITI.json"
MARKDOWN=HERE/"RECUPERO_119_ESITI.md"

def read(path,default):
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else default

def main():
    baseline=read(BASE,{})
    catalog=read(CAT,{}).get("components",[])
    preview=read(MAN,{}).get("previews",{})
    uids=read(UIDS,{}).get("entries",[])
    assert baseline.get("baseline_count")==119 and len(baseline["ids"])==119
    assert len(catalog)==len(uids)==len(preview)==480
    canonical={c["id"]:c for c in catalog}
    linked={e["canonical_id"]:e["uid"] for e in uids}
    known=set(canonical)
    for cid in [r["canonical_id"] for r in baseline["ids"]]:
        assert cid in known
    prov={}
    for p in (RU,GF,FUI,SEC):
        for cid,val in read(p,{}).get("previews",{}).items():
            if cid in prov: raise ValueError("Duplicate source provenance for "+cid)
            prov[cid]=val
    renders=read(TSX,{})
    fcl=read(FCL,{})
    captured=set(renders.get("captured",[]))
    captured_fcl=set(fcl.get("captured",[]))
    fail=renders.get("failed",{})
    blocked_before=renders.get("blocked_before_run",{})
    fail_fcl=fcl.get("blocked",{})
    rows=[]
    for b in baseline["ids"]:
        cid=b["canonical_id"]
        cat=canonical[cid]
        entry=preview[cid]
        file=entry.get("image_path")
        original=cat.get("archive_path")
        origin=prov.get(cid)
        if file:
            p=ROOT/file
            if not p.is_file() or not origin:
                raise ValueError(cid+": manifest claims image without PNG or provenance")
            digest=hashlib.sha256(p.read_bytes()).hexdigest()
            if digest != origin.get("preview_sha256"):
                raise ValueError(cid+": preview SHA not proven")
            code="PNG_ARCHIVED_SHA_VERIFIED_VISUAL_QA_PENDING"
            reason="PNG reale acquisita e SHA256 verificato; revisione visiva e uso nell'app non ancora certificati"
            evidence=[file,origin.get("capture_mode",""),"SHA256:"+digest]
        else:
            digest=None
            evidence=[]
            if cat.get("archive_state")=="REFERENCE_ONLY" and not original:
                if cat["source_site"]=="FLUTTER_COMPONENT_LIBRARY":
                    if cid in fail_fcl:
                        code="BLOCKED_PUBLIC_DEMO_CAPTURE"
                        reason="Tentativo demo ufficiale fallito: "+str(fail_fcl[cid])[:250]
                    elif cid in captured_fcl:
                        raise ValueError(cid+": FCL report claims capture, but PNG missing")
                    else:
                        code="PUBLIC_DEMO_CAPTURE_NOT_YET_ATTEMPTED"
                        reason="Esiste URL pubblico di demo; nessun Dart originale o licenza verificata, non esiste ancora PNG"
                    evidence=[cat.get("source_url") or ""]
                elif cat["source_site"]=="USER_IMAGE":
                    code="BLOCKED_USER_IMAGE_NOT_ATTACHED"
                    reason="Riferimento a immagine personale privo di file nel repository: occorre l'originale dell'utente"
                elif cat.get("source_url") and cat.get("license_status")!="LICENSE_NOT_VERIFIED":
                    code="BLOCKED_SOURCE_NOT_ARCHIVED"
                    reason="Pagina di riferimento nota, ma sorgente originale/asset esatto non archiviato: vietato inventare screenshot"
                    evidence=[cat.get("source_url")]
                else:
                    code="BLOCKED_NO_SOURCE_OR_LICENSE"
                    reason="Né file originale archiviato né URL e diritti verificabili nel catalogo"
            elif original:
                source=ROOT/original
                if not source.is_file():
                    code="BLOCKED_ARCHIVED_SOURCE_MISSING_FROM_REPO"
                    reason="Il percorso del codice originale è registrato ma il file non esiste sul branch"
                elif cid in fail:
                    code="BLOCKED_ACTUAL_TSX_RENDER"
                    reason=str(fail[cid])[:250]
                elif cid in blocked_before:
                    code="BLOCKED_ORIGINAL_SOURCE_GATE"
                    reason=str(blocked_before[cid])[:250]
                elif cid in captured:
                    raise ValueError(cid+": TSX render log claims capture but PNG missing")
                else:
                    code="ARCHIVED_SOURCE_RENDER_NOT_YET_ATTEMPTED"
                    reason="Sorgente originale presente; manca cattura verificata, pipeline di rendering in corso o da completare"
                evidence=[original]
                if cat.get("source_blob_sha"):
                    evidence.append("GIT_BLOB_SHA:"+cat["source_blob_sha"])
            else:
                code="BLOCKED_NO_SOURCE_OR_LICENSE"
                reason="Nessun asset o sorgente verificabile"
        rows.append({
            "uid":linked[cid],"canonical_id":cid,"name":cat.get("name"),
            "provider":cat["source_site"],"result":code,
            "reason":reason,"image_path":file,"image_sha256":digest,
            "original_archive_path":original,
            "source_url":cat.get("source_url"),
            "source_blob_sha":cat.get("source_blob_sha"),
            "license_state":cat.get("license_status"),
            "capture_mode":origin.get("capture_mode") if origin else None,
            "evidence_refs":evidence,
            "consumer_admission":"NOT_VERIFIED",
        })
    assert len(rows)==119 and len({r["canonical_id"] for r in rows})==119
    counts=dict(Counter(r["result"] for r in rows))
    providers=dict(Counter(r["provider"] for r in rows))
    png=sum(x["image_path"] is not None for x in rows)
    report={
        "schema_version":1,"as_of":"2026-11-19","baseline_sha":baseline["source_head_sha"],
        "baseline_missing":119,
        "resolved_to_preview_png":png,
        "still_without_preview_png":119-png,
        "result_counts":counts,"provider_counts":providers,
        "definition_of_resolved":"Captured means only a physical, source-grounded, SHA256-proven PNG. Blocked has a per-UID explicit reason. None are visual-QA or consumer-certified.",
        "cases":rows,
    }
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=[
        "# Esito nominativo delle 119 anteprime — Design-App\n",
        f"Baseline immutabile: 119 UID iniziali; **{png} recuperate**; **{119-png} senza PNG**.\n",
        "La colonna risultato distingue **PNG reale acquisita** da **blocco concreto** e **acquisizione ancora non eseguita**. "
        "Una PNG con QA visivo UNREVIEWED non è né Golden Flutter né asset approvato per l'app.\n",
        "Le fonti originali non sono state sostituite.\n",
        "| UID | Componente | Origine | Esito | Evidenza/impedimento |\n|---|---|---|---|---|\n",
    ]
    for e in rows:
        safe_reason=e["reason"].replace("|","&#124;").replace("\n"," ").replace("<","&lt;")
        lines.append(f"| {e['uid']} | {e['canonical_id']} | {e['provider']} | {e['result']} | {safe_reason} |\n")
    lines.append("\nDettaglio, SHA256, link ai file e fonti: [RECUPERO_119_ESITI.json](./RECUPERO_119_ESITI.json).\n")
    MARKDOWN.write_text("".join(lines),encoding="utf-8")
    print("RECOVERY_LEDGER_119",json.dumps({"png":png,"missing":119-png,"statuses":counts}))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
