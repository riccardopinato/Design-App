# Deskland Android — Dossier Design-App

**Registro permanente:** `PER_APP/deskland-android.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Launcher Android interattivo con accenti desktop/spatial 3D; gesti e leggibilità prime, effetti visivi dopo stabilità.

**Categorie da studiare:** desktop · launcher · batteria/widget · meteo se reale.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. icone app nella home launcher.
2. drag/drop e selezione tile.
3. controlli player/effetti dove realmente presenti.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-003 · battery-charging](https://gentleface.com/icons/battery-charging) | MEDIUM | widget stato batteria reale | VERIFIED_DETAIL |
| [ICO-020 · play](https://gentleface.com/icons/play) | MEDIUM | avvio animazione o elemento interattivo | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | MEDIUM | pausa effetti quando previsto | VERIFIED_SITE |
| [ICO-026 · home](https://gentleface.com/icons/home) | MEDIUM | launcher home senza costi animazioni | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `home`, `play`, `battery-charging`.

## Animazioni e feedback proposti

- risposta drag a 60 fps e rilascio leggibile.
- transizione selezione/long-press sobria.

## Cosa evitare

- animazioni continue che rallentano il launcher.
- finti indicatori batteria o meteo.
- effetti sofisticati prima di eliminare i glitch.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-002 — Impeccable | MEDIUM | launcher accessibility and touch-state review |
| DSK-004 — Emil Design Engineering | HIGH | long-press drag, icon motion and frame pacing |
| DSK-009 — UI UX Pro Max | HIGH | launcher spatial controls, only after functional stability |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.

## Voice Orb — proposta futura (MEDIUM)

**Origine:** [DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) → [beUI Voice Orb](https://beui.dev/components/agents/voice-orb) · [Audit sorgente](../sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md) · [Mappa molti-a-molti](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md).

- **Idea:** Overlay per futuro agente o note vocali solo se previsti.
- **Collocazione candidata:** Pannello vocale separato dal launcher.
- **Adattamento estetico:** effetto launcher leggero.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (MEDIUM)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Launcher side panel after stabilization. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-002 · [Cursor Trail](https://devlibraries.com/libraries/amicro/cursor-trail) (MEDIUM):** Only with proven mouse/trackpad connected, avoid launcher CPU impact. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (HIGH):** Enter a launcher room/panel only after launcher stabilizes. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** First launcher data loading only, never on every home action. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-004 · App Icon Load (HIGH)** — Avvio launcher con inizializzazione effettiva. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/app-icon-load.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-009 · Terminal Loader (MEDIUM)** — Diagnostica developer opzionale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/terminal-loader.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-012 · Grid Dots (MEDIUM)** — Preparazione pannello app. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/grid-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-017 · Concentric Ring (MEDIUM)** — Caricamento pannello widget. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/concentric-ring.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-020 · Concentric Squares (MEDIUM)** — Caricamento launcher con modalità risparmio movimento. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/concentric-squares.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-029 · Particle Shape Morph (MEDIUM)** — Effetto visivo accessorio dopo stabilità launcher. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.
- **DBM-030 · Infinite Spiral (MEDIUM)** — Esperimento visuale dopo collaudo FPS. Evidenza: `USER_SCREENSHOT_ONLY`; sorgente esatto da identificare. Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** lo stato di caricamento deve corrispondere a una vera operazione; se esiste avanzamento misurabile usare progress bar/tempo affidabile; timeout/error/retry, a11y, reduced motion, stop fuori viewport e consumo energetico. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi, ordine e hash sono nel JSON canonico. Per software Flutter/Compose il codice React è solo riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 7 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P2**, modalità `OPERATE+EXPERIENCE`, fit MEDIUM. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Launcher, scene e overlay.
- **Miglioramento proposto:** Conservare l'impatto immersivo senza perdere usabilità del launcher o performance Android; motion solo quando utile.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] FPS e rendering scenico misurati su device
  - [ ] Overlay e controlli accessibili, nessun bottone fuori schermo
  - [ ] Animazioni sospese in background/riduzione movimento
  - [ ] Home avviabile anche quando asset dinamici non caricano

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.
