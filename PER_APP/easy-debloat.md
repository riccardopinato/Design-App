# Easy Debloat — Dossier Design-App

**Registro permanente:** `PER_APP/easy-debloat.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Utility sicurezza minimale premium: SAFE/CAUTION/DANGEROUS sempre espliciti e accessibili.

**Categorie da studiare:** package app · rimozione controllata · severità rischio · diagnostica.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. lista applicazioni e dettagli.
2. flusso disattivazione/disinstallazione con conferma.
3. esiti Shizuku/ADB e prerequisiti.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-023 · eye](https://gentleface.com/icons/eye) | MEDIUM | espandi dettagli app | VERIFIED_SITE |
| [ICO-027 · shield-check](https://gentleface.com/icons/shield-check) | MEDIUM | operazione sicura ma mai garanzia assoluta | ANIMATION_UNVERIFIED |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `eye`, `check`, `shield-check`.

## Animazioni e feedback proposti

- conferma azione solo dopo esito comando reale.
- breve espansione dettagli senza movimento eccessivo.

## Cosa evitare

- scudo o check che implica protezione automatica.
- rosso/verde come unico canale informativo.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-009 — UI UX Pro Max | HIGH | severity-safe utility tokens |

## Stato, provenance e aggiornamenti

- **Per la app:** implementazione non verificata; Product Bible non confrontata; solo catalogo Design-App.
- **Per le fonti:** Gentleface = reference; skill = reference; altre icone tematiche = idea non ancora reperita.
- **Contenuti da conservare:** direzione visiva, categorie, placement, trigger, do-not, app↔icone e app↔skill. Non sostituire la precedente evidenza quando cambia lo stato: aggiungere una voce al changelog.
- **Fonti interne:** [Cover Design Harvest](../sources/COVERAGE.md) · [UI/UX app↔stili](../UI-UX/MATRICE_APP_STILI.md) · [Icon Adapter Pack](../packs/icons/README.md).
- **17/11/2026:** scheda creata dal catalogo e dalle proposte correnti; nessuna app alterata.

## Prossima verifica per arrivare a un'implementazione

Confrontare HEAD, Product Bible e schermate reali; confermare i pattern da implementare, licenza file/asset, fallback statico e a11y; pilot con 2–3 icone al massimo, prove visive e test runtime prima di aggiornare lo stato da `PROPOSAL_ONLY`.

## Tema, transizioni, tendine e loader — intake 17/11/2026

[Audit EaseUI/Amicro](../sources/EASEUI_AMICRO_PATTERNS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/EASEUI_AMICRO_LOADING_APP_MAP_2026-11-17.md). **Reference esterne, nessuna implementazione o approvazione di feature nella presente app.**

- **DSP-001 · EaseUI Theme Toggle (MEDIUM)** — Preferenze tema Light/Dark/System, palette, tokens, focus/accessibilità persistenti. *Evidenza:* SOURCE_FILE_READ; status PROPOSED_ONLY.
- **DSP-003 · Accordion Blind Pull (MEDIUM)** — Accordion e pannelli espandibili, non un widget picker/menu funzionante. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-004 · Interlocking Gear Step (MEDIUM)** — Operazioni realmente attive, pausa fuori schermo, stop al termine, progress bar determinate quando disponibili. *Evidenza:* SOURCE_FILE_READ (rettifica ricerca 17/11/2026); status PROPOSED_ONLY.
- **DSP-006 · Loading & Waiting Visual References (user screenshot) (MEDIUM)** — Loader brevi solo quando necessari; skeleton per contenuti; indicatore %/byte se misurabile; timeout/error/retry nei tempi lunghi. *Evidenza:* USER_IMAGE_NOT_ARCHIVED_AS_BINARY; status PROPOSED_ONLY.

Per il tema chiaro/scuro preservare ThemeMode (sistema/chiaro/scuro), preferenze, Golden, palette e accessibilità; per le tendine distinguere Accordion Blind Pull (espansione) da Shutter Step Slices (comparsa). Per loading usare sempre lo stato reale, fallback statico/reduced motion, retry/errori e nessuna GPU persistente in background. Lo screenshot dell'utente è documentato come **riferimento non vendorizzato**; non sono stati importati asset o file eseguibili.

**Storico 17/11/2026:** nuove proposte registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` nel campo `motion_design_candidates`; non cancellare i riferimenti e le decisioni precedenti.

## Nuove microinterazioni Amicro — 6 references (17/11/2026)

- **AMX-006 · [Accordion Loader](https://devlibraries.com/libraries/amicro/accordion-loader) (MEDIUM):** ADB/Shizuku operation pending real acknowledgment. *Sorgente:* `SOURCE_FILE_READ`; `PROPOSED_ONLY`.

[Audit sorgenti, licenze ed evidenze](../sources/AMICRO_SIX_COMPONENTS_AUDIT_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/AMICRO_SIX_COMPONENTS_APP_MAP_2026-11-17.md).

**Decisione:** proposte di design, non implementazioni né approvazioni della Product Bible. Solo 4 dei 6 componenti dispongono di un file con nome/implementazione corrispondente esaminato. Per Perspective Flip e Spatial Door Portal si conserva il link come idea, senza inventare codice. Il loader Accordion è indeterminato: nessuna percentuale senza lavoro realmente misurato. Evitare animazioni continue fuori schermata e rispettare reduced-motion, performance e testo accessibile.

**Storico 17/11/2026:** nuova mappatura registrata in `PER_APP/REGISTRO_APP_DESIGN.json` campo `amicro_six_candidates`; rettificata la provenienza dei precedenti quattro effetti Amicro dove presenti.

## DevLibraries Bookmarks — screenshot 17/11/2026

[Inventario user-supplied e fonte](../sources/DEVLIBRARIES_BOOKMARK_SCREENSHOTS_2026-11-17.md) · [Matrice molti-a-molti](../UI-UX/DEVLIBRARIES_BOOKMARKS_APP_MAP_2026-11-17.md). **Proposte di compatibilità, nessun consumer implementato e nessuna Product Bible modificata.**

- **DBM-009 · Terminal Loader (MEDIUM)** — Operazione ADB/Shizuku effettiva. Evidenza: `SOURCE_PATH_PINNED`; [file originale](https://github.com/Subhan-code/Amicro--Micro-transitions-/blob/fa5f8ffbe39537a8db191806066b8773c47c82e9/registry/ui/loading/terminal-loader.tsx). Stato: `PROPOSED_ONLY`.

**Controlli obbligatori:** loader solo mentre esiste un'operazione reale; usare avanzamento determinato se misurabile; prevedere timeout/error/retry, accessibilità, reduced-motion, stop fuori viewport e budget FPS/APK. Face Id Scan non conferma autenticazione biometrica, View On Map richiede controllo privacy/provider, Infinite Spiral è un effetto media non un loader. Screenshot forniti in chat ma **file PNG non archiviati nel repo**: nomi/ordine/hash sono nel JSON canonico. Per Flutter/Compose, il codice React è soltanto riferimento e richiede adattamento/test.

**Storico 17/11/2026:** 1 relazioni registrate anche in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `bookmarked_visual_references`, senza duplicare gli ID già esistenti.

## Uiverse — proposte 18/11/2026

- **UIV-006 — [JustCode14/red-dingo-61](https://uiverse.io/JustCode14/red-dingo-61)**: Toggle semantico legato a impostazione reale (MEDIUM). Originale da estrarre.
- **UIV-008 — [Shoh2008/cold-walrus-85](https://uiverse.io/Shoh2008/cold-walrus-85)**: Caricamento temporaneo con stop/errore/retry (MEDIUM). [Sorgente originale](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-008_original.html).

[Catalogo](../UI-UX/UIVERSE/README.md) · [mappa bidirezionale](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.json) · [archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato **PROPOSED_ONLY**; nessun codice consumer integrato, nessuna approvazione Product Bible implicita.

## Uiverse Favorites — archivio incrociato 18/11/2026

**28 preferiti proposti per easy-debloat**. Nessuna funzione è implementata in questa app. Per ogni riferimento: licenza/provenienza, Product Bible, accessibilità, riduzione movimento, GPU/battery budget, screenshot QA e codice consumer prima dell'adozione.

| ID / Uiverse | Famiglia | Schermata o ruolo proposto | Fit | Codice nel Design-App |
|---|---|---|---|---|
| [UIV-006](https://uiverse.io/JustCode14/red-dingo-61) | SWITCH | Toggle semantico legato a impostazione reale | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-006_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-006_original.css) |
| [UIV-011](https://uiverse.io/Admin12121/black-sheep-17) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-011_original.html) |
| [UIV-012](https://uiverse.io/Admin12121/massive-dodo-67) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-012_original.html) |
| [UIV-015](https://uiverse.io/FColombati/spotty-snake-82) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-015_original.css) |
| [UIV-025](https://uiverse.io/Nawsome/ancient-yak-42) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-025_original.html) |
| [UIV-029](https://uiverse.io/Nawsome/wet-mayfly-23) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-029_original.html) |
| [UIV-030](https://uiverse.io/Nawsome/young-goat-78) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-030_original.html) |
| [UIV-034](https://uiverse.io/Pradeepsaranbishnoi/fast-cobra-20) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-034_original.html) |
| [UIV-039](https://uiverse.io/SelfMadeSystem/pretty-treefrog-77) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-039_original.html) |
| [UIV-040](https://uiverse.io/Shoh2008/curvy-bulldog-27) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-040_original.html) |
| [UIV-044](https://uiverse.io/Subaashbala/average-horse-18) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-044_original.html) |
| [UIV-046](https://uiverse.io/Uncannypotato69/rotten-wasp-10) | CHECKBOX | Selezione con semantica e feedback | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-046_original.css) |
| [UIV-047](https://uiverse.io/Yaya12085/plastic-quail-42) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-047_original.html) |
| [UIV-049](https://uiverse.io/andrew-demchenk0/honest-stingray-90) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-049_original.html) |
| [UIV-057](https://uiverse.io/cohencoo/dry-rat-94) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-057_original.html) |
| [UIV-058](https://uiverse.io/cssbuttons-io/mean-dolphin-24) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-058_original.html) |
| [UIV-059](https://uiverse.io/cuzpq/gentle-goat-72) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-059_original.html) |
| [UIV-061](https://uiverse.io/dexter-st/bright-lizard-8) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-061_original.css) |
| [UIV-062](https://uiverse.io/dexter-st/spicy-otter-30) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-062_original.css) |
| [UIV-066](https://uiverse.io/elijahgummer/polite-earwig-72) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-066_original.css) |
| [UIV-069](https://uiverse.io/fthisilak/bitter-termite-36) | BUTTON | CTA con azione verificata e focus | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-069_original.css) |
| [UIV-071](https://uiverse.io/gharsh11032000/sour-vampirebat-66) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-071_original.html) |
| [UIV-076](https://uiverse.io/kat_2522/rude-robin-51) | LOADER | Attesa attività reale e risoluzione errore | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-076_original.css) |
| [UIV-085](https://uiverse.io/m1her/odd-fireant-56) | SWITCH | Preferenza on/off persistita | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-085_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-085_original.css) |
| [UIV-086](https://uiverse.io/mamyapro123/cuddly-warthog-66) | SWITCH | Preferenza on/off persistita | MEDIUM | [HTML](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-086_original.html) · [CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-086_original.css) |
| [UIV-087](https://uiverse.io/marcelodolza/fat-zebra-11) | BUTTON | CTA con azione verificata e focus | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-087_original.html) |
| [UIV-090](https://uiverse.io/mobinkakei/strong-lizard-79) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-090_original.html) |
| [UIV-100](https://uiverse.io/zanina-yassine/afraid-eel-50) | SWITCH | Preferenza on/off persistita | MEDIUM | [Originale HTML/CSS](../UI-UX/UIVERSE/CODICE_SORGENTE/UIV-100_original.html) |

[Registro 97 Favorites](../UI-UX/UIVERSE/FAVORITES/REGISTRO_PREFERITI_2026-11-18.json) · [Matrice complessiva 25 app](../UI-UX/UIVERSE/MATRICE_APP_COMPONENTI.md) · [Archivio codice](../UI-UX/UIVERSE/CODICE_SORGENTE/README.md). Stato: **PROPOSED_ONLY**.
