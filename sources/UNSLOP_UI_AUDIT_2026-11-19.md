# Unslop UI — acquisizione e adozione anti-AI (19 novembre 2026)

**ID nuova fonte:** DSK-011. **Fonte:** [felipebasurto/unslop-ui](https://github.com/felipebasurto/unslop-ui/tree/cd891160453f26aaacc569bad96a8d10d595076d) @ `cd891160453f26aaacc569bad96a8d10d595076d`. **Licenza:** MIT (copia e attribuzione inclusa). **Maturità:** SOURCE_ARCHIVED / REFERENCE, NON COPY_READY. **Factory baseline:** App-Factory-Core `14722698bf92e80c526f5f1f211c8d694ce01fb9` (Master v27; Golden Index v29).

## Scopo

Capability di revisione *sottrattiva*: elimina copy, chrome e ornamenti superflui. L'upstream definisce U1–U16 su copy/badge/status/chart e U17–U20 come `--surface` opzionale. Lo script originale conta candidati con regex nei sorgenti Web/markup/JSON/prose, non scannerizza Dart o Kotlin; diverse regole richiedono osservazione umana e contesto. Nessun automatico "rimuovi tutto": evidenza del dato vero, UX distruttiva, a11y, funzioni e stile scelto prevalgono.

## Complementarità e deduplicazione

- DSK-001 Uizze = direzione estetica, prodotti e anti-template generale.
- DSK-002 Impeccable = processo completo critique/audit/harden/polish e QA visivo.
- DSK-011 Unslop UI = diagnosi microcopy/ornamenti in forma ripetibile. Non è un secondo design system, né un set di nuovi 20 divieti assoluti.
- Canonical rubric: [64 segnali AT-01…AT-64](https://github.com/riccardopinato/App-Factory-Core/blob/main/contracts/PROFESSIONAL_PRODUCT_DESIGN_ANTI_AI_STOCK_v1.md). Mapping U→AT in `contracts/UNSLOP_UI_ANTI_AI_64_BRIDGE_v1.md` sul Core.

## Intake OSS

La fonte è archiviata in [sources/oss/unslop-ui](./oss/unslop-ui/README.md), con sorgenti originali, LICENSE, test upstream e SHA. Non duplicare in `BIBLIOTECA_COMPONENTI/CATALOGO.json`: questa è una **capability di QA**, non un componente UI visuale e non deve consumare un UID.

## App consumer candidate

| Consumer | Design-App prima | Focus | Confine |
|---|---|---|---|
| Anna's Diary | Organic iOS Journal; Lora/Manrope, Rose/HSV, Classic | ripetizioni, sottotitoli, badge, decorative section labels, densità | non toccare Cassaforte, sync, dati o estetica approvata |
| Android Omni Cleaner | UI e mock-up già approvati; PR design corrente | eyebrow, subtitles, status pill, grafici, hero gradient | Kotlin/Compose; solo review e piccole modifiche non distruttive, RC1 freeze |
| World Days | priorità editoriale e leggibilità | testi didascalici, stati di contenuto veritieri | non modificare storie/traduzioni nel QA visivo |
| Notes-Ecosistema | document-first design | icone/chrome inutili | non modificare canvas/persistenza |
| Cooking Anime | identità originale, ricette | frasi generiche e badge non supportati | non cambiare ricette senza revisione |

## Protocollo operativo

1. Read-only scan (upstream Web, adapter AppLab Flutter/Compose) su SHA esatto. Il numero di finding non è punteggio di qualità.
2. Classificare ciascuno `KEEP_PURPOSEFUL | ADAPT | REMOVE_CANDIDATE | NEEDS_RUNTIME_EVIDENCE`. Mai sopprimere label accessibili o messaggi di errore/ripristino.
3. Modifiche mirate solo dopo confronto con riferimento Design-App e Product Bible; localizzazioni in file canonici.
4. Test sorgente → PR CI exact-head → screenshot reali prima/dopo su stato e fixture identici → review → fisico se pertinente. Senza immagini: VISUAL_NOT_VERIFIED.
5. Registrare esiti per ciascuna app e falsi positivi, tenere la Golden come CANDIDATE fino a validazione indipendente di almeno due consumer.

**Stato di questo intake:** raccolta sorgenti e definizione del protocollo. Non prova ancora consumer implementati/merge o test native.
