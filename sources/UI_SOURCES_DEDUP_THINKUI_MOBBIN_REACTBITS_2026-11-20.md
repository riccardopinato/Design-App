# Deduplica 15 risorse design — solo 3 nuove fonti (2026-11-20)

**Origine:** 15 collegamenti condivisi dall'utente dopo la precedente acquisizione Design-App (PR #58 e #59). Richiesta: se una fonte e' duplicata, SALTARLA SENZA RIANALISI. **Esito:** 12 gia' note; 3 nuove: ThinkUI, Mobbin, React Bits. Nessun aggiornamento dei record dei 12 duplicati; mai ricatalogarli con ID alternativi.

**Factory baseline:** `riccardopinato/App-Factory-Core@4df94ac3b3ea22a2323634fe83c3c7770fe3b835` (CURRENT Master 27 / Index 31 / Registry 2). Design-App di base `0c6345fa915e19ab69e0dd50eff8045968a50888`.

## Verifica duplicati: NO REANALYSIS

| # origine | Risorsa | Link canonico interno |
|---:|---|---|
| 1 | Uizze | `DSK-001` |
| 4 | Land-book | `DESIGN-SITE-017` |
| 5 | Godly | `DESIGN-SITE-018 (Recent Design alias)` |
| 6 | 60FPS | `DESIGN-SITE-021` |
| 7 | shadcn/ui | `registry/OSS_DESIGN_SOURCES.yaml — shadcn-ui/ui` |
| 9 | Magic UI | `registry/OSS_DESIGN_SOURCES.yaml — magicuidesign/magicui` |
| 10 | Fontshare | `DESIGN-SITE-022` |
| 11 | Realtime Colors | `DESIGN-SITE-023` |
| 12 | Lucide | `DESIGN-SITE-025` |
| 13 | SVGL | `DESIGN-SITE-026` |
| 14 | Shots | `DESIGN-SITE-027` |
| 15 | Cosmos | `DESIGN-SITE-028` |

In particolare **Uizze** era gia' `DSK-001`; **shadcn-ui/ui** e **magicuidesign/magicui** risultavano gia' nel registro delle fonti OSS; Godly e' alias del `DESIGN-SITE-018`. Nessun nuovo UID/Golden/Donor per queste fonti.

## Tre nuove fonti — audit selettivo

### 2. ThinkUI — DESIGN-SITE-032

**URL:** https://thinkui.xyz/ — MCP remoto: https://thinkui.xyz/mcp

**Verifica:** letti README e `llms.txt` del repository pubblico **`Dionisselami/thinkui@b94cbdfbdd30b872288116e4c2c68a4ed0b70e56`**. La homepage non era disponibile per accesso diretto: i dati sono dichiarazioni del fornitore e non test del server MCP autenticato. Il repository contiene documentazione/distribuzione del servizio, **non** il codice del server (proprietario).

**Dati del provider:** 1.483 screenshot (solo **417** indicati permissivi, 1.066 a uso studio); 3.802 elementi HTML/CSS MIT; 1.698 SVG animati MIT; 1.639 riferimenti testuali e 118 materiali. Sono conteggi dichiarati in `llms.txt`, non risultati di chiamate `corpus_stats` eseguite da noi. Licenze per singolo risultato sempre da leggere, font incluso.

**5 tool documentati:** `find_ui_references`, `find_ui_elements`, `find_animated_icons`, `find_ui_materials`, `corpus_stats`. Accesso con OAuth o API key secondo README; `llms.txt` non elenca OAuth (documentazione divergente): non configurare client automaticamente. **Prezzi dichiarati USD:** Starter $9.99/mese, Pro $19.99/mese, Lifetime $190; nessun piano gratuito confermato. **Nessun acquisto o connessione effettuata.**

**Valore App Factory:** source attribution in ogni ricerca, studio di flussi completi, risultati `NO_MATCH` invece di componenti inventati, licenze collegate. Possibile *reference/review provider* nel Fast Track Design, non un servizio obbligatorio per il Master. **Gate:** privacy, canone, licenze, consenso utente e compatibilita' di Chat/MCP prima di usare in un progetto.

### 3. Mobbin — DESIGN-SITE-033

**URL:** https://mobbin.com/ — [prezzi ufficiali](https://mobbin.com/pricing) — [termini ufficiali](https://mobbin.com/terms) (in vigore dal 16/05/2026).

**Verifica:** Mobbin e' un archivio di screenshot e flussi di app commerciali reali, con ricerca per flow/screen e sezioni web. Piano Free limitato: app e siti limitati, **nessuna** ricerca, flow, animazione o MCP; max 3 collection. Piano Pro ufficiale mostrato in EUR **€10 al mese con fatturazione annuale**; contiene flows, animation, AI credits, MCP. Il piano Team e' separato.

**Restrizioni concrete:** termini §3.2 vietano archiviare/mirrors/re-hostare contenuti senza autorizzazione e §3.4 proibisce alcuni usi dei materiali con IA per derivati o addestramento, salvo permessi. API/MCP non autorizzano realizzare una raccolta autonoma concorrente. **Quindi Design-App salva solo URL e annotazioni sintetiche originali**, mai le schermate ricavate da Mobbin o copie automatiche. No scraping, no MCP/abbonamento avviati.

**Valore:** guardare **sequenze** di schermate reali (onboarding, preview media, conferme distruttive, pagamenti e privacy), ricostruendo un flusso prodotto coerente con UI nativa originale e senza duplicare l'identita' altrui.

### 8. React Bits — DESIGN-SITE-034

**URL:** https://reactbits.dev/ — repository https://github.com/DavidHDev/react-bits — commit verificato `701a8acc34f718b305d1ff0cc7d4700df0e1f1c9`.

**Verifica:** README ufficiale cita **215+ componenti/background animati gratuiti** divisi in 5 macro-famiglie: 33 Text Animations, 38 Animations, 48 Components, 34 Micro, 63 Backgrounds (conteggio variabile). Esempi in JS/TS + CSS/Tailwind. **React Bits Pro** e' un prodotto distinto a pagamento. L'uso Web necessita auditing delle dipendenze GSAP/Motion/three/OGL e dell'impatto prestazionale.

**Licenza:** file `LICENSE.md` letto direttamente, **MIT + Commons Clause**, non MIT puro e non una licenza open source senza restrizioni. Consente l'utilizzo in applicazioni/siti/prodotti commerciali, ma vieta vendita, sublicenza o redistribuzione dei **componenti stessi**, da soli, in bundle o versione portata. Anche tools/sounds/exports hanno vincoli specifici. **Non archiviare TSX originali in una biblioteca pubblica redistribuibile come Design-App**; usare riferimenti e valutare integrazione puntuale rispettando termini e attribution. Un port Flutter originale non e' tecnicamente un copia-incolla e va valutato anche sotto il profilo delle restrizioni della licenza.

**Pattern approvati per shortlist:** motion funzionale di cards, nav, accordion, testo e tooltip; microinterazioni brevi, con reduced-motion e test FPS. **Pattern da NON importare automaticamente:** background shader continui, particelle/pesanti scene 3D o effetti che aumentano consumo batteria e peso APK; nessuna adozione consumer.

## Priorita' cross-app

1. **Mobbin** per confronti di UX e sequenze reali; uso manuale/di ricerca nei limiti del piano e dei diritti.
2. **React Bits** per microinterazioni Web mirate, facendo prevalere i sorgenti gia' approvati/Design-App e la coerenza estetica dell'app.
3. **ThinkUI** per reference assistite da agente con provenienza, solo se valore concreto giustifica abbonamento e accesso al provider.

## Stato finale dell'intake

- 15 URL in input, **12 SKIPPED_ALREADY_CATALOGUED**, **3 NEW_REFERENCE**.
- 12 app con 22 associazioni `PROPOSED_ONLY`, no consumer source modified.
- 0 font, screenshot, SVG, TSX, source code, credenziali o pacchetti importati.
- Nessuna attivazione di provider cloud/AI, nessun Golden o Product Bible modificato.
- **Validation scope:** formato JSON, URL/ID unici, integrazione PER_APP e CI del repo; nessun test Flutter/Web consumer eseguito.

## Fonti ufficiali

- https://github.com/Dionisselami/thinkui/blob/b94cbdfbdd30b872288116e4c2c68a4ed0b70e56/README.md
- https://github.com/Dionisselami/thinkui/blob/b94cbdfbdd30b872288116e4c2c68a4ed0b70e56/llms.txt
- https://mobbin.com/pricing · https://mobbin.com/terms
- https://github.com/DavidHDev/react-bits/blob/701a8acc34f718b305d1ff0cc7d4700df0e1f1c9/README.md
- https://github.com/DavidHDev/react-bits/blob/701a8acc34f718b305d1ff0cc7d4700df0e1f1c9/LICENSE.md
