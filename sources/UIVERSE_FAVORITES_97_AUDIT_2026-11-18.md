# Audit 97 Favorites Uiverse — 18/11/2026

## Fonte e integrità

- File locale dell'utente: `uiverse-favorites-export.json`; `exported_at=2026-11-18T10:08:06.777Z`, `scan_steps=67`.
- 97 stringhe URL normalizzate, 97 unici, 6 già nel Design-App prima del batch e 91 nuovi.
- Il file stesso ha `completeness=REQUIRES_USER_COUNT_VERIFICATION`: **non attestare che 97 sia il totale effettivo dei segnalibri dell'account**.
- Source archive GitHub `uiverse-io/galaxy@adbd2adde0a299a3956ea288fb444ec01891ca41`: 54 URL corrispondenti ai favoriti, di cui 3 già archiviati, 51 snapshot nuovi.
- 43 link senza copia HTML/CSS in Galaxy; classifica da pagina pubblica dove recuperabile, altrimenti UNKNOWN. I titoli delle pagine non forniscono il codice originale.
- Repository stesso contiene anche tre componenti del primo lotto che non sono in Favorites; totale catalogo 100 e 57 sorgenti archiviati.

## Analisi per categoria

- **LOADER (36)**: verificare stato task reale, progress indicator corretto, timeout/error/retry, blocco riduzione movimento; priorità proposta nel dossier app.
- **CARD (24)**: verificare gerarchia, contenuto accessibile senza hover e media a proporzioni originali; priorità proposta nel dossier app.
- **SWITCH (13)**: on/off semantico con persisted state e feedback affidabile; priorità proposta nel dossier app.
- **BUTTON (7)**: touch/keyboard, semantics, stato e contrasto; priorità proposta nel dossier app.
- **UNKNOWN (7)**: touch/keyboard, semantics, stato e contrasto; priorità proposta nel dossier app.
- **RADIO (3)**: touch/keyboard, semantics, stato e contrasto; priorità proposta nel dossier app.
- **CHECKBOX (2)**: touch/keyboard, semantics, stato e contrasto; priorità proposta nel dossier app.
- **PATTERN (2)**: sfondo solo se non degrada contrasto, GPU/batteria e densità informativa; priorità proposta nel dossier app.
- **CARD_BACKGROUND (1)**: touch/keyboard, semantics, stato e contrasto; priorità proposta nel dossier app.
- **INPUT (1)**: touch/keyboard, semantics, stato e contrasto; priorità proposta nel dossier app.
- **TOOLTIP (1)**: touch/keyboard, semantics, stato e contrasto; priorità proposta nel dossier app.

## Evidenza, licenze, limitazioni

- 54 snippet effettivamente acquisiti da Galaxy per i Favorites: archiviati byte-per-byte (senza adattamenti) in `UI-UX/UIVERSE/CODICE_SORGENTE` e associati ai blob SHA Git.
- Il repository Galaxy reca licenza MIT; conservare LICENSE e attribuzioni. Asset esterni, icone, font e link incorporati non ereditano automaticamente i medesimi diritti.
- Altri 43 componenti possono essere Tailwind/CSS, ma il formato esatto NON va indovinato; alcuni hanno categoria verificata pubblicamente, altri `UNKNOWN`.
- Nessun adattamento Flutter/Compose, consumer test, screenshot review, APK o Golden viene dichiarato completato.

## Protocollo per tutti i futuri siti di preferiti

1. Tentare un accesso diretto verificato; se privato, usare script DOM **specifico del sito**, leggibile e non invasivo, eseguito solo dall'utente nel proprio browser.
2. Mai chiedere/password token/cookie o disabilitare difese del browser senza revisione del codice; niente invio rete nel codice di export.
3. Esportare URLs + conteggio + provenienza; confrontare il conteggio con quello del sito. Salvare `PARTIAL` quando la completezza non è dimostrata.
4. Dedupe e classificazione molti-a-molti, estrazione dell'originale solo con licenza/provenienza, sorgente indisponibile esplicitamente registrato.
5. PR e CI; app consumer, Product Bible e Golden restano separati.

## Registro dettagliato per ogni link

### UIV-010 00Kubi/fluffy-jellyfish-87
- Link: https://uiverse.io/00Kubi/fluffy-jellyfish-87
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): annas-diary, notes-ecosistema, world-days, wonderlog, cooking-anime, framelab, beerclass-ai.

### UIV-011 Admin12121/black-sheep-17
- Link: https://uiverse.io/Admin12121/black-sheep-17
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-011_original.html; blob `6984437ea0d5805fce59054c7dc55b3199108c06`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): world-days, send-to-pc, battery-guard, app-factory-dashboard, easy-debloat, cashmate-ai, omni-cleaner.

### UIV-012 Admin12121/massive-dodo-67
- Link: https://uiverse.io/Admin12121/massive-dodo-67
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-012_original.html; blob `b265064d5513db9b39f8cfde2e802c543aef8c33`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): pocket-guard, phone-guard, easy-debloat, sleepmax-coach, camperboss, the-luminous-infinite-circle, battery-guard.

### UIV-013 AqFox/young-dragon-29
- Link: https://uiverse.io/AqFox/young-dragon-29
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-013_original.html; blob `bdbf3337446aba49c718f7f171187178f7c85947`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): camperboss, wonderlog, cooking-anime, sleepmax-coach, focussense, deskland-android, omni-cleaner.

### UIV-014 ElSombrero2/tricky-robin-67
- Link: https://uiverse.io/ElSombrero2/tricky-robin-67
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-014_original.html; blob `051f5f8db0340b05218814bfdb3cd042b3a01daf`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): annas-diary, notes-ecosistema, world-days, wonderlog, cooking-anime, framelab, beerclass-ai.

### UIV-015 FColombati/spotty-snake-82
- Link: https://uiverse.io/FColombati/spotty-snake-82
- Categoria: BUTTON; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Touch+keyboard, feedback e focus; nessuna CTA senza azione reale.
- App candidate (6): cooking-anime, framelab, beerclass-ai, camperboss, easy-debloat, annas-diary.

### UIV-016 Gidarx/clever-panther-6
- Link: https://uiverse.io/Gidarx/clever-panther-6
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): beerclass-ai, cashmate-ai, app-factory-dashboard, camperboss, edu-01-corpo-umano, deskland-android, notes-ecosistema.

### UIV-017 Gidarx/moody-falcon-73
- Link: https://uiverse.io/Gidarx/moody-falcon-73
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): camperboss, edu-01-corpo-umano, deskland-android, annas-diary, notes-ecosistema, world-days, wonderlog.

### UIV-018 JaydipPrajapati1910/average-shrimp-57
- Link: https://uiverse.io/JaydipPrajapati1910/average-shrimp-57
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-018_original.html; blob `3a28252e0b776fd329b2974b2f956ecf711615c4`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): camperboss, the-luminous-infinite-circle, tabletop-motion-alarm, cashmate-ai, battery-guard, focussense, omni-cleaner.

### UIV-019 JkHuger/new-deer-97
- Link: https://uiverse.io/JkHuger/new-deer-97
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-019_original.html; blob `7658a32997ebed32e5f08a7bf2bfe68d0bf74416`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): sleepmax-coach, focussense, deskland-android, omni-cleaner, notes-ecosistema, framelab, world-days.

### UIV-020 JkHuger/selfish-bulldog-36
- Link: https://uiverse.io/JkHuger/selfish-bulldog-36
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-020_original.html; blob `f1abd425af55eca3e05e69acca69dc454744a8d1`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-021 JohnnyCSilva/black-rabbit-68
- Link: https://uiverse.io/JohnnyCSilva/black-rabbit-68
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-021_original.html; blob `1284138c691e85555b3f1c2785178f1e42c84949`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): camperboss, edu-01-corpo-umano, deskland-android, annas-diary, notes-ecosistema, world-days, wonderlog.

### UIV-004 JohnnyCSilva/jolly-elephant-67
- Link: https://uiverse.io/JohnnyCSilva/jolly-elephant-67
- Categoria: CARD; evidenza: SOURCE_FILE_READ.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-004_original.html; blob `0019adeac6dd9990f16bcc5519dcf24b73dad347`.
- Vincoli: Verifica accessibilità e licenza.
- App candidate (7): wonderlog, camperboss, annas-diary, world-days, notes-ecosistema, framelab, web-utility-factory.

### UIV-006 JustCode14/red-dingo-61
- Link: https://uiverse.io/JustCode14/red-dingo-61
- Categoria: SWITCH; evidenza: SOURCE_CODE_NOT_LOCATED.
- Codice: NON DISPONIBILE.
- Vincoli: Verifica accessibilità e licenza.
- App candidate (8): battery-guard, easy-debloat, focussense, omni-cleaner, 180flipcharge, annas-diary, phone-guard, pocket-guard.

### UIV-022 Lakshay-art/curvy-earwig-22
- Link: https://uiverse.io/Lakshay-art/curvy-earwig-22
- Categoria: INPUT; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-022_original.html; blob `58643ca24accf02472d44f75b92ac021ec6bc356`.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (6): cashmate-ai, app-factory-dashboard, wonderlog, omni-cleaner, world-days, notes-ecosistema.

### UIV-023 LilaRest/soft-baboon-75
- Link: https://uiverse.io/LilaRest/soft-baboon-75
- Categoria: RADIO; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-023_original.html; blob `6a66af15a1670a1dfcbccfc97b19e8485334195a`.
- Vincoli: Stato effettivo, semantica e dimensione touch.
- App candidate (6): annas-diary, notes-ecosistema, cashmate-ai, battery-guard, world-days, wonderlog.

### UIV-024 MuhammadHasann/fast-badger-70
- Link: https://uiverse.io/MuhammadHasann/fast-badger-70
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-024_original.html; blob `b82917e322c0995963fbc4b189cdbf88fe3b66be`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): annas-diary, notes-ecosistema, world-days, wonderlog, cooking-anime, framelab, beerclass-ai.

### UIV-025 Nawsome/ancient-yak-42
- Link: https://uiverse.io/Nawsome/ancient-yak-42
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-025_original.html; blob `414308b9d2e63b6e4b61b187aca687ca3d5ee8f4`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): app-factory-dashboard, easy-debloat, cashmate-ai, camperboss, wonderlog, cooking-anime, trailpath.

### UIV-026 Nawsome/brave-turtle-26
- Link: https://uiverse.io/Nawsome/brave-turtle-26
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-026_original.html; blob `2beba2a88c36c3a9a294d7641c73e9b139cd9582`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): camperboss, wonderlog, cooking-anime, sleepmax-coach, focussense, deskland-android, omni-cleaner.

### UIV-027 Nawsome/empty-snail-69
- Link: https://uiverse.io/Nawsome/empty-snail-69
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-027_original.html; blob `df9b34147dd54d386ac4748febcc4ea7073b8f00`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): focussense, omni-cleaner, 180flipcharge, annas-diary, notes-ecosistema, pocket-guard, battery-guard.

### UIV-028 Nawsome/kind-mole-87
- Link: https://uiverse.io/Nawsome/kind-mole-87
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-028_original.html; blob `fe7843a1ac3913c9dac0a95a376e81fd9dc4f7c5`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-029 Nawsome/wet-mayfly-23
- Link: https://uiverse.io/Nawsome/wet-mayfly-23
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-029_original.html; blob `71f91a8ab8cdd0fd892e15c887ae2de966d676ee`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): world-days, send-to-pc, battery-guard, app-factory-dashboard, easy-debloat, cashmate-ai, omni-cleaner.

### UIV-030 Nawsome/young-goat-78
- Link: https://uiverse.io/Nawsome/young-goat-78
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-030_original.html; blob `503557c486d7eb2170c6b0d0f19a6c75512e3911`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): app-factory-dashboard, easy-debloat, cashmate-ai, camperboss, wonderlog, cooking-anime, omni-cleaner.

### UIV-031 Novaxlo/rotten-lionfish-4
- Link: https://uiverse.io/Novaxlo/rotten-lionfish-4
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): camperboss, wonderlog, cooking-anime, sleepmax-coach, focussense, deskland-android, omni-cleaner.

### UIV-032 Praashoo7/lucky-hound-44
- Link: https://uiverse.io/Praashoo7/lucky-hound-44
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-032_original.html; blob `ead4110cd4088117f484880dfb795a4fbfc6a7c6`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): sleepmax-coach, focussense, deskland-android, omni-cleaner, notes-ecosistema, framelab, world-days.

### UIV-033 Praashoo7/smooth-crab-52
- Link: https://uiverse.io/Praashoo7/smooth-crab-52
- Categoria: BUTTON; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-033_original.html; blob `357bad2a0d52db3af7e2cdbdf21292d4c3b4a9c9`.
- Vincoli: Touch+keyboard, feedback e focus; nessuna CTA senza azione reale.
- App candidate (6): web-utility-factory, app-factory-dashboard, annas-diary, notes-ecosistema, wonderlog, world-days.

### UIV-034 Pradeepsaranbishnoi/fast-cobra-20
- Link: https://uiverse.io/Pradeepsaranbishnoi/fast-cobra-20
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-034_original.html; blob `f27725c14f6e3cf945b71372e95d995f0dafd749`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): world-days, send-to-pc, battery-guard, app-factory-dashboard, easy-debloat, cashmate-ai, omni-cleaner.

### UIV-035 Pradeepsaranbishnoi/hungry-bat-66
- Link: https://uiverse.io/Pradeepsaranbishnoi/hungry-bat-66
- Categoria: RADIO; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-035_original.html; blob `efa91622500bad2b98db6df48d557ca94dbaa2ea`.
- Vincoli: Stato effettivo, semantica e dimensione touch.
- App candidate (6): annas-diary, notes-ecosistema, cashmate-ai, battery-guard, world-days, trailpath.

### UIV-036 Pradeepsaranbishnoi/tall-fish-38
- Link: https://uiverse.io/Pradeepsaranbishnoi/tall-fish-38
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-036_original.html; blob `92558e8d215749b701db6bdbb70cd821be1253ba`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): camperboss, wonderlog, cooking-anime, sleepmax-coach, focussense, deskland-android, omni-cleaner.

### UIV-037 Prince4fff/slippery-baboon-37
- Link: https://uiverse.io/Prince4fff/slippery-baboon-37
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-037_original.html; blob `0cd4da603c62229ff6e2ef7bf7f0b785ba5a1ef1`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): wonderlog, cooking-anime, framelab, beerclass-ai, cashmate-ai, app-factory-dashboard, notes-ecosistema.

### UIV-038 Priyanshu02020/popular-puma-87
- Link: https://uiverse.io/Priyanshu02020/popular-puma-87
- Categoria: BUTTON; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Touch+keyboard, feedback e focus; nessuna CTA senza azione reale.
- App candidate (6): wonderlog, world-days, cooking-anime, framelab, beerclass-ai, annas-diary.

### UIV-039 SelfMadeSystem/pretty-treefrog-77
- Link: https://uiverse.io/SelfMadeSystem/pretty-treefrog-77
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-039_original.html; blob `6e11812581f769d2319c9d4ac8a55d6919581aed`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): world-days, send-to-pc, battery-guard, app-factory-dashboard, easy-debloat, cashmate-ai, omni-cleaner.

### UIV-040 Shoh2008/curvy-bulldog-27
- Link: https://uiverse.io/Shoh2008/curvy-bulldog-27
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-040_original.html; blob `9c500210bf6627cd4ed241d4ca3547e69fe617c2`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): app-factory-dashboard, easy-debloat, cashmate-ai, camperboss, wonderlog, cooking-anime, omni-cleaner.

### UIV-041 Shoh2008/ugly-elephant-80
- Link: https://uiverse.io/Shoh2008/ugly-elephant-80
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-041_original.html; blob `cc7eaaa9f24c666016117d214f7e3ead829eac98`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): camperboss, wonderlog, cooking-anime, sleepmax-coach, focussense, deskland-android, omni-cleaner.

### UIV-042 Shoh2008/yellow-dolphin-16
- Link: https://uiverse.io/Shoh2008/yellow-dolphin-16
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-042_original.html; blob `23a2c1b848505b341dc5bd8c1d84732b7abdebd6`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): sleepmax-coach, focussense, deskland-android, omni-cleaner, notes-ecosistema, framelab, world-days.

### UIV-043 Stavros2410/wet-duck-69
- Link: https://uiverse.io/Stavros2410/wet-duck-69
- Categoria: UNKNOWN; evidenza: PAGE_LINK_FROM_AUTH_EXPORT_CATEGORY_NOT_VERIFIED.
- Codice: NON DISPONIBILE.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (3): notes-ecosistema, world-days, omni-cleaner.

### UIV-044 Subaashbala/average-horse-18
- Link: https://uiverse.io/Subaashbala/average-horse-18
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-044_original.html; blob `015627b6aa0daa8499681adf3fc23614a5e61019`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): world-days, send-to-pc, battery-guard, app-factory-dashboard, easy-debloat, cashmate-ai, omni-cleaner.

### UIV-045 Uncannypotato69/honest-starfish-32
- Link: https://uiverse.io/Uncannypotato69/honest-starfish-32
- Categoria: UNKNOWN; evidenza: PAGE_LINK_FROM_AUTH_EXPORT_CATEGORY_NOT_VERIFIED.
- Codice: NON DISPONIBILE.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (3): omni-cleaner, app-factory-dashboard, notes-ecosistema.

### UIV-046 Uncannypotato69/rotten-wasp-10
- Link: https://uiverse.io/Uncannypotato69/rotten-wasp-10
- Categoria: CHECKBOX; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Stato effettivo, semantica e dimensione touch.
- App candidate (6): app-factory-dashboard, world-days, easy-debloat, wonderlog, camperboss, notes-ecosistema.

### UIV-047 Yaya12085/plastic-quail-42
- Link: https://uiverse.io/Yaya12085/plastic-quail-42
- Categoria: BUTTON; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-047_original.html; blob `d5ca897cb7736ee43d89d013ea8903b5fba4927a`.
- Vincoli: Touch+keyboard, feedback e focus; nessuna CTA senza azione reale.
- App candidate (6): camperboss, easy-debloat, web-utility-factory, app-factory-dashboard, annas-diary, notes-ecosistema.

### UIV-048 akshat-patel28/quick-baboon-29
- Link: https://uiverse.io/akshat-patel28/quick-baboon-29
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-048_original.html; blob `38932b0955fade0693a9b499f33a75ba7d23fdfd`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): annas-diary, notes-ecosistema, world-days, wonderlog, cooking-anime, framelab, beerclass-ai.

### UIV-001 alexruix/tame-fly-42
- Link: https://uiverse.io/alexruix/tame-fly-42
- Categoria: LOADER; evidenza: SOURCE_FILE_READ.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-001_original.html; blob `b2c97fd8dbf0f2cf49ab1dc854bc6fc84a1dd0cd`.
- Vincoli: Verifica accessibilità e licenza.
- App candidate (6): omni-cleaner, notes-ecosistema, battery-guard, send-to-pc, framelab, world-days.

### UIV-005 amir_6539/red-duck-82
- Link: https://uiverse.io/amir_6539/red-duck-82
- Categoria: CARD_BACKGROUND; evidenza: SOURCE_CODE_NOT_LOCATED.
- Codice: NON DISPONIBILE.
- Vincoli: Verifica accessibilità e licenza.
- App candidate (8): annas-diary, omni-cleaner, notes-ecosistema, cashmate-ai, focussense, battery-guard, deskland-android, app-factory-dashboard.

### UIV-049 andrew-demchenk0/honest-stingray-90
- Link: https://uiverse.io/andrew-demchenk0/honest-stingray-90
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-049_original.html; blob `363e1cf715b671b7d0f99f2304cd48f53171babe`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): 180flipcharge, annas-diary, notes-ecosistema, pocket-guard, phone-guard, easy-debloat, battery-guard.

### UIV-050 andrew-manzyk/fast-vampirebat-53
- Link: https://uiverse.io/andrew-manzyk/fast-vampirebat-53
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): sleepmax-coach, focussense, deskland-android, omni-cleaner, notes-ecosistema, framelab, world-days.

### UIV-051 andrew-manzyk/young-walrus-64
- Link: https://uiverse.io/andrew-manzyk/young-walrus-64
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-007 arthur_6104/orange-walrus-50
- Link: https://uiverse.io/arthur_6104/orange-walrus-50
- Categoria: LOADER; evidenza: SOURCE_CODE_NOT_LOCATED.
- Codice: NON DISPONIBILE.
- Vincoli: Verifica accessibilità e licenza.
- App candidate (8): notes-ecosistema, omni-cleaner, framelab, app-factory-dashboard, cashmate-ai, world-days, web-utility-factory, annas-diary.

### UIV-052 ashif_6672/rare-bat-68
- Link: https://uiverse.io/ashif_6672/rare-bat-68
- Categoria: UNKNOWN; evidenza: PAGE_LINK_FROM_AUTH_EXPORT_CATEGORY_NOT_VERIFIED.
- Codice: NON DISPONIBILE.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (3): notes-ecosistema, world-days, omni-cleaner.

### UIV-053 barisdogansutcu/plastic-dolphin-67
- Link: https://uiverse.io/barisdogansutcu/plastic-dolphin-67
- Categoria: TOOLTIP; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-053_original.html; blob `ac68771909167b2bb07675128055b26b2b625ae2`.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (6): edu-01-corpo-umano, battery-guard, wonderlog, app-factory-dashboard, omni-cleaner, notes-ecosistema.

### UIV-054 byllzz/great-wombat-13
- Link: https://uiverse.io/byllzz/great-wombat-13
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): wonderlog, cooking-anime, framelab, beerclass-ai, cashmate-ai, app-factory-dashboard, notes-ecosistema.

### UIV-055 chase2k25/modern-stingray-54
- Link: https://uiverse.io/chase2k25/modern-stingray-54
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-056 chase2k25/warm-chicken-23
- Link: https://uiverse.io/chase2k25/warm-chicken-23
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): camperboss, edu-01-corpo-umano, deskland-android, annas-diary, notes-ecosistema, world-days, wonderlog.

### UIV-057 cohencoo/dry-rat-94
- Link: https://uiverse.io/cohencoo/dry-rat-94
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-057_original.html; blob `0a5760717133c5c5a99bd69cca51da1a1344eaeb`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): app-factory-dashboard, easy-debloat, cashmate-ai, camperboss, wonderlog, cooking-anime, trailpath.

### UIV-058 cssbuttons-io/mean-dolphin-24
- Link: https://uiverse.io/cssbuttons-io/mean-dolphin-24
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-058_original.html; blob `059cab0c1c8c318b5fa9e34c4cfc9e992f027f69`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): notes-ecosistema, pocket-guard, phone-guard, easy-debloat, sleepmax-coach, camperboss, battery-guard.

### UIV-059 cuzpq/gentle-goat-72
- Link: https://uiverse.io/cuzpq/gentle-goat-72
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-059_original.html; blob `6490b825b36be2b810fa75fd8ffed9623e2b5375`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): easy-debloat, sleepmax-coach, camperboss, the-luminous-infinite-circle, tabletop-motion-alarm, cashmate-ai, battery-guard.

### UIV-060 dexter-st/breezy-zebra-94
- Link: https://uiverse.io/dexter-st/breezy-zebra-94
- Categoria: BUTTON; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Touch+keyboard, feedback e focus; nessuna CTA senza azione reale.
- App candidate (6): annas-diary, notes-ecosistema, wonderlog, world-days, cooking-anime, framelab.

### UIV-061 dexter-st/bright-lizard-8
- Link: https://uiverse.io/dexter-st/bright-lizard-8
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): world-days, send-to-pc, battery-guard, app-factory-dashboard, easy-debloat, cashmate-ai, omni-cleaner.

### UIV-062 dexter-st/spicy-otter-30
- Link: https://uiverse.io/dexter-st/spicy-otter-30
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): app-factory-dashboard, easy-debloat, cashmate-ai, camperboss, wonderlog, cooking-anime, omni-cleaner.

### UIV-063 dexter-st/tough-falcon-78
- Link: https://uiverse.io/dexter-st/tough-falcon-78
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): beerclass-ai, cashmate-ai, app-factory-dashboard, camperboss, edu-01-corpo-umano, deskland-android, notes-ecosistema.

### UIV-064 dopekid_9309/tiny-dog-80
- Link: https://uiverse.io/dopekid_9309/tiny-dog-80
- Categoria: UNKNOWN; evidenza: PAGE_LINK_FROM_AUTH_EXPORT_CATEGORY_NOT_VERIFIED.
- Codice: NON DISPONIBILE.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (3): notes-ecosistema, world-days, omni-cleaner.

### UIV-065 dovatgabriel/massive-vampirebat-17
- Link: https://uiverse.io/dovatgabriel/massive-vampirebat-17
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-066 elijahgummer/polite-earwig-72
- Link: https://uiverse.io/elijahgummer/polite-earwig-72
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): world-days, send-to-pc, battery-guard, app-factory-dashboard, easy-debloat, cashmate-ai, omni-cleaner.

### UIV-067 elijahgummer/young-horse-7
- Link: https://uiverse.io/elijahgummer/young-horse-7
- Categoria: RADIO; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Stato effettivo, semantica e dimensione touch.
- App candidate (6): web-utility-factory, sleepmax-coach, beerclass-ai, annas-diary, notes-ecosistema, cashmate-ai.

### UIV-009 eslam-hany/selfish-bobcat-73
- Link: https://uiverse.io/eslam-hany/selfish-bobcat-73
- Categoria: BOOK_CARD; evidenza: SOURCE_FILE_READ.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html; blob `39b56b1f36760326076e7bf4fbdcd550cd6cbb8f`.
- Vincoli: Verifica accessibilità e licenza.
- App candidate (6): annas-diary, notes-ecosistema, world-days, wonderlog, cooking-anime, framelab.

### UIV-068 esraaabdel-kareem/bad-dragonfly-54
- Link: https://uiverse.io/esraaabdel-kareem/bad-dragonfly-54
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): sleepmax-coach, focussense, deskland-android, omni-cleaner, notes-ecosistema, framelab, world-days.

### UIV-069 fthisilak/bitter-termite-36
- Link: https://uiverse.io/fthisilak/bitter-termite-36
- Categoria: BUTTON; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Touch+keyboard, feedback e focus; nessuna CTA senza azione reale.
- App candidate (6): easy-debloat, web-utility-factory, app-factory-dashboard, annas-diary, notes-ecosistema, wonderlog.

### UIV-070 gagan-gv/unlucky-yak-4
- Link: https://uiverse.io/gagan-gv/unlucky-yak-4
- Categoria: CHECKBOX; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-070_original.html; blob `62b562fdd2d95acc3d55096357957fd7256621e2`.
- Vincoli: Stato effettivo, semantica e dimensione touch.
- App candidate (6): camperboss, cashmate-ai, notes-ecosistema, omni-cleaner, app-factory-dashboard, world-days.

### UIV-071 gharsh11032000/sour-vampirebat-66
- Link: https://uiverse.io/gharsh11032000/sour-vampirebat-66
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-071_original.html; blob `f15f3150cfea784f3f29597694210e03f2c10c8b`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): notes-ecosistema, pocket-guard, phone-guard, easy-debloat, sleepmax-coach, camperboss, battery-guard.

### UIV-072 gsperandio/shaggy-kangaroo-12
- Link: https://uiverse.io/gsperandio/shaggy-kangaroo-12
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-072_original.html; blob `1ca675900cf3a771940754ad0c3efb30f4f4379b`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): camperboss, wonderlog, cooking-anime, sleepmax-coach, focussense, deskland-android, omni-cleaner.

### UIV-073 ilkhoeri/thin-bobcat-83
- Link: https://uiverse.io/ilkhoeri/thin-bobcat-83
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): wonderlog, cooking-anime, framelab, beerclass-ai, cashmate-ai, app-factory-dashboard, notes-ecosistema.

### UIV-074 jeremy_4982/massive-falcon-52
- Link: https://uiverse.io/jeremy_4982/massive-falcon-52
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-075 joe-watson-sbf/honest-bullfrog-6
- Link: https://uiverse.io/joe-watson-sbf/honest-bullfrog-6
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-075_original.html; blob `d75df12bc3d2c26e7eeb7c04ff06e40052252279`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): camperboss, edu-01-corpo-umano, deskland-android, annas-diary, notes-ecosistema, world-days, wonderlog.

### UIV-076 kat_2522/rude-robin-51
- Link: https://uiverse.io/kat_2522/rude-robin-51
- Categoria: LOADER; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): app-factory-dashboard, easy-debloat, cashmate-ai, camperboss, wonderlog, cooking-anime, omni-cleaner.

### UIV-077 kennyotsu/fast-emu-70
- Link: https://uiverse.io/kennyotsu/fast-emu-70
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-077_original.html; blob `382dd91ec3e58433c7cc9f9d41ec0fc42f7c504c`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): wonderlog, cooking-anime, framelab, beerclass-ai, cashmate-ai, app-factory-dashboard, notes-ecosistema.

### UIV-078 kennyotsu/giant-sloth-18
- Link: https://uiverse.io/kennyotsu/giant-sloth-18
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): beerclass-ai, cashmate-ai, app-factory-dashboard, camperboss, edu-01-corpo-umano, deskland-android, notes-ecosistema.

### UIV-079 kennyotsu/selfish-bear-69
- Link: https://uiverse.io/kennyotsu/selfish-bear-69
- Categoria: UNKNOWN; evidenza: PAGE_LINK_FROM_AUTH_EXPORT_CATEGORY_NOT_VERIFIED.
- Codice: NON DISPONIBILE.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (3): notes-ecosistema, world-days, omni-cleaner.

### UIV-080 kennyotsu/short-ape-5
- Link: https://uiverse.io/kennyotsu/short-ape-5
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-080_original.html; blob `fd81c86a93976d8a20f48de1baca74c0853965a2`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): annas-diary, notes-ecosistema, world-days, wonderlog, cooking-anime, framelab, beerclass-ai.

### UIV-081 kennyotsu/tender-badger-21
- Link: https://uiverse.io/kennyotsu/tender-badger-21
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): wonderlog, cooking-anime, framelab, beerclass-ai, cashmate-ai, app-factory-dashboard, trailpath.

### UIV-082 kennyotsu/wise-rattlesnake-92
- Link: https://uiverse.io/kennyotsu/wise-rattlesnake-92
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-082_original.html; blob `cdaa9908d7930c29c5ede58d669cfdf7a435ecce`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): beerclass-ai, cashmate-ai, app-factory-dashboard, camperboss, edu-01-corpo-umano, deskland-android, notes-ecosistema.

### UIV-083 kennyotsu/wonderful-firefox-31
- Link: https://uiverse.io/kennyotsu/wonderful-firefox-31
- Categoria: UNKNOWN; evidenza: PAGE_LINK_FROM_AUTH_EXPORT_CATEGORY_NOT_VERIFIED.
- Codice: NON DISPONIBILE.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (3): notes-ecosistema, world-days, omni-cleaner.

### UIV-084 lukepadiachy/funny-moose-89
- Link: https://uiverse.io/lukepadiachy/funny-moose-89
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-084_original.html; blob `5da11e20c71ec3ccb35b6b2c9158bd59ee0c5348`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-085 m1her/odd-fireant-56
- Link: https://uiverse.io/m1her/odd-fireant-56
- Categoria: SWITCH; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): notes-ecosistema, pocket-guard, phone-guard, easy-debloat, sleepmax-coach, camperboss, battery-guard.

### UIV-086 mamyapro123/cuddly-warthog-66
- Link: https://uiverse.io/mamyapro123/cuddly-warthog-66
- Categoria: SWITCH; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): easy-debloat, sleepmax-coach, camperboss, the-luminous-infinite-circle, tabletop-motion-alarm, cashmate-ai, battery-guard.

### UIV-087 marcelodolza/fat-zebra-11
- Link: https://uiverse.io/marcelodolza/fat-zebra-11
- Categoria: BUTTON; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-087_original.html; blob `b193da3bdefbfc7101f484a2b1ad3b4964b40db7`.
- Vincoli: Touch+keyboard, feedback e focus; nessuna CTA senza azione reale.
- App candidate (6): camperboss, easy-debloat, web-utility-factory, app-factory-dashboard, annas-diary, notes-ecosistema.

### UIV-088 mobinkakei/great-skunk-8
- Link: https://uiverse.io/mobinkakei/great-skunk-8
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-088_original.html; blob `56a5540c5fc7d9901184edfc3bcb604d7c07dc07`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): battery-guard, focussense, omni-cleaner, 180flipcharge, annas-diary, notes-ecosistema, pocket-guard.

### UIV-089 mobinkakei/grumpy-turtle-41
- Link: https://uiverse.io/mobinkakei/grumpy-turtle-41
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-089_original.html; blob `2704a11f9a5b7a67ee5706698d793da73ff38079`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-090 mobinkakei/strong-lizard-79
- Link: https://uiverse.io/mobinkakei/strong-lizard-79
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-090_original.html; blob `17240e468825008e163efc58fefaeae1204a5439`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): pocket-guard, phone-guard, easy-debloat, sleepmax-coach, camperboss, the-luminous-infinite-circle, battery-guard.

### UIV-091 monkey_8812/curly-moth-56
- Link: https://uiverse.io/monkey_8812/curly-moth-56
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): camperboss, edu-01-corpo-umano, deskland-android, annas-diary, notes-ecosistema, world-days, wonderlog.

### UIV-092 mymiamo/quiet-dragon-5
- Link: https://uiverse.io/mymiamo/quiet-dragon-5
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): annas-diary, notes-ecosistema, world-days, wonderlog, cooking-anime, framelab, beerclass-ai.

### UIV-093 preet_7613/new-cougar-63
- Link: https://uiverse.io/preet_7613/new-cougar-63
- Categoria: UNKNOWN; evidenza: PAGE_LINK_FROM_AUTH_EXPORT_CATEGORY_NOT_VERIFIED.
- Codice: NON DISPONIBILE.
- Vincoli: Usare solo dopo verifica visuale, a11y e codice.
- App candidate (3): omni-cleaner, app-factory-dashboard, notes-ecosistema.

### UIV-094 satyamchaudharydev/splendid-husky-54
- Link: https://uiverse.io/satyamchaudharydev/splendid-husky-54
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-094_original.html; blob `112071ace5d9cb34849313300882195ff816c52d`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-095 seoulchik/funny-seahorse-89
- Link: https://uiverse.io/seoulchik/funny-seahorse-89
- Categoria: CARD; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): camperboss, edu-01-corpo-umano, deskland-android, annas-diary, notes-ecosistema, world-days, wonderlog.

### UIV-096 solowzrd/wet-lionfish-63
- Link: https://uiverse.io/solowzrd/wet-lionfish-63
- Categoria: PATTERN; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contrasto, leggibilità, batterie/GPU e sfondo statico ridotto.
- App candidate (6): battery-guard, app-factory-dashboard, web-utility-factory, omni-cleaner, deskland-android, focussense.

### UIV-097 vamsidevendrakumar/soft-shrimp-94
- Link: https://uiverse.io/vamsidevendrakumar/soft-shrimp-94
- Categoria: CARD; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-097_original.html; blob `053573c3c481c3ebe13cdbde46f415e2b8a89e9b`.
- Vincoli: Contenuti leggibili senza hover; touch/focus, immagini originali e safe area.
- App candidate (7): wonderlog, cooking-anime, framelab, beerclass-ai, cashmate-ai, app-factory-dashboard, notes-ecosistema.

### UIV-098 whoisyourdeadie/foolish-rabbit-13
- Link: https://uiverse.io/whoisyourdeadie/foolish-rabbit-13
- Categoria: PATTERN; evidenza: PUBLIC_UIVERSE_CATEGORY_VERIFIED_SOURCE_CODE_MISSING.
- Codice: NON DISPONIBILE.
- Vincoli: Contrasto, leggibilità, batterie/GPU e sfondo statico ridotto.
- App candidate (6): cashmate-ai, notes-ecosistema, annas-diary, world-days, battery-guard, deskland-android.

### UIV-099 xXJollyHAKERXx/lucky-falcon-75
- Link: https://uiverse.io/xXJollyHAKERXx/lucky-falcon-75
- Categoria: LOADER; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-099_original.html; blob `7251e090e8398d62610a883e70c0426780631557`.
- Vincoli: Solo durante operazione realmente avviata; stop/timeout/error/retry e reduced-motion.
- App candidate (7): omni-cleaner, notes-ecosistema, framelab, world-days, send-to-pc, battery-guard, app-factory-dashboard.

### UIV-100 zanina-yassine/afraid-eel-50
- Link: https://uiverse.io/zanina-yassine/afraid-eel-50
- Categoria: SWITCH; evidenza: SOURCE_FILE_LOCATED_BLOB_PINNED_AND_SNAPSHOT_SAVED.
- Codice: UI-UX/UIVERSE/CODICE_SORGENTE/UIV-100_original.html; blob `0912f31f0eff6995ef91fc5e6c8fa5103db93b60`.
- Vincoli: On/off deve rappresentare stato reale, persistent state e TalkBack.
- App candidate (7): easy-debloat, sleepmax-coach, camperboss, the-luminous-infinite-circle, tabletop-motion-alarm, cashmate-ai, battery-guard.

## QA statica dei 57 codici originali

[Report dettagliato](../UI-UX/UIVERSE/FAVORITES/ANALISI_TECNICA_57.md). Sorgenti letti e verificati contro blob Git; 35 con keyframes e 16 con hover. Questo non equivale a esecuzione/QA su dispositivo. Ogni segnalazione statica rimane un rischio da verificare.

