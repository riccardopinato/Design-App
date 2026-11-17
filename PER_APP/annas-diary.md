# Anna's Diary — Dossier Design-App

**Registro permanente:** `PER_APP/annas-diary.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

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
