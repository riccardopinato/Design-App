# React source preview — residual triage (19 novembre 2026)

## Risultato verificato e confini
- Catalogo: **446/480 PNG registrate** in `ANTEPRIME.json`, **34 UID senza PNG**.
- Baseline congelata: **85/119 UID risolti**, 34/119 con blocco documentato in `RECUPERO_119_ESITI.json`.
- Delle 34 rimanenti: **14 sorgenti React**, **10 demo Flutter non acquisibili**, **10 fonti mancanti/non ammissibili** (dettaglio in `SOURCE_TRIAGE_10.md`).
- Le PNG archiviate con `PINNED_ORIGINAL_TSX_ISOLATED_REACT_RENDER` sono prodotte da sorgenti originali fissati a commit e associati a SHA256. **Visual QA = UNREVIEWED**, non sono certificazioni di fedeltà visiva o di compatibilità Flutter/consumer.
- Per la presente sessione il Master App Factory è stato risolto tramite `App-Factory-Core/CURRENT.yaml` (baseline core `14722698bf92e80c526f5f1f211c8d694ce01fb9`).

## 14 React non recuperati — classificazione a prova di errore

| Gruppo | UID | Evidenza del renderer | Passaggio tecnico necessario |
|---|---|---|---|
| Framer/Amicro (5) | `AMX-002`, `AMX-004`, `DBM-002`, `DBM-011`, `DBM-016` | Runtime `Cannot read properties of null (reading 'useContext')`; problema di dispatcher/hook, origine precisa non ancora certificata | Isolare la dipendenza Framer nello stesso contesto React, ottenere stack completa e verificare tramite browser senza alterare i TSX |
| Ruixen/Radix (6) | `RXN-behavioral-history-select`, `RXN-carousel-3d-select`, `RXN-command-deck`, `RXN-file-tree`, `RXN-package-installer-tabs`, `RXN-ruixen-query-box` | `useMemo`, `useState` o `useContext` con dispatcher null; gli import UI ora provengono dai nove file originali del commit Ruixen | Studiare la doppia risoluzione/bundling React/Radix; test per singolo modulo e firma delle dipendenze |
| Richiede Next.js (1) | `RXN-glowing-send-input` | Import non risolvibile `next/font/google` in Vite isolato | Usare un runtime Next.js autentico con risorse font consentite, non stubbate |
| Resa visiva non affidabile (2) | `RXN-scrub-datetime`, `RXN-video-text` | `NEAR_BLANK_UNVERIFIED_COMPONENT` | Per datetime: screenshot focalizzato che mostri davvero la UI senza confondere uno sfondo artificiale con il componente. Per video: media originale/licenziato e test browser di riproduzione |

## Origine dei nove file ausiliari Ruixen

I nove file di `components/ui/{button,card,context-menu,popover,scroll-area,select,tabs,textarea}.tsx` e `hooks/use-auto-resize-textarea.ts` sono archiviati byte-per-byte in `ruixen_renderer/src/`, insieme alla licenza MIT. La loro provenienza è documentata in `ruixen_renderer/vendor/ruixen/PROVENANCE_PINNED_UI.md`, commit `f6b20860623fa39122ac2b5f0e5bd29a9eb10941`. Le versioni Radix sono bloccate per il runtime di acquisizione, non per le app Flutter.

## Priorità di chiusura

1. Riprodurre e isolare lo stesso errore di dispatcher React in una demo con una sola dipendenza; catturare stack e modulo realmente caricato. Non modificare i componenti originali per superare il gate.
2. Rieseguire le acquisizioni dei 14 UID esclusivamente dopo una modifica motivata, verificando che eseguano i componenti reali e che le PNG passino il filtro anti-blank e SHA.
3. Mantenere i 10 Flutter e i 10 source blockers separati. Non accettare screenshot generici, pagine errate, media di licenza ignota o implementazioni alternative come anteprima ufficiale.
4. Eseguire **Visual QA manuale** delle PNG `UNREVIEWED`; solo dopo riesaminare promozione nel catalogo, compatibilità dei consumer e merito del merge.

## Evidenze machine-readable
- `BIBLIOTECA_COMPONENTI/ANTEPRIME.json`
- `BIBLIOTECA_COMPONENTI/RENDER_ARCHIVED_TSX_BATCH_REPORT.json`
- `BIBLIOTECA_COMPONENTI/RECUPERO_119_ESITI.json` / `.md`
- `BIBLIOTECA_COMPONENTI/SOURCE_TRIAGE_10.md`

**Stato di chiusura:** i 480 UID sono inventariati, non tutti hanno una preview acquisibile; catalogo e provenienza avanzano, ma questa PR **non attribuisce** certificazioni visuali o di produzione a fonti bloccate o solo documentali.
