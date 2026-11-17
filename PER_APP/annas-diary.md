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
