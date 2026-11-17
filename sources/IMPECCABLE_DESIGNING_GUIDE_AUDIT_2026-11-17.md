# Impeccable — Designing: analisi incrementale App Factory (17/11/2026)

**Pagina esatta esaminata:** https://impeccable.style/designing/ · integrazioni ufficiali https://impeccable.style/docs/, https://impeccable.style/slop/, https://impeccable.style/docs/detector/, https://impeccable.style/docs/hooks/.

**Il repository/skill è GIÀ CENSITO** come `DSK-002`, `pbakaus/impeccable@d41d9860b0094dcb68030657da63461212835aaa`, Apache-2.0 nella [prima ricognizione](./ANTI_SLOP_DESIGN_SKILLS_AUDIT_2026-11-17.md) e [matrice preesistente](../UI-UX/MATRICE_REPO_DESIGN_APP_2026-11-17.md). Nessuna nuova sorgente OSS, donor, Golden o skill installata. La pagina corrente può avere documentazione più nuova del commit GitHub già fissato; **non assumere equivalenza di versione del runtime**.

## Principi verificati nella guida ufficiale

- Quattro fasi **Start → Improve → Check → Maintain**, con comandi `init` / `document` / `shape`, `critique` / `layout` / `typeset` / `colorize` / `generate`, `audit` / `clarify` / `harden` / `polish`, `extract` / `document` / `hooks`.
- **Mockup-first** offre più libertà espressiva, ma l'implementazione non riproduce automaticamente tutti i dettagli; **code-first** tende a un primo risultato coerente, meno ambizioso. Scegliere caso per caso e valutare il risultato renderizzato.
- `PRODUCT.md` conserva destinatari, funzione e vincoli e `DESIGN.md` documenta un sistema visivo (palette, font, tipografia, forme, componenti). Nel nostro progetto la **Product Bible resta canonica**: `DESIGN.md` deve essere una *vista derivata e verificata* delle decisioni, senza inventare un secondo product owner.
- Quattro modi d'uso **Persuade / Operate / Read / Experience**. Per utility e dashboard conta la precisione **Operate**; per World Days prevale **Read**; per Ricordi, Wonderlog e gallery serve **Experience**, pur mantenendo funzioni Operate.
- Evitare il conflitto fra più skill di design sovrapposte. Impeccable è un *review/quality playbook* `DSK-002`, non sostituisce le Golden Rules M3 o Shell, né diventa automaticamente componente runtime.

## Rischi concreti e suggerimenti dal catalogo anti-slop

Riferimento https://impeccable.style/slop/. Il catalogo elenca anti-pattern, NON regole universalmente vietate. Si valuta intenzione e Product Bible.

| Pattern ufficiale | Applicazione App Factory |
|---|---|
| Card annidate senza motivo | Semplificare Home di Anna e Omni Cleaner, usare separatori e titoli prima di nuove card |
| Abuso di modali | Aprire funzioni Omni Cleaner su schermate dedicate quando il flusso è complesso |
| Testo minuscolo, gerarchia piatta, contrasto insufficiente | Fissare tipografia/sfondo in token e testare su font grande + tema scuro |
| Animare tutto: status dot pulsante, decorazioni e marquee | Collegare animazioni a stati veri, evitare GPU continua e loader di progresso fittizi |
| Gradient text generico, glow/colori default | Distinguere i link a Text Gradient dalla decisione di usarlo: non imporlo al brand |
| Schede tutte identiche o scrollers che tagliano i bordi | Riconoscere blocchi funzionali diversi, spaziature e caroselli senza crop |
| UI copy ripetitiva/ambigua | Titolo, CTA, spiegazione, errori e vuoto devono avere uno scopo diverso, senza duplicare informazioni |

## 8 controlli riutilizzabili proposti

1. **Product & design context** (`init/document`): Product Bible canonica, snapshot DESIGN.md derivato e versionato, font/colore/token; mai secondo proprietario dei requisiti.
2. **Direction before code** (`shape + mockup-first vs code-first`): Obiettivo, target utenti, modo Operate/Read/Experience, confronto massimo 2-3 alternative se serve; nessun design implementato per implicazione.
3. **Human critique** (`critique`): Revisione gerarchia, densità, leggibilità, omogeneità e flussi con screenshot aggiornati: report e priorità, nessuna mutazione automatica senza approvazione.
4. **Technical audit** (`audit`): Focus/semantics, touch 48dp, font scale, responsive, insets, dark/light/system, performance e overlay.
5. **Resilient states** (`clarify + harden`): Loading/empty/error/offline/timeout/sync/account switch, testo UI e recupero da errore, date/locale, senza inventare stati.
6. **Visual finishing** (`layout + typeset + colorize + polish`): Spaziatura e gerarchia, font e palette già approvati, componenti non ripetuti inutilmente, motion solo semanticamente utile.
7. **Design-token reuse** (`extract + document`): Donor/Golden esistenti prima della nuova libreria; consolidare comportamenti identici, non solo superfici esteticamente simili.
8. **Automated checks with platform split** (`detect/hooks`): CLI/hook solo HTML/CSS/Web e CI Web; Flutter/Android richiedono screenshot, device, TalkBack, test e report separati.

## Riferimento vs runtime realmente utilizzabile

**Deterministic CLI e hook:** la guida del detector precisa che `npx impeccable detect` analizza CSS, HTML e fonti Web, comprese pagine renderizzate, con `--json`; non analizza il codice nativo Android/iOS. La documentazione hook ribadisce che **non viene eseguito** per prodotti marcati `ios`, `android` o `adaptive`. Codex richiede installazione e approvazione esplicita. Non è stato eseguito nessuno di questi strumenti in questo intake. I check possono essere sperimentati **solo per frontend Web/PWA** e con consenso alle nuove dipendenze; non promuovere PASS Flutter da detector web.

**Flutter:** usare Golden [Theme M3](https://github.com/riccardopinato/App-Factory-Core/blob/c5adc147046beb7024629466d10eeb799c3c2619/golden/ui/GOLDEN_THEME_M3_FLUTTER_v1.txt) già COPY-READY per token/tema/touch 48dp; usare Golden [App Shell & Visual QA](https://github.com/riccardopinato/App-Factory-Core/blob/c5adc147046beb7024629466d10eeb799c3c2619/golden/ui/GOLDEN_APP_SHELL_RESPONSIVE_VISUAL_QA_FLUTTER_v1_DRAFT.txt) come matrice *DRAFT*, non come certificazione. Native test: piccolo telefono, grande telefono, dark/light/system, font grande, tastiera, safe-area, loading/empty/error/offline, localizzazioni, screenshot e TalkBack, incluso consumo/motion.

**Policy anti-slop:** non standardizzare lo stesso layout per tutte le app. Il principio centrale è una coerenza *interna* a ciascun prodotto, non un'identità App Factory uniforme. Raffinamento estetico non autorizza modifica della Product Bible, cancellazione dati, deploy e nuove capability.

## Applicabilità già esistente — 10 app (senza duplicare 10 relazioni)

| App | Fit esistente | Priorità proposta | Modo | Focus |
|---|---|---|---|---|
| Anna's Diary | HIGH | P1 | OPERATE+EXPERIENCE | Oggi, Calendario, Ricordi, Impostazioni |
| Notes-Ecosistema | HIGH | P1 | OPERATE | Editor, canvas, ricerca, Smart Inbox |
| Omni Cleaner | HIGH | P1 | OPERATE | Home, schede funzione dedicate, galleria, player |
| World Days | HIGH | P1 | READ+OPERATE | Elenco ricorrenze, dettaglio storia, ricerca |
| Battery Guard | HIGH | P2 | OPERATE | Dashboard batteria e diagnostica |
| App Factory Dashboard | HIGH | P1 | OPERATE | Progetti, Golden, donor, blocchi, roadmap |
| FrameLab | HIGH | P2 | OPERATE+EXPERIENCE | Editor media, galleria, pannelli di controllo |
| Wonderlog | MEDIUM | P2 | EXPERIENCE+OPERATE | Diario viaggio, luoghi, mappa |
| CashMate AI | MEDIUM | P2 | OPERATE | Transazioni, grafici, filtri e budget |
| Deskland Android | MEDIUM | P2 | OPERATE+EXPERIENCE | Launcher, scene e overlay |

**Stato:** solo documentazione e suggerimenti. Nessuna app sottoposta a screenshot review reale, nessun componente/feature installato, nessun nuovo Golden o donor certificato, nessuna esecuzione di CLI/hook.

[Specifiche per le 10 app](../UI-UX/IMPECCABLE_DESIGNING_APP_MATRIX_2026-11-17.json).
