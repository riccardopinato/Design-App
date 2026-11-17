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
1. Design-App COPY_READY / LIBRARY_VERIFIED item.
2. App-Factory-Core Golden or certified internal donor when applicable.
3. Design-App SOURCE_VERIFIED first-party pattern.
4. Design-App REFERENCE / external OSS source.
5. New implementation.

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
- Material 3 can be the technical foundation without forcing a generic Material look.
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
