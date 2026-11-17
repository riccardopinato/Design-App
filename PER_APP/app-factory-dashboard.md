# App Factory Dashboard — Dossier Design-App

**Registro permanente:** `PER_APP/app-factory-dashboard.md` · [Indice](./README.md) · [Profilo JSON](./REGISTRO_APP_DESIGN.json) · [Matrice icone](../ICONE/MATRICE_APP_ICONE.md) · [Fonti di design](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md)

**Stato delle proposte:** `PROPOSAL_ONLY` — non sono stati ispezionati il codice HEAD o la Product Bible della singola app in questo lavoro. Le scelte visive già approvate nei repository delle app prevalgono; nessun asset copiato, nessun test consumer, nessuna integrazione.

## Identità e direzione visiva

Pannello operativo tecnico: densità controllata, bento strutturato, badge semantici e qualità visiva verificabile.

**Categorie da studiare:** repository e branch · capability/Golden · CI e build · priorità.

## Superfici consigliate (proposte condizionate all'esistenza della funzione)

1. stato CI/PR/merge.
2. ricerca repository e capability.
3. schede progetti e dipendenze.

## Riferimenti di icone da catalogo Gentleface

| Icona ufficiale | Fit | Impiego proposto | Evidenza animazione |
|---|---|---|---|
| [ICO-011 · search](https://gentleface.com/icons/search) | HIGH | ricerca repository e capability | VERIFIED_DETAIL |
| [ICO-012 · apps-sparkle](https://gentleface.com/icons/apps-sparkle) | MEDIUM | scoperta capability | VERIFIED_DETAIL |
| [ICO-014 · check](https://gentleface.com/icons/check) | HIGH | job realmente verificato | VERIFIED_SITE |
| [ICO-018 · gauge](https://gentleface.com/icons/gauge) | HIGH | stato CI/portfolio | VERIFIED_SITE |

**Concetti da cercare o disegnare, senza fornitore assegnato:** `check`, `search`, `gauge`.

## Animazioni e feedback proposti

- conferma job solo dopo risposta GitHub.
- caricamento soltanto durante richieste effettive.

## Cosa evitare

- animazioni che fanno apparire eseguiti task non avvenuti.
- mini-illustrazioni che nascondono lo stato.

## Skill / fonti di design associate

| Fonte | Fit | Utilizzo |
|---|---|---|
| DSK-001 — Anti UI Slop / Uizze | HIGH | consistent design language and preview QA |
| DSK-002 — Impeccable | HIGH | cross-app visual acceptance gate |
| DSK-003 — Taste Skill | HIGH | web landing and narrative hero |
| DSK-005 — Vercel Web Design Guidelines | HIGH | keyboard navigation, responsive dashboards and forms |
| DSK-006 — Anthropic Frontend Design | MEDIUM | non-generic web dashboard identity |
| DSK-007 — Hallmark | MEDIUM | public project showcase, not operations UI |
| DSK-008 — Better Interfaces (Jakub Krehel) | HIGH | responsive dashboard QA |
| DSK-009 — UI UX Pro Max | HIGH | cross-product visual catalog |
| DSK-010 — Stageshow | HIGH | portfolio project teasers |

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

- **Idea:** Cattura vocale di idee o note di progetto.
- **Collocazione candidata:** Composer idea/nota.
- **Adattamento estetico:** UI tecnica e leggibile.
- **Stato:** `PROPOSED_ONLY` · `NOT_IMPLEMENTED`; Product Bible e feature voice non approvate da questa registrazione.
- **Comportamento:** sfera attiva solo durante vero audio con permesso microfono e registratore funzionante; pausa su sfondo, errori e reduced-motion, fallback microfono statico, durata e comandi accessibili.
- **Vincolo:** l'orb non registra, trascrive o salva; nessuna libreria Web/React Native viene installata automaticamente in Flutter/Compose.
- **Storico 17/11/2026:** idea salvata in `PER_APP/REGISTRO_APP_DESIGN.json` sotto `voice_ui_candidates`; fonte utente, non implementazione.
