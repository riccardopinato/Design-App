# BIBLIOTECA COMPONENTI — App Factory

**Data iniziale: 19/11/2026.** Biblioteca operativa dentro Design-App; non e' un nuovo repository, un nuovo Golden o un secondo Product Bible.

## Cosa contiene

- **CATALOGO.json**: indice canonico consultabile di 478 componenti, deduplicazione con 4 alias storici, collegamenti ad app e fonti, linguaggio, stato e percorso del codice.
- **INDICE.md**: panoramica per famiglie e sorgenti.
- **sorgenti/ruixen/**: 277 file **originali** TSX/React acquisiti da `ruixenui/ruixen.com@f6b20860623fa39122ac2b5f0e5bd29a9eb10941`, verificati contro SHA Git dei 277 file, con `LICENSE.md` MIT e `PROVENIENZA.json`. Non sono widget Flutter.
- **Uiverse**: 111 file originali HTML/CSS gia' conservati in `UI-UX/UIVERSE/CODICE_SORGENTE/`; il catalogo vi punta, senza salvarne copie. Due varianti con identico blob sono rappresentate da un ID e alias.
- **Altre fonti**: Flutter Component Library, Flutter Gems, Forui, DevLibraries, Watermelon, Amicro, Gentleface, ecc. I portali senza codice originale recuperato restano `REFERENCE_ONLY`, per evitare di spacciarli per pacchetti pronti.

## Ricerca locale

```bash
python BIBLIOTECA_COMPONENTI/cerca.py --testo button
python BIBLIOTECA_COMPONENTI/cerca.py --app annas-diary
python BIBLIOTECA_COMPONENTI/cerca.py --fonte RUIXEN --solo-sorgente --limite 5
python BIBLIOTECA_COMPONENTI/cerca.py --linguaggio flutter --formato json
python BIBLIOTECA_COMPONENTI/cerca.py --id UIV-107
python BIBLIOTECA_COMPONENTI/validate.py
```

## Status: cosa significa

| Stato | Significato |
|---|---|
| ARCHIVED_SOURCE | Codice originale recuperato e presente nel repo; NON implica compatibilita' Flutter, dipendenze risolte o test runtime. |
| REFERENCE_ONLY | Solo metadati/link o demo; non esiste un codice originale vendorizzato nel catalogo. |
| COPY_READY | **Nessuna nuova voce** raggiunge automaticamente questa maturita'; serve validazione della versione adattata. |

## Processo di adozione

1. Leggere Product Bible e stile approvato dell'app; preferire reference selezionate dall'utente e verificare Golden/donor interni.
2. Cercare il componente nel catalogo, identificare origine, file, lingua, license e dipendenze.
3. Per sorgenti React, CSS o TSX realizzare un adapter o una reimplementazione Flutter/Compose idonea; non rinominare `.tsx` in `.dart`.
4. Controllare caso per caso licenza originaria e asset esterni: codice pubblicamente visibile non autorizza sempre redistribuzione. Materiale senza diritti dimostrati resta linkato, non copiato.
5. Svolgere build, analisi semantica/accessibilita', responsive, reduced-motion, screenshot before/after e QA su target reale. Soltanto dopo classificare una versione adattata come LIBRARY_VERIFIED/COPY_READY e, se giustificato, candidarla ai Golden di Core.
6. Aggiornare il catalogo quando si importano nuovi componenti, evitando duplicati per ID, URL/commit/path o sorgente identico; conservare gli alias di vecchi registri.

## Confini

- Nessun package installato in app consumer; nessuna modifica alle app.
- Gli originali Ruixen sono TSX/React con possibili dipendenze e asset esterni non verificati; conservare MIT e attribution quando riutilizzati. L'origine Uiverse ha un archivio con proprio registro licenze.
- Le 15 schede Flutter Component Library censite non espongono attualmente, nell'audit svolto, file Dart originali e licenza verificabile: pertanto non sono state copiate.
- Il catalogo e' un indice leggero: non contiene una seconda copia dei file Uiverse e non incorpora download inutili di asset dimostrativi.

**Principio:** archiviare originali quando accessibili e legittimamente riutilizzabili, catalogare ogni fonte utile, certificare solo l'adattamento effettivamente testato.
