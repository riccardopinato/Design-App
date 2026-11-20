# Anna's Diary — Dossier Design-App

**Anteprime dei componenti:** [tabella con miniature, ID, fonte e stato](../BIBLIOTECA_COMPONENTI/PER_APP/annas-diary.md). Le immagini mancanti sono indicate esplicitamente.


**Registro permanente:** `PER_APP/annas-diary.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Rettifica link 19/11/2026:** le quattro reference prioritarie `UIR-0003/0014/0021/0029` restano preferenze dell'utente ma i JPG del 12/11 **non erano pubblicati**. Consultare [dossier di provenienza e link funzionanti](ANNAS_DIARY_MISSING_UIR_20261119.md); non inferire che i JPG UIR-0051/52/76 siano sostituti 1:1. Questa rettifica non cambia il design approvato né l'uso di Design-App come prima fonte di ispirazione.

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Diario iOS contemporaneo con rosa tenue, tipografia Manrope/Lora e ritmo editoriale approvato; non cambiare l'identità senza nuova decisione.

**Categorie da studiare:** diario e ricordi · calendario · affetti e condivisione · privacy.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. calendario Mese/Settimana/Oggi.
2. schede Ricordi e inserimento eventi.
3. successo salvataggio evento.
4. Vault e contenuti protetti.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-001 · bell-ring](https://gentleface.com/icons/bell-ring) | HIGH | promemoria confermato | VERIFIED_SITE |
| [ICO-002 · calendar](https://gentleface.com/icons/calendar) | HIGH | apertura calendario e selezione data | VERIFIED_SITE |
| [ICO-007 · import](https://gentleface.com/icons/import) | MEDIUM | recupero backup dove implementato | VERIFIED_DETAIL |
| [ICO-008 · images](https://gentleface.com/icons/images) | HIGH | ricordi e media | VERIFIED_DETAIL |
| [ICO-010 · bookmark](https://gentleface.com/icons/bookmark) | MEDIUM | ricordi in evidenza | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | salvataggio evento riuscito | VERIFIED_SITE |
| [ICO-017 · cloud](https://gentleface.com/icons/cloud) | HIGH | sincronizzazione reale con ricevuta | VERIFIED_SITE |
| [ICO-023 · eye](https://gentleface.com/icons/eye) | HIGH | visibilità campi privati senza mostrare dati per errore | VERIFIED_SITE |
| [ICO-024 · archive](https://gentleface.com/icons/archive) | MEDIUM | ricordi archiviati se supportati | VERIFIED_SITE |
| [ICO-025 · messages](https://gentleface.com/icons/messages) | MEDIUM | spazio condiviso solo per feature reale | VERIFIED_DETAIL |
| [ICO-026 · home](https://gentleface.com/icons/home) | MEDIUM | torna alla schermata Oggi | VERIFIED_SITE |
| [ICO-028 · lock](https://gentleface.com/icons/lock) | HIGH | Vault blocco/sblocco realmente completato | ANIMATION_UNVERIFIED |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `calendar`, `check`, `lock`.

## Animazioni e feedback proposti

- micro-feedback di salvataggio verificato.
- transizione di selezione giorno contenuta.
- blocco Vault solo dopo esito reale.

## Cosa evitare

- icone kawaii indiscriminate nel diario maturo.
- animazione del cloud senza ricevuta sync.
- modificare picker HSV o palette concordata.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | iOS Journal and pastel identity quality checks |
| DSK-002 — Impeccable | HIGH | reduce card overload while preserving diary identity |
| DSK-003 — Taste Skill | MEDIUM | PWA marketing entry, not diary calendar UI |
| DSK-004 — Emil Design Engineering | HIGH | calendar gestures, Capture sheet and memory transitions |
| DSK-005 — Vercel Web Design Guidelines | HIGH | PWA accessibility and layout; native separately |
| DSK-006 — Anthropic Frontend Design | HIGH | coherent editorial diary personality |
| DSK-007 — Hallmark | MEDIUM | marketing site and app feature pages |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | readable diary and navigation review |
| DSK-009 — UI UX Pro Max | HIGH | rose editorial token system and calendar polish |
| DSK-010 — Stageshow | HIGH | feature showcase and app-store creative |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.

## Voice Orb — proposta futura (HIGH)

**Origine:** [DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) → [beUI Voice Orb](https://beui.dev/components/agents/voice-orb) · [Audit sorgente](../sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md) · [Mappa molti-a-molti](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md).

- **Idea:** Ricordi e diario con eventuali note vocali.
- **Collocazione candidata:** Editor Ricordi o acquisizione evento.
- **Adattamento estetico:** rosa, Manrope/Lora approvati.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-002 · Card Stack Peel (HIGH)** — Transizioni fra card, album e raccolte in una stessa schermata; stato e back invariati. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (HIGH)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Reveal special memory cover only. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-003 · [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) (MEDIUM):** Memory card reveal without hiding data. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (HIGH):** Memories and month/annual recap editorial cards. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (MEDIUM):** Optional memories section, not Vault security transition. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** Real sync progress with reconciliation states. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Questa sezione contiene **proposte**; nessuna libreria installata, nessuna feature consumer confermata dal solo catalogo.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (HIGH)** — Swipe raccolta Ricordi, apri foto originale, non sostituire navigazione calendario. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-002 · [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) (HIGH)** — Selezione giorno in un mese già fissato o rotella valori nelle Impostazioni, data completa deve restare accessibile. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-003 · [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) (MEDIUM)** — Scorrimento anno/mese di Ricordi solo se utile e non sostituisce calendario. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (HIGH)** — Filtra Ricordi per intervallo date o definisci fascia oraria appuntamento solo dopo definizione UX. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-005 · [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) (MEDIUM)** — Accesso/account opzionale solo dove previsto, mai obbligare login per diario locale. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-006 · [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) (MEDIUM)** — Titoli editoriali secondari mantenendo palette rose/Manrope/Lora. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-007 · [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) (HIGH)** — Invita persona/spazio condiviso con codice se già previsto; conferma server reale, nessun invito simulato. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (HIGH)** — Home Oggi — riepilogo impegni del giorno in alto, prima apertura giornaliera e/o orario scelto, deduplicato per data/account. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-009 · [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) (MEDIUM)** — Conto alla rovescia a un evento importante scelto, non rendere ogni appuntamento un timer. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.


### Proposta prioritaria — riepilogo «I tuoi impegni di oggi»

**Origine diretta: richiesta dell'utente 17/11/2026.** All'inizio della Home **Oggi**, piccolo riquadro editoriale con impegni del giorno ordinati per orario, ciascuno apribile. Trigger **prima apertura del giorno** oppure **orario prestabilito configurato**: sono due modalità alternative o combinabili solo dopo scelta prodotto, senza assumere funzionalità già operative. Non sovrascrive la pagina Oggi, la palette rose, Manrope/Lora o la navigazione esistente.

- **Prima apertura:** banner riepilogativo in-app, al massimo una comparsa non richiesta per profilo/data locale; l'utente può ritrovare gli impegni nella sezione anche dopo la chiusura del banner.
- **Orario configurato:** il riquadro può aggiornarsi quando l'app è aperta, ma **non è una notifica di sistema**. Un avviso quando l'app è chiusa richiede un'ulteriore feature con consenso e scheduling nativo Android/iOS.
- **Dati e privacy:** utilizzare esclusivamente eventi del calendario reale, gestire appuntamenti condivisi, account switch, sincronizzazione, modifiche, eventi cancellati, offline/errore e privacy su lockscreen; evitare duplicati quando si cambia scheda o si ritorna in Home.
- **Tempo:** rispettare fuso del dispositivo, cambio giorno, ora legale, quiet hours e preferenze esplicite. Se non ci sono impegni, mostrare uno stato sobrio, non una notifica falsa.
- **Interazione:** raggiungere il dettaglio evento esistente, conservare accessibilità, swipe/tap, font scale e reduced motion. La UI può usare l'idea di Notification List, ma la sua implementazione sorgente esatta **non è stata trovata** nel repo Watermelon.

### Proposta Ricordi — Carousel Slider

Carosello con swipe fra ricordi/immagini; immagini nel loro **formato originale senza ritagli forzati**, fullscreen al tap, indicatori e azioni precedente/successivo accessibili. Riutilizzare la navigazione esistente del diario. **Non cambiare la vista Calendario in una ruota numerica:** Fractional Picker è solo un suggerimento alternativo per scegliere un giorno all'interno del mese valido o un valore nelle Impostazioni, senza sacrificare il date-picker standard.

### Form e condivisione

Dialog Stack può rendere più chiaro **il flusso di invito allo spazio condiviso a codice**; il demo non crea inviti né gestisce utenti. Swap Form è solo una transizione di interfaccia, non motivo per introdurre login obbligatorio o toccare il Google login opzionale.

**Nota tecnica:** nessuna di queste proposte autorizza modifiche a backend, permessi push, eventi o cronologia dell'app. Verificare HEAD e Product Bible prima dello sviluppo.

**Gate comune:** rispettare Product Bible, accessibilità, controlli di input alternativi, riduzione movimento, performance, colore e lingua; Flutter/Compose richiedono adattamento nativo dei componenti React. I riferimenti `Text Gradient`, `Notification List` e `Flip Clock` non hanno un file componente esatto verificato alla baseline e restano `REFERENCE`.

**Storico 17/11/2026:** proposte inserite in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, con provenienza e stato `PROPOSED_ONLY`.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-002 · Classic Spinner (MEDIUM)** — Sync visibile solo se reale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/classic-spinner.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-003 · Pulsating Dots (HIGH)** — Piccolo feedback non intrusivo per sincronizzazione. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/pulsating-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-005 · Face Id Scan (HIGH)** — Sblocco Vault dopo risposta biometrica reale. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/face-id-scan.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-007 · Apple Breathe (HIGH)** — Feedback delicato nella Home Ricordi solo durante attesa vera. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/apple-breathe.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-008 · Fade Arc (HIGH)** — Attesa breve con palette rose. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/fade-arc.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-010 · Apple Pulse Dots (HIGH)** — Attesa contenuti Ricordi. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/apple-pulse-dots.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-015 · Intersecting Rings (HIGH)** — Sync eventi e Ricordi. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/intersecting-rings.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-016 · Skeleton (HIGH)** — Sezione Ricordi quando serve davvero il caricamento. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/skeleton.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-018 · Range Selection Slider (MEDIUM)** — Selezione intervallo per Ricordi o calendario se realmente supportata. Evidenza: `SOURCE_FILE_PREVIOUSLY_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/range-selection-slider/base.tsx); già censito: `WML-004`. Stato: `PROPOSED_ONLY`.
- **DBM-021 · Notification List (HIGH)** — Home Oggi elenco impegni reali alla prima apertura del giorno o orario configurato. Evidenza: `EXACT_SOURCE_NOT_LOCATED`; sorgente esatto da identificare; già censito: `WML-008`. Stato: `PROPOSED_ONLY`.
- **DBM-024 · View On Map (MEDIUM)** — Luogo appuntamento opzionale e con privacy. Evidenza: `SOURCE_FILE_READ`; [file originale](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/view-on-map/base.tsx). Stato: `PROPOSED_ONLY`.
- **DBM-025 · Bouncing Lines (MEDIUM)** — Attesa breve dopo salvataggio. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/bouncing-lines.tsx). Stato: `PROPOSED_ONLY`.

**Home Oggi:** lo screenshot mostra visivamente `Notification List`, ma **il codice esatto non risulta individuato**. Resta valida la proposta già registrata: riepilogo degli impegni reali in alto alla **prima apertura del giorno oppure a un orario configurabile**, con deduplica, gestione sync/account e possibilità di vedere il dettaglio evento. Non è una notifica push né una feature già implementata.

**Ricordi:** il carousel già censito conserva il proprio ruolo; i loader e lo Skeleton si usano soltanto quando il contenuto è realmente in attesa, senza animazioni decorative perpetue.

**Controlli obbligatori:** lo stato di caricamento deve corrispondere a una vera operazione; se esiste avanzamento misurabile usare progress bar/tempo affidabile; timeout/error/retry, a11y, reduced motion, stop fuori viewport e consumo energetico. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi, ordine e hash sono nel JSON canonico. Per software Flutter/Compose il codice React è solo riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 12 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Impeccable — metodologia Designing (17/11/2026)

**Fonte ufficiale:** [Designing with Impeccable](https://impeccable.style/designing/) · [Audit incrementale](../sources/IMPECCABLE_DESIGNING_GUIDE_AUDIT_2026-11-17.md) · riferimento già catalogato `DSK-002` (non creare un nuovo OSS source). **Priorità proposta P1**, modalità `OPERATE+EXPERIENCE`, fit HIGH. Nessun intervento nell'app eseguito.

- **Schermate interessate:** Oggi, Calendario, Ricordi, Impostazioni.
- **Miglioramento proposto:** Ridurre l'affollamento di card senza perdere gli appuntamenti; mantenere palette rose, Manrope/Lora e navigazione aderente; dare priorità agli impegni giornalieri e agli stati di sincronizzazione.
- **Verifiche da eseguire quando autorizzato:**
  - [ ] Oggi: primo contenuto significativo visibile e impegno raggiungibile senza scorciatoie simulate
  - [ ] Calendario: 31 giorni/indicatori e font grande senza overflow, evento apribile
  - [ ] Ricordi: galleria a proporzioni originali, testo lungo e fallback immagini
  - [ ] Shared: offline/retry/account switch senza falsi stati di salvataggio

**Pipeline futura:** brief e decisioni Product Bible → verifica screenshot e gerarchia `critique` → controllo funzionale/semantico `audit` → stati di errore e vuoto `harden` → rifinitura `polish` → aggiornamento token e decisioni visive. Impeccable CLI/hook sono **Web-only**, non un passaggio di build o QA Flutter. Conservare colori, font, navigazione e caratteristiche già approvate; matrice responsive e App Shell Golden DRAFT si applicano senza dichiararne la certificazione.

**Storico:** aggiunta una checklist di design nel campo `impeccable_designing_quality` del registro per-app; stato `PROPOSED_ONLY` / `NOT_EXECUTED`.

## Dribbble + Collect UI — proposte 2026/27 (18/11/2026)

- **Pattern:** DCL-001, DCL-002, DCL-004, DCL-006, DCL-007, DCL-011.
- **Schermate:** Oggi, Calendario, Ricordi.
- **Vincolo:** Preservare Manrope/Lora, palette rose, look diario contemporaneo.
- **Fonti:** [Audit sorgenti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) · [Matrice pattern/app](../UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.md).
- **Stato:** `PROPOSED_ONLY`, non implementato né testato in questa attività. La Product Bible e le scelte di design pregresse prevalgono. Nessun asset di terzi copiato.

## Uiverse — proposte 18/11/2026

- **UIV-002 — [xueyuantan/rotten-pig-19](https://uiverse.io/xueyuantan/rotten-pig-19)**: CTA con gradiente e stato focus/tap (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-002_original.html).
- **UIV-004 — [JohnnyCSilva/jolly-elephant-67](https://uiverse.io/JohnnyCSilva/jolly-elephant-67)**: Schede editoriali e viaggi (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html).
- **UIV-005 — [amir_6539/red-duck-82](https://uiverse.io/amir_6539/red-duck-82)**: Sfondo decorativo valutabile solo dopo lettura del codice (HIGH). Originale da estrarre.
- **UIV-006 — [JustCode14/red-dingo-61](https://uiverse.io/JustCode14/red-dingo-61)**: Toggle semantico legato a impostazione reale (MEDIUM). Originale da estrarre.
- **UIV-007 — [arthur_6104/orange-walrus-50](https://uiverse.io/arthur_6104/orange-walrus-50)**: Stato attesa job reale; frase personalizzata quando appropriata (MEDIUM). Originale da estrarre.
- **UIV-009 — [eslam-hany/selfish-bobcat-73](https://uiverse.io/eslam-hany/selfish-bobcat-73)**: Card libro apribile con tap; note/ricordi e raccolte (HIGH). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**31 preferiti proposti per annas-diary**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-004](https://uiverse.io/JohnnyCSilva/jolly-elephant-67) | CARD | Schede editoriali e viaggi | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html) |
| [UIV-005](https://uiverse.io/amir_6539/red-duck-82) | CARD_BACKGROUND | Sfondo decorativo valutabile solo dopo lettura del codice | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-005_original.css) |
| [UIV-006](https://uiverse.io/JustCode14/red-dingo-61) | SWITCH | Toggle semantico legato a impostazione reale | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-006_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-006_original.css) |
| [UIV-007](https://uiverse.io/arthur_6104/orange-walrus-50) | LOADER | Stato attesa job reale; frase personalizzata quando appropriata | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-007_original.css) |
| [UIV-009](https://uiverse.io/eslam-hany/selfish-bobcat-73) | BOOK_CARD | Card libro apribile con tap; note/ricordi e raccolte | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html) |
| [UIV-010](https://uiverse.io/00Kubi/fluffy-jellyfish-87) | CARD | Ricordi/diario illustrato | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-010_original.css) |
| [UIV-014](https://uiverse.io/ElSombrero2/tricky-robin-67) | CARD | Ricordi/diario illustrato | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-014_original.html) |
| [UIV-015](https://uiverse.io/FColombati/spotty-snake-82) | BUTTON | CTA con azione verificata e focus | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.css) |
| [UIV-017](https://uiverse.io/Gidarx/moody-falcon-73) | CARD | Ricordi/diario illustrato | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-017_original.css) |
| [UIV-021](https://uiverse.io/JohnnyCSilva/black-rabbit-68) | CARD | Ricordi/diario illustrato | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-021_original.html) |
| [UIV-023](https://uiverse.io/LilaRest/soft-baboon-75) | RADIO | Selettore visualizzazione | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-023_original.html) |
| [UIV-024](https://uiverse.io/MuhammadHasann/fast-badger-70) | CARD | Ricordi/diario illustrato | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-024_original.html) |
| [UIV-027](https://uiverse.io/Nawsome/empty-snail-69) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-027_original.html) |
| [UIV-033](https://uiverse.io/Praashoo7/smooth-crab-52) | BUTTON | CTA con azione verificata e focus | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-033_original.html) |
| [UIV-035](https://uiverse.io/Pradeepsaranbishnoi/hungry-bat-66) | RADIO | Selettore visualizzazione | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-035_original.html) |
| [UIV-038](https://uiverse.io/Priyanshu02020/popular-puma-87) | BUTTON | CTA con azione verificata e focus | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-038_original.css) |
| [UIV-047](https://uiverse.io/Yaya12085/plastic-quail-42) | BUTTON | CTA con azione verificata e focus | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-047_original.html) |
| [UIV-048](https://uiverse.io/akshat-patel28/quick-baboon-29) | CARD | Ricordi/diario illustrato | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-048_original.html) |
| [UIV-049](https://uiverse.io/andrew-demchenk0/honest-stingray-90) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-049_original.html) |
| [UIV-056](https://uiverse.io/chase2k25/warm-chicken-23) | CARD | Ricordi/diario illustrato | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-056_original.css) |
| [UIV-060](https://uiverse.io/dexter-st/breezy-zebra-94) | BUTTON | CTA con azione verificata e focus | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-060_original.css) |
| [UIV-067](https://uiverse.io/elijahgummer/young-horse-7) | RADIO | Selettore visualizzazione | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-067_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-067_original.css) |
| [UIV-069](https://uiverse.io/fthisilak/bitter-termite-36) | BUTTON | CTA con azione verificata e focus | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.css) |
| [UIV-075](https://uiverse.io/joe-watson-sbf/honest-bullfrog-6) | CARD | Ricordi/diario illustrato | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-075_original.html) |
| [UIV-080](https://uiverse.io/kennyotsu/short-ape-5) | CARD | Ricordi/diario illustrato | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-080_original.html) |
| [UIV-087](https://uiverse.io/marcelodolza/fat-zebra-11) | BUTTON | CTA con azione verificata e focus | HIGH | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-087_original.html) |
| [UIV-088](https://uiverse.io/mobinkakei/great-skunk-8) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-088_original.html) |
| [UIV-091](https://uiverse.io/monkey_8812/curly-moth-56) | CARD | Ricordi/diario illustrato | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-091_original.css) |
| [UIV-092](https://uiverse.io/mymiamo/quiet-dragon-5) | CARD | Ricordi/diario illustrato | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-092_original.css) |
| [UIV-095](https://uiverse.io/seoulchik/funny-seahorse-89) | CARD | Ricordi/diario illustrato | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-095_original.css) |
| [UIV-098](https://uiverse.io/whoisyourdeadie/foolish-rabbit-13) | PATTERN | Texture background con gate contrasto/FPS | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-098_original.css) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.

## Uiverse — refresh preferiti 108 (18/11/2026)

**6 nuove associazioni**, derivate dagli undici nuovi preferiti con HTML/CSS originale recuperato da Uiverse. Nessuna nuova autenticazione obbligatoria; la proposta non modifica il codice consumer.

| Sorgente | Famiglia | Superficie proposta | Fit | Codice sorgente |
|---|---|---|---|---|
| [UIV-101](https://uiverse.io/Javierrocadev/chatty-ladybug-95) | FORM | Inserimento nome/codice Insieme senza nuovo login, preservando privacy e sync | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-101_original.css) |
| [UIV-102](https://uiverse.io/Praashoo7/bitter-pig-24) | FORM | Inserimento nome/codice Insieme senza nuovo login, preservando privacy e sync | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-102_original.css) |
| [UIV-104](https://uiverse.io/alexmaracinaru/tall-owl-30) | FORM | Inserimento nome/codice Insieme senza nuovo login, preservando privacy e sync | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-104_original.css) |
| [UIV-105](https://uiverse.io/ayyjayy2/sour-dog-94) | FORM | Inserimento nome/codice Insieme senza nuovo login, preservando privacy e sync | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-105_original.css) |
| [UIV-109](https://uiverse.io/mamyapro123/curvy-bear-51) | FORM | Inserimento nome/codice Insieme senza nuovo login, preservando privacy e sync | HIGH | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-109_original.css) |
| [UIV-111](https://uiverse.io/vinodjangid07/horrible-warthog-14) | FORM | Inserimento nome/codice Insieme senza nuovo login, preservando privacy e sync | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-111_original.css) |

Ogni riferimento resta `PROPOSED_ONLY`: prima del riuso servono Product Bible, revisione estetica, UI/accessibilità, licenza e test nel consumer.

[Confronto 97→108](../UI-UX/UIVERSE/FAVORITES/CONFRONTO_108_VS_97_2026-11-18.json) · [Analisi tecnica degli 11](../UI-UX/UIVERSE/FAVORITES/ANALISI_REFRESH_11_2026-11-18.json).

## Flutter Gems / Forui / F22 — librerie UI native (18/11/2026)

Fonti: [Flutter Gems](https://fluttergems.dev/), [Forui Button](https://forui.dev/docs/widgets/form/button) e [F22 Labs 2026](https://www.f22labs.com/blogs/top-8-flutter-ui-libraries-for-2025-you-must-explore/). [Matrice bidirezionale](../UI-UX/FLUTTER_UI_LIBRARIES_APP_MAP_2026-11-18.json). **PROPOSED_ONLY, NOT_VERIFIED**: prima rispettare le reference utente in Design-App e Product Bible, poi verificare il package originale e il codice consumer.

| Libreria | Fit | Uso ipotizzato |
| --- | --- | --- |
| Forui | MEDIUM | form controls matching approved diary style |
| Mix | HIGH | product-owned visual tokens |

Nessun package installato, nessuna modifica dati/architettura o Golden promosso; verifica Flutter SDK, dipendenze, APK size, accessibilità e performance necessaria prima dell'adozione.


## DSK-011 — Unslop UI, audit sottrattivo (19/11/2026)

**PROPOSED_ONLY · fonte OSS MIT** [felipebasurto/unslop-ui @ cd891160453f26aaacc569bad96a8d10d595076d](https://github.com/felipebasurto/unslop-ui/tree/cd891160453f26aaacc569bad96a8d10d595076d). [Audit e limiti](../sources/UNSLOP_UI_AUDIT_2026-11-19.md) · [matrice di associazione](../UI-UX/UNSLOP_UI_APP_MAP_2026-11-19.json).

**Proposta:** Organic iOS Journal: individua etichette ornamentali, microcopy ripetitivo e stati non supportati, senza toccare le scelte editoriali Rose/HSV, Manrope/Lora, Classic o privacy. Le U1–U20 sono controlli diagnostici e alias degli AT-01…AT-64, non un nuovo tema. Riutilizzo **ADAPT_NATIVE / SOURCE_REVIEW**; nessun automatismo rimuove elementi, nessun consumer certificato da questo dossier. Product Bible e reference preferite restano prioritarie. Stato visivo/fisico: **NOT_VERIFIED**.


## Fonti esterne aggiunte — 20/11/2026 (15 URL, 14 servizi unici)

Intake visivo documentale: [audit](../sources/DESIGN_SITES_15_AUDIT_2026-11-20.md) · [matrice per app](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.md) · [registro JSON](../UI-UX/DESIGN_SITES_15_APP_MAP_2026-11-20.json).

- **Recent Design** (`DESIGN-SITE-018`): App icon and typography moodboards. **Stato: PROPOSED_ONLY**.
- **Font in Logo** (`DESIGN-SITE-020`): Match editorial title typography to product tone. **Stato: PROPOSED_ONLY**.
- **60FPS** (`DESIGN-SITE-021`): Contextual bottom sheets, card transitions, long press. **Stato: PROPOSED_ONLY**.
- **Fontshare** (`DESIGN-SITE-022`): Pair serif editorial headings with neutral readable UI fonts. **Stato: PROPOSED_ONLY**.
- **Realtime Colors** (`DESIGN-SITE-023`): Preview text/background/primary/secondary/accent combinations on real UI. **Stato: PROPOSED_ONLY**.
- **Coolors** (`DESIGN-SITE-024`): Generate candidate 5-color palettes, then test in actual screen. **Stato: PROPOSED_ONLY**.
- **Lucide** (`DESIGN-SITE-025`): Consistent stroke and semantic icon naming. **Stato: PROPOSED_ONLY**.
- **Shots** (`DESIGN-SITE-027`): Create marketing phone/device mockups from own QA screenshots. **Stato: PROPOSED_ONLY**.
- **Cosmos** (`DESIGN-SITE-028`): Moodboard collections and search by color/similarity. **Stato: PROPOSED_ONLY**.

I pattern richiedono decisione di prodotto, valutazione della licenza e QA sulla schermata target. Nessun componente, font, foto o logo di terzi e' stato copiato; nessuna funzione consumer risulta implementata da questo intake.


## Design external sources 20/11/2026 — Figma, ReUI, Best Designs on X

[Audit e prove](../sources/DESIGN_SOURCES_FIGMA_REUI_BESTDESIGNSONX_2026-11-20.md) · [Matrice per app](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.md) · [Catalogo JSON](../UI-UX/DESIGN_SOURCES_4_APP_MAP_2026-11-20.json).

- **Best Designs on X** (`DESIGN-SITE-029`): Curate editorial diary layouts from credited original creators; do not copy X imagery. **PROPOSED_ONLY**.
- **Figma Community Mobile Apps** (`DESIGN-SITE-030`): Study mobile journal/calendar multi-screen kits and reusable navigation patterns. **PROPOSED_ONLY**.
- **Bento Widget Templates** (`FIGMA-BENTO-001`): Personalizable Il tuo spazio grid with compact ricordi, giorno, diario cards; preserve approved editorial identity. **PROPOSED_ONLY**.

[File Figma Bento con nodi e varianti verificati](../UI-UX/FIGMA_BENTO_WIDGET_TEMPLATES_2026-11-20.json). **Bento indica tile di interfaccia, non un vero widget Android.**

Licenze degli asset e approvazione estetica per-app obbligatorie prima di qualsiasi codice o risorsa distribuita. Proposte non implementate, nessun nuovo Golden.
