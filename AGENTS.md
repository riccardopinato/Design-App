# AGENTS.md — Design-App

## Role
Design-App is the specialized design library for the App Factory.

It stores reusable visual patterns, UI/UX references, motion patterns, design tokens,
iconography, semantic sound/haptic patterns, first-party source snapshots, tested
components and external design sources.

It does NOT replace:
- App-Factory-Core CURRENT / Master / Golden Rules;
- a product's Product Bible;
- a product's roadmap;
- the app repository's own architecture and source of truth.

## Intake rule
Whenever work on an App Factory project discovers a reusable design pattern,
animation, sound asset, icon system, library, component, layout, interaction or external repository, evaluate
it for Design-App without waiting for a separate request.

## Maturity states
DISCOVERY -> REFERENCE -> ADAPTED -> SOURCE_VERIFIED -> LIBRARY_VERIFIED -> COPY_READY

Definitions:
- DISCOVERY: interesting source, not yet evaluated enough for reuse.
- REFERENCE: useful visual/interaction idea; not necessarily copyable code.
- ADAPTED: normalized for App Factory conventions.
- SOURCE_VERIFIED: implementation already works/tests in the source app.
- LIBRARY_VERIFIED: extracted version has its own validation evidence.
- COPY_READY: safe rapid-reuse asset with provenance, license and usage notes.

Never label an item COPY_READY solely because the source repository works.

## Reuse hierarchy
1. App-Factory-Core CERTIFIED GOLDEN / COPY-READY GOLDEN and its binding technical contracts.
2. App-Factory-Core CERTIFIED DONOR / applicable candidate Golden with explicit consumer audit.
3. Design-App COPY_READY / LIBRARY_VERIFIED visual asset or implementation compatible with the above.
4. Design-App SOURCE_VERIFIED first-party pattern, when source/version matches consumer requirements.
5. Design-App REFERENCE / external OSS source; new implementation only when gaps remain.

This hierarchy is for technical admission. The target app Product Bible and approved design direction retain visual/product ownership. A visual reference never overrides a Golden's accessibility, lifecycle or release requirements. Do not interpret the old specialized Design-App selection order as permission to replace Core technical rules.

## Provenance
Every significant item must record:
- source repository/chat/document;
- immutable source ref or file blob when available;
- source path;
- license/ownership;
- reuse mode: COPY | ADAPT | REFERENCE_ONLY;
- validation level;
- known constraints.

## External code
Before copying third-party code:
- verify LICENSE/SPDX;
- prefer maintained sources;
- do not copy code with absent, ambiguous or incompatible license;
- use those sources as REFERENCE_ONLY and reimplement independently.

Do not copy logos, brand identity, proprietary illustrations or recognizable
third-party product identity.

## Design principles
- Visual identity is product-owned, not dictated by any default component toolkit; preserve accessible platform behavior while building distinct tokens/components per app.
- Maintain one coherent icon language.
- Use design tokens rather than screen-local arbitrary values.
- Prefer progressive disclosure over crowded surfaces.
- Respect reduced-motion/accessibility preferences.
- Minimum interactive targets should normally be 48 dp where platform conventions apply.
- Empty/loading/error/offline states are part of the design.
- Motion must clarify state, attention or feedback; decorative noise is not a goal.
- Sound is optional semantic feedback, not decoration: never add a sound to every tap.
- Sound must never be the only carrier of state; pair critical meaning with visual/semantic feedback.
- UI sound packs require asset-level licensing, not only a code repository license.
- Critical alarms/safety audio are product capabilities and must not be replaced by decorative UI SFX.
- Responsive layouts should adapt navigation and information density, not merely stretch phone UI.

## Source snapshots
Files under tested/source_snapshots/ are first-party snapshots copied from working
app repositories for fast retrieval. Their header/provenance record identifies the
source. A snapshot remains pinned; updates create a new version rather than silently
rewriting history when the behavior materially changes.


## External design-source categories
Use external sources according to their classification:
- TOOLING_DONOR: development/design-system tooling; do not ship unless the app needs it.
- CODE_DONOR: runtime library candidate; apply Dependency Admission before adding it.
- UI_UX_REFERENCE: study concepts and reimplement in the target design system.
- ASSET_SOURCE: verify asset-level license before vendoring icons/audio.
- REFERENCE_ONLY: never copy code/assets when licensing or fit is uncertain.

For motion, prefer the smallest tier that solves the problem:
1. native/framework animation;
2. lightweight composable motion;
3. Lottie/dotLottie for bounded vector sequences;
4. Rive for genuinely interactive/stateful animation.

For short UI audio, prefer a small semantic sound set and ordinary platform/player
APIs. Oboe/AudioKit-level engines require a product-level reason.

## Persistenza delle idee di design per ogni app

Quando l'utente fornisce una fonte di design esterna, registrare il **sito di scoperta** (es. `sources/DESIGN_RESEARCH_SITES.json`) separatamente dall'**origine del codice** (es. `registry/OSS_DESIGN_SOURCES.yaml`). Ogni componente/asset mantiene URL originale, commit/blob se reperibile, licenza, limiti di riuso e status. Un aggregatore non concede la licenza di tutti i contenuti indicizzati.

Quando una reference è pertinente alle app, aggiornare `PER_APP/REGISTRO_APP_DESIGN.json`, il dossier Markdown delle app interessate e la matrice molti-a-molti nella stessa PR, con changelog e fonte. Lasciare `PROPOSED_ONLY` finché Product Bible e repo consumer non approvano/confermano la feature. Non sovrascrivere informazioni storiche; appendere decisioni e motivazioni.

Per componenti vocali: l'effetto audio-reattivo non gestisce automaticamente microfono, salvataggio, trascrizione, permessi o privacy. Bloccare stati di registrazione senza segnale reale e prevedere fallback statico/reduced-motion; per Flutter minimizzare peso APK e dipendenze GPU.

## Fonti di motion e stati di attesa

Per una proposta di animazione distinguere sorgente implementativa letta, sola descrizione di catalogo, immagine chat non persistita ed esito di test. Non etichettare un comando CLI citato in una scheda come componente funzionante se il relativo file non è individuato. Registrare tema/stack/accordion/stagger/loader come pattern diversi e mappare le app in `PER_APP` senza alterare Product Bible.

Per tema usare Golden/ThemeMode e token del prodotto, animando al massimo la transizione. Loader e progressi devono corrispondere a lavoro reale, con timeout/error/retry, reduced-motion e stop in background. Gli screenshot di chat senza backing file esplicito sono **reference testuali**, non asset visuali caricati su GitHub.

## Provenienza verificabile delle microinterazioni

Per ogni link a un componente di DevLibraries/Amicro distinguere **nome e URL forniti dall'utente** dalla disponibilità di un export omonimo nel repository originale: registrare SHA completo, file, blob ed eventuale `SOURCE_FILE_READ`; se il nome esatto non è localizzabile, conservare `EXACT_SOURCE_NOT_LOCATED` e NON inventare file, comando CLI, implementazione Flutter o licenze specifiche non verificate. Quando una ricognizione corregge un audit precedente, aggiornare i registri esistenti e documentare l'errata attribuzione nello storico, senza scambiare lettura sorgenti per test runtime.

## Catalogazione Watermelon / UI di agenda e notifiche

Per ogni nuovo componente di un portale (es. DevLibraries) tentare URL esatto, poi verificare repository originale. Registrare separatamente: sorgente React letta con SHA/blob, item con solo metadata, e nome non localizzabile. Mai supporre che uno slug 'base' sia un widget Flutter già pronto; verificare il file reale e le dipendenze prima di estrarre. I file demomedia e immagini stock non sono automaticamente licenziati per riuso.

Se un'idea proposta riguarda un riepilogo giornaliero appuntamenti (Anna's Diary), mantenere nel dossier `PER_APP/annas-diary.md` il requisito di **prima apertura giornaliera oppure orario configurato**, senza presumere notifiche push, permessi di sistema, job in background o database. Distinguere visuale in-app da scheduling Android/iOS; richiedere Product Bible, privacy, fuso/DST, deduplica per account/data, gestione sync, errori e verifica su device. Le proposte in Design-App restano PROPOSED_ONLY finché implementazione e test non sono dimostrati.

## Screenshot utente di cataloghi e Bookmarks di design

Quando l'utente condivide screenshot con card design, trascrivere solo nomi, ordine e categorie effettivamente visibili; salvare la provenienza con filename/SHA-256 se il file è disponibile, senza inventare URL o repo specifici da un semplice titolo. Il binario screenshot non è 'salvato nel repo' senza prova di upload reale. Riconciliare i componenti già censiti con ID canonici (es. `AMX-006`, `WML-004`, `WML-008`) anziché duplicarli; gli abbinamenti per app restano PROPOSED_ONLY con changelog, fonte e limite di verifica. Verificare source file e licenza originali **separatamente** da screenshot e sito aggregatore. Per carichi non misurabili un loader può solo indicare attività reale; Face Id Scan non certifica biometria; un overlay View On Map non sostituisce routing offline e può coinvolgere provider esterni. Prima di chiamare `IMPLEMENTED` o `VERIFIED`, ispezionare codice e test dell'app target.

## Revisione design con Impeccable — confine mobile/Web e fonti

La guida https://impeccable.style/designing/ è **un'estensione documentale della fonte già catalogata `DSK-002`**: non aggiungere un secondo OSS repo o donor per ogni sottopagina. Per ogni app usa la Product Bible come source of truth del prodotto, tokens/Golden corrente e decisioni estetiche registrate; `DESIGN.md` può essere una rappresentazione derivata e verificata, mai un database parallelo del product scope.

Operativamente distinguere `critique` (analisi estetica), `audit` (controllo tecnico), `harden` (stati e recupero), `polish` (finitura), `document/extract` (riuso coerente); documentare screenshot, screen size, state, expected vs observed, evidence e severità prima di un claim `VERIFIED`. `npx impeccable detect` e gli hook CSS/HTML/JS sono **Web-only**, non collaudano Flutter/Compose/Android. In app native usare matrice Golden App Shell e vere prove su device (dark/light, font grande, keyboard, safe-area, VoiceOver/TalkBack, empty/loading/error/offline). Evitare competizione fra più skill di design e promozione implicita di un Golden DRAFT. Non introdurre animazioni decorative senza segnali di stato reali.

## Cross-app visual review evidence (2026-11-17)

Follow the canonical App-Factory-Core `contracts/DESIGN_VISUAL_QA_PROCESS_v1.md` and existing Golden App Shell (DRAFT), Theme M3 (COPY-READY), and AppLab QA boundaries. For Impeccable `DSK-002` apply IWC-01..IWC-08 without installing Web-only hooks in native apps. Register pilot plans in `UI-UX/DESIGN_QA_PILOTS_2026-11-17.json` and validate via `scripts/validate_visual_qa_evidence.py`. Screenshots, physical tests, app changes and design approval must remain explicitly NOT_VERIFIED unless backed by exact-head evidence. Never mark a guideline source as COPY_READY or CERTIFIED solely because a documentation validation passes.

## 2026–27 visual source policy (18 November 2026)

- No default framework visual style for new apps. The app Product Bible defines brand, typography and surface language; Flutter remains available as implementation technology.
- Consult `sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md` and the bidirectional UI-UX app matrix for proposed patterns. Dribbble/Collect UI are reference portals only; original shots and assets remain third-party copyrighted unless individually licensed.
- State `PROPOSED_ONLY` until mock-up review, Product Bible admission, exact consumer implementation, visual regression and accessibility QA. Never infer runtime from a static shot.
