# World Days — Dossier Design-App

**Registro permanente:** [Indice PER_APP](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Catalogo ICONE](../ICONE/README.md) · [Skill UI/UX](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato: PROPOSAL_ONLY.** La Product Bible e il codice HEAD di questa app non sono stati verificati in questo intervento. Le decisioni del prodotto prevalgono sul dossier. Le idee non sono codice implementato o certificato.

## Identità e direzione visiva

Giornate del mondo: schede editoriali colorate, densità informativa elevata e palette esistente da mantenere.

**Temi candidati:** calendario; ricorrenza; storia; preferiti; offline.

## Superfici e placement proposti

1. scheda giornata e informazioni varie.
2. salvataggio preferiti.
3. navigazione calendario e download contenuti.
4. sezioni storiche multilingue.

## Icone Gentleface collegate (molti-a-molti)

| Icona | Fit | Superficie proposta | Evidenza animazione |
|---|---|---|---|
| [ICO-001 · bell-ring](https://gentleface.com/icons/bell-ring) | MEDIUM | avviso contenuto disponibile | VERIFIED_SITE |
| [ICO-002 · calendar](https://gentleface.com/icons/calendar) | HIGH | navigazione giorni | VERIFIED_SITE |
| [ICO-005 · download](https://gentleface.com/icons/download) | HIGH | contenuti offline | VERIFIED_DETAIL |
| [ICO-006 · export](https://gentleface.com/icons/export) | MEDIUM | condivisione/export soltanto se implementato | VERIFIED_DETAIL |
| [ICO-010 · bookmark](https://gentleface.com/icons/bookmark) | HIGH | salva ricorrenze | VERIFIED_DETAIL |
| [ICO-011 · search](https://gentleface.com/icons/search) | HIGH | ricerca giornate | VERIFIED_DETAIL |
| [ICO-013 · loader](https://gentleface.com/icons/loader) | HIGH | download e caricamento reale | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | download verificato | VERIFIED_SITE |
| [ICO-016 · map-pin](https://gentleface.com/icons/map-pin) | MEDIUM | localizzazione evento solo se presente | VERIFIED_SITE |
| [ICO-017 · cloud](https://gentleface.com/icons/cloud) | MEDIUM | download contenuti reale | VERIFIED_SITE |
| [ICO-019 · star](https://gentleface.com/icons/star) | MEDIUM | giornate preferite | VERIFIED_SITE |
| [ICO-024 · archive](https://gentleface.com/icons/archive) | MEDIUM | collezioni archiviate se supportate | VERIFIED_SITE |
| [ICO-026 · home](https://gentleface.com/icons/home) | MEDIUM | home delle ricorrenze | VERIFIED_SITE |

**Nuove icone da cercare/disegnare:** calendar, bookmark, download. Sono idee, non asset acquisiti o licenziati.

## Motion / trigger

- bookmark breve dopo salvataggio reale.
- download solo durante trasferimento.
- microtransizione giorno senza variare i colori.

## Cosa evitare

- spostare informazioni in icone senza testo.
- cambiare la palette che l'utente ha già approvato.
- celebrare un contenuto ancora non certificato.

## Fonti e skill di design

| Fonte | Fit | Uso proposto |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | daily content cards and empty-state polish |
| DSK-002 — Impeccable | HIGH | content density, long-copy and reader flow |
| DSK-003 — Taste Skill | MEDIUM | content discovery pages where web-native |
| DSK-004 — Emil Design Engineering | MEDIUM | subtle content-card transitions |
| DSK-005 — Vercel Web Design Guidelines | HIGH | content-heavy web views and navigation |
| DSK-006 — Anthropic Frontend Design | HIGH | recognizable day-story cards |
| DSK-007 — Hallmark | MEDIUM | public promotional pages |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | long story and multilingual layouts |
| DSK-009 — UI UX Pro Max | HIGH | information-card design and locale-aware typography |
| DSK-010 — Stageshow | HIGH | new rich-story feature preview |

## Provenienza e storico

- **Fonte:** [Design Harvest](../sources/COVERAGE.md), [matrice UI/UX](../UI-UX/MATRICE_APP_STILI.md), [registro ICONE](../ICONE/REGISTRO_ICONE.json) e [mappa skill](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.json).
- **17/11/2026:** dossier creato da catalogazione e proposte, senza implementazioni consumer.
- **Prossimo gate:** confrontare Product Bible, schermate e codice reali, approvare un pattern e verificare file/licenza, fallback statico, a11y, performance, test e collaudo prima di dichiararlo implementato.

Non cancellare le decisioni superate: aggiungere nuove voci al changelog del JSON e aggiornare questa scheda nella stessa PR.

## Voice Orb — proposta futura (MEDIUM)

**Origine:** [DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) → [beUI Voice Orb](https://beui.dev/components/agents/voice-orb) · [Audit sorgente](../sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md) · [Mappa molti-a-molti](../UI-UX/VOICE_ORB_APP_MAP_2026-11-17.md).

- **Idea:** Memo personali su una ricorrenza solo se la funzione verrà prevista.
- **Collocazione candidata:** Spazio note utente separato dal contenuto editoriale.
- **Adattamento estetico:** palette attuale invariata.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (HIGH)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-002 · Card Stack Peel (MEDIUM)** — Transizioni fra card, album e raccolte in una stessa schermata; stato e back invariati. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (HIGH)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-004 · Interlocking Gear Step (MEDIUM)** — Operazioni realmente attive, pausa fuori schermo, stop al termine, progress bar determinate quando disponibili. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-005 · Shutter Step Slices (MEDIUM)** — Comparsa di dettagli/pannelli secondari, senza ritagliare il contenuto e senza flash ripetuti. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (HIGH)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-001 · [CurtainReveal](https://devlibraries.com/libraries/amicro/CurtainReveal) (MEDIUM):** Optional cover of a story, never gating text. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-003 · [Perspective Flip](https://devlibraries.com/libraries/amicro/perspective-flip) (MEDIUM):** Historical fact card front/back, keep full text accessible. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-004 · [Scroll Reveal](https://devlibraries.com/libraries/amicro/scroll-reveal) (HIGH):** Long editorial history and day cards without hiding accessibility text. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.
- **AMX-005 · [Spatial Door Portal](https://devlibraries.com/libraries/amicro/spatial-door-portal) (MEDIUM):** Special day detail entrance only if subtle. *Sorgente:* `EXACT_SOURCE_NOT_LOCATED`; `PROPOSED_ONLY`.
- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (HIGH):** Content download or parsing while active. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## Watermelon UI — 9 riferimenti (17/11/2026)

[Audit sorgente e licenza](../sources/WATERMELON_UI_NINE_AUDIT_2026-11-17.md) · [Matrice app-componenti](../UI-UX/WATERMELON_NINE_APP_MAP_2026-11-17.md). Queste sono **proposte**; nessuna nuova feature o libreria implementata.

- **WML-001 · [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) (MEDIUM)** — Esplora giornate in evidenza senza perdere ricerca. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-002 · [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) (MEDIUM)** — Selezione giorno opzionale con supporto date reali. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-004 · [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) (MEDIUM)** — Filtra ricorrenze per intervallo del calendario. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-005 · [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) (MEDIUM)** — Account volontario, non bloccare lettura del catalogo. *Evidenza:* `SOURCE_FILE_READ`; stato `PROPOSED_ONLY`.
- **WML-006 · [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) (MEDIUM)** — Accento su heading senza cambiare colori approvati. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-008 · [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) (MEDIUM)** — Una ricorrenza del giorno nel riepilogo, non cancellare contenuti editoriali. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.
- **WML-009 · [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) (MEDIUM)** — Conto alla rovescia fino alla prossima giornata selezionata. *Evidenza:* `EXACT_SOURCE_NOT_LOCATED`; stato `PROPOSED_ONLY`.

**Gate comune:** Product Bible e HEAD consumer, accessibilità, input alternativi, reduced-motion, performance, palette e lingua. Flutter/Compose richiedono adattamento nativo dei riferimenti React. `Text Gradient`, `Notification List` e `Flip Clock` restano nomi senza sorgente esatta verificata nel repo a commit fissato.

**Storico 17/11/2026:** collegamenti persistiti in `PER_APP/REGISTRO_APP_DESIGN.json` come `watermelon_ui_candidates`, stato `PROPOSED_ONLY`.
