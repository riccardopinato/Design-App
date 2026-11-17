# Cooking Anime — Dossier Design-App

**Registro permanente:** `PER_APP/cooking-anime.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Identità image-first culinaria anime, con accenti kawaii controllati. Core UI leggibile, motivi illustrati per categorie e stati speciali. Distinguere coerentemente cucina giapponese, cinese e altri contesti senza stereotipi.

**Categorie da studiare:** kawaii-gattini · food-japan · food-china · anime-seasonal · ui-standard.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. Home con motivo brand (mascotte, ciotola o sakura).
2. Ricette con icona ricettario/bento e fotografia prioritaria.
3. Categorie con sushi, ramen, onigiri, dumpling o bao coerenti con ricetta.
4. Preferiti con cuore o stella leggibile.
5. Profilo con avatar gatto opzionale.
6. Sfide/collezioni/achievement soltanto se le funzioni esistono.
7. Empty state di ricerca o raccolta con gattino chef.
8. Loading con vapore della ciotola, solo durante vera attesa.
9. Salvataggio e ricetta completata con sparkle/check dopo conferma.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-009 · video](https://gentleface.com/icons/video) | MEDIUM | contenuti video dove disponibili | VERIFIED_DETAIL |
| [ICO-012 · apps-sparkle](https://gentleface.com/icons/apps-sparkle) | MEDIUM | novità editoriali senza claim AI | VERIFIED_DETAIL |
| [ICO-019 · star](https://gentleface.com/icons/star) | MEDIUM | ricette favorite | VERIFIED_SITE |
| [ICO-020 · play](https://gentleface.com/icons/play) | MEDIUM | riproduzione video ricetta | VERIFIED_SITE |
| [ICO-021 · pause](https://gentleface.com/icons/pause) | MEDIUM | pausa tutorial | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `kawaii-cat-chef`, `sushi`, `ramen`, `onigiri`, `bento`, `chopsticks`, `sakura`.

## Catalogo tematico Cooking Anime (NON sorgenti verificate)

I seguenti 36 concetti provengono dalla richiesta dell'utente e dai suggerimenti in chat del 17/11/2026. Non sono presentati come icone disponibili in Gentleface né come asset già licenziati: lo stato è `DESIGN_IDEA`, provider `NOT_SELECTED`.

| Categoria | Concept | Destinazioni | Motion | Disponibilità |
|---|---|---|---|---|
| kawaii-gattini | Mascotte gattino con cappello da chef (`CAI-gattino-chef`) | home, empty-state, onboarding | STATIC_OR_BRIEF_ON_CONFIRMED_EVENT | da cercare/verificare |
| kawaii-gattini | Testolina di gattino (`CAI-testolina-gatto`) | profilo, stato-personalizzato | STATIC | da cercare/verificare |
| kawaii-gattini | Zampetta (`CAI-zampetta`) | badge, collezione, progresso | ON_CONFIRMED_EVENT | da cercare/verificare |
| kawaii-gattini | Faccina kawaii (`CAI-faccina-kawaii`) | feedback, empty-state | ON_CONFIRMED_EVENT | da cercare/verificare |
| kawaii-gattini | Avatar gattino (`CAI-gattino-avatar`) | profilo, personalizzazione | STATIC | da cercare/verificare |
| food-japan | Sushi (`CAI-sushi`) | categorie, suggerimenti | ON_SELECT | da cercare/verificare |
| food-japan | Ciotola di ramen con vapore (`CAI-ramen`) | categorie, loading | ONLY_LOADING_VISIBLE | da cercare/verificare |
| food-japan | Onigiri (`CAI-onigiri`) | categorie, tag | ON_SELECT | da cercare/verificare |
| food-japan | Bento box (`CAI-bento`) | ricette, categorie | STATIC | da cercare/verificare |
| food-japan | Bacchette (`CAI-bacchette`) | categoria, ricetta | STATIC | da cercare/verificare |
| food-japan | Teiera (`CAI-teiera`) | bevande, categorie | STATIC | da cercare/verificare |
| food-japan | Ciotola di riso (`CAI-riso`) | ingredienti, tag | STATIC | da cercare/verificare |
| food-japan | Pesce (`CAI-pesce`) | ingredienti, tag | STATIC | da cercare/verificare |
| food-japan | Dolcetto/mochi (`CAI-mochi-dessert`) | dessert, categorie | STATIC | da cercare/verificare |
| food-china | Ravioli cinesi jiaozi (`CAI-jiaozi-dumplings`) | categoria-cucina-cinese | STATIC | da cercare/verificare |
| food-china | Bao al vapore (`CAI-bao`) | categoria-cucina-cinese | STATIC | da cercare/verificare |
| food-china | Wok (`CAI-wok`) | preparazioni-cinesi | STATIC | da cercare/verificare |
| food-china | Cestello a vapore in bambù (`CAI-cestello-bambu`) | tecniche-cottura | STATIC | da cercare/verificare |
| food-china | Tazza da tè cinese (`CAI-te-cinese`) | bevande | STATIC | da cercare/verificare |
| anime-seasonal | Fiore di sakura (`CAI-sakura`) | sezioni, ricorrenze-stagionali | STATIC | da cercare/verificare |
| anime-seasonal | Torii (`CAI-torii`) | contenuti-situati-in-giappone | STATIC | da cercare/verificare |
| anime-seasonal | Lanterna (`CAI-lanterna`) | contenuti-culturali-coerenti | STATIC | da cercare/verificare |
| anime-seasonal | Ventaglio (`CAI-ventaglio`) | decorazione-contestuale | STATIC | da cercare/verificare |
| anime-seasonal | Nuvola stilizzata (`CAI-nuvola-stilizzata`) | header, empty-state | STATIC | da cercare/verificare |
| anime-seasonal | Stellina/sparkle (`CAI-sparkle`) | successo, badge, preferiti | ON_CONFIRMED_EVENT | da cercare/verificare |
| ui-standard | Casetta semplice (`CAI-home`) | navigazione-principale | STATIC | da cercare/verificare |
| ui-standard | Libro ricette (`CAI-ricettario`) | navigazione-ricette | STATIC | da cercare/verificare |
| ui-standard | Griglia categorie (`CAI-categorie`) | navigazione-categorie | STATIC | da cercare/verificare |
| ui-standard | Cuore preferito (`CAI-cuore`) | preferiti | ON_CONFIRMED_TOGGLE | da cercare/verificare |
| ui-standard | Lente ricerca (`CAI-search`) | ricerca | STATIC | da cercare/verificare |
| ui-standard | Ingranaggio impostazioni (`CAI-settings`) | impostazioni | STATIC | da cercare/verificare |
| ui-standard | Condividi (`CAI-share`) | condivisione | STATIC | da cercare/verificare |
| ui-standard | Modifica (`CAI-edit`) | editor-ricette-se-presente | STATIC | da cercare/verificare |
| ui-standard | Elimina (`CAI-delete`) | rimozione-con-conferma | STATIC | da cercare/verificare |
| ui-standard | Profilo (`CAI-profile`) | profilo | STATIC | da cercare/verificare |
| ui-standard | Conferma (`CAI-check`) | salvataggio, reazione | ON_CONFIRMED_EVENT | da cercare/verificare |

**Direzione consigliata**: un unico illustratore/pack vettoriale per icone kawaii, gastronomiche e decorative; non confondere giapponese/cinese. Per le azioni principali restano icone standard (lente, impostazioni, modifica, cestino, condividi) con priorità alla leggibilità. L'atmosfera anime non implica il riuso di marchi/personaggi protetti.

## Animazioni e feedback proposti

- cuore o stella con transizione discreta alla conferma preferito.
- vapore ramen o ciotola solo in caricamento visibile.
- gattino chef felice dopo completamento ricetta confermato.
- nessun loop perpetuo su listati ricette.

## Cosa evitare

- sostituire Cerca, Modifica, Elimina, Condividi o Impostazioni con simboli difficili da capire.
- mescolare emoji, outline, 3D, flat e pixel art senza un'unica grammatica.
- associare cibo cinese a simboli giapponesi o viceversa indiscriminatamente.
- usare bandiere o torii come sinonimo generico di 'Asia'.
- replicare personaggi o loghi anime protetti.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | MEDIUM | image-first editorial cards |
| DSK-003 — Taste Skill | HIGH | product/store marketing website |
| DSK-005 — Vercel Web Design Guidelines | MEDIUM | marketing and public site only |
| DSK-006 — Anthropic Frontend Design | HIGH | image-first culinary identity |
| DSK-007 — Hallmark | HIGH | public product marketing and themed campaign |
| DSK-009 — UI UX Pro Max | HIGH | image-first catalogue design |
| DSK-010 — Stageshow | HIGH | app store promotional cards |

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

- **Idea:** Appunti vocali personali durante una ricetta.
- **Collocazione candidata:** Dettaglio ricetta, non overlay costante.
- **Adattamento estetico:** anime/kawaii senza distrarre dalla ricetta.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.
