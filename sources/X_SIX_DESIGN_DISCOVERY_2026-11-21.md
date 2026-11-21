# Lotto di 6 post X — intake DISCOVERY in attesa di ispezione (21 novembre 2026)

**Origine:** sei URL condivisi dall'utente dopo i precedenti intake di fonti Design-App. **Factory baseline** `4df94ac3b3ea22a2323634fe83c3c7770fe3b835`; **Design-App main preflight** `b083c626abb399c16930c38587270cc4617bb786`.

## Verifica effettiva

- Tentato l'accesso diretto alle sei pagine X: contenuto e media non resi accessibili dai fetcher.
- Tentata ricerca web dei sei ID esatti: nessuna trascrizione attendibile recuperata.
- Tentati mirror e servizi per embed: nessun testo o media effettivo del post recuperato.
- Ricerca dei sei ID nel repository Design-App: nessuna occorrenza individuata nell'indice principale (non è prova assoluta di assenza altrove).
- Da URL si conoscono solo `url_handle` e `post_id`; **non** il contenuto, la tipologia tecnica, gli asset, la licenza o i link esterni.
- Per questa ragione **non si deduce alcuno stile dal nome degli account** e non si inventano app-mapping, UID, anteprime o nuove sorgenti OSS.

| ID intake | Link originale | Stato |
|---|---|---|
| `XDISC-20261121-01` | [0xaditin / 2123469621449850890](https://x.com/0xaditin/status/2123469621449850890) | DISCOVERY · CONTENT_UNVERIFIED |
| `XDISC-20261121-02` | [ianneo_ai / 2123243488645206322](https://x.com/ianneo_ai/status/2123243488645206322) | DISCOVERY · CONTENT_UNVERIFIED |
| `XDISC-20261121-03` | [Jakubantalik / 2122738787667349562](https://x.com/Jakubantalik/status/2122738787667349562) | DISCOVERY · CONTENT_UNVERIFIED |
| `XDISC-20261121-04` | [elbeyoglu / 2123328186901836077](https://x.com/elbeyoglu/status/2123328186901836077) | DISCOVERY · CONTENT_UNVERIFIED |
| `XDISC-20261121-05` | [amananimates / 2123291753264656823](https://x.com/amananimates/status/2123291753264656823) | DISCOVERY · CONTENT_UNVERIFIED |
| `XDISC-20261121-06` | [BenjaminUIX / 2123340929633550834](https://x.com/BenjaminUIX/status/2123340929633550834) | DISCOVERY · CONTENT_UNVERIFIED |

## Regole di recupero

1. Ottenere copia del testo e degli allegati **di ciascun post esatto** (es. screenshot/screen recording dell'utente o accesso pubblico ripristinato), inclusi eventuali thread e URL di origine.
2. Identificare il contenuto effettivo (app mockup, motion, font, component code, pattern UI, workflow, tool) e le demo o repository reali.
3. Verificare provenienza, eventuale repository e commit, licenza specifica di codice/media e compatibilità Flutter, Compose, Web.
4. Deduplicare rispetto a `sources/DESIGN_RESEARCH_SITES.json`, `registry/OSS_DESIGN_SOURCES.yaml`, `BIBLIOTECA_COMPONENTI` e mappa per app.
5. Soltanto dopo: eventuali screenshot/preview autorizzate, classificazione `REFERENCE` o superiore, possibili proposte app. Nessun codice consumer senza gate Product Bible/QA.

**Stato:** sei link archiviati nel [manifest JSON](./X_SIX_DESIGN_DISCOVERY_2026-11-21.json), zero design identificati, zero licenze verificate, zero nuove source canoniche, zero app modificate. Questa è conservazione del riferimento **non** un audit stilistico completato.
