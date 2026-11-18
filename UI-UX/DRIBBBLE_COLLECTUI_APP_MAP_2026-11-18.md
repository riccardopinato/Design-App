# Dribbble + Collect UI — matrice app ↔ pattern, 18/11/2026

Stato: **PROPOSED_ONLY**. Scoperta e idee, NON approvazione di nuovi scope o componenti implementati. Vedere [audit e fonti](../sources/DRIBBBLE_COLLECTUI_RESEARCH_2026-11-18.md) e [JSON](./DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.json).

| App | Pattern | Dove applicarli | Fit | Guardrail |
|---|---|---|---|---|
| [Anna's Diary](../PER_APP/annas-diary.md) | DCL-001 · DCL-002 · DCL-004 · DCL-006 · DCL-007 · DCL-011 | Oggi, Calendario, Ricordi | HIGH | Preservare Manrope/Lora, palette rose, look diario contemporaneo |
| [Notes-Ecosistema](../PER_APP/notes-ecosistema.md) | DCL-002 · DCL-004 · DCL-007 · DCL-010 · DCL-011 | Workspace, Inbox, Canvas, Web | HIGH | Densità da workspace, niente dashboard scenografica senza funzione |
| [Android Omni Cleaner](../PER_APP/omni-cleaner.md) | DCL-002 · DCL-004 · DCL-005 · DCL-006 · DCL-007 | Home funzioni, scansione, galleria e player | HIGH | No micro-animazioni nelle operazioni distruttive; foto/video a proporzioni originali |
| [World Days](../PER_APP/world-days.md) | DCL-001 · DCL-003 · DCL-007 · DCL-011 | Schede giornata e scoperta | HIGH | Preservare colori già approvati, storia e fonti sopra il puro decorativo |
| [Battery Guard](../PER_APP/battery-guard.md) | DCL-003 · DCL-005 · DCL-008 · DCL-011 | Stato batteria, sessioni e grafici | HIGH | Grafici reali; overhead GPU e consumo prossimi a zero |
| [CashMate AI](../PER_APP/cashmate-ai.md) | DCL-002 · DCL-003 · DCL-005 · DCL-007 | Saldo, spese, budget, dettagli | HIGH | Privacy, accuratezza valori, niente false metriche |
| [Wonderlog](../PER_APP/wonderlog.md) | DCL-001 · DCL-006 · DCL-007 · DCL-010 | Viaggi, diari, foto e mappa | HIGH | No immagini tagliate; viaggio e navigazione non sacrificati |
| [FrameLab](../PER_APP/framelab.md) | DCL-001 · DCL-006 · DCL-010 · DCL-012 | Portfolio, foto, palette | HIGH | Foto contenuto primario; controlli cromatici precisi |
| [FocusSense](../PER_APP/focussense.md) | DCL-003 · DCL-005 · DCL-008 | Sessioni e Focus Score | MEDIUM | No colori o dati che suggeriscono misure non verificate |
| [CamperBoss](../PER_APP/camperboss.md) | DCL-002 · DCL-004 · DCL-007 · DCL-010 | Dashboard viaggio, controlli | MEDIUM | Offline e leggibilità in esterno prioritari |
| [TrailPath](../PER_APP/trailpath.md) | DCL-001 · DCL-005 · DCL-007 | Mappa, percorso, statistiche | MEDIUM | Routing e posizione corretti prima del polish |
| [SleepMax Coach](../PER_APP/sleepmax-coach.md) | DCL-003 · DCL-005 · DCL-009 | Sonno, routine e onboarding | MEDIUM | Evita affermazioni cliniche con grafici ornamentali |
| [BeerClass AI](../PER_APP/beerclass-ai.md) | DCL-001 · DCL-002 · DCL-006 | Diario birre e rapid log | MEDIUM | Rapid Log più importante delle immagini |
| [Deskland Android](../PER_APP/deskland-android.md) | DCL-004 · DCL-008 · DCL-012 | Home launcher e transizioni | LOW | Prima rendere launcher affidabile e fluido |
| [App Factory Dashboard](../PER_APP/app-factory-dashboard.md) | DCL-002 · DCL-005 · DCL-010 | Portfolio, roadmap, stato e gate | HIGH | Separare implementato, verificato e roadmap; non simulare CI |

## Mappatura inversa (pattern → app)

- **DCL-001**: Anna's Diary · World Days · Wonderlog · FrameLab · TrailPath · BeerClass AI
- **DCL-002**: Anna's Diary · Notes-Ecosistema · Android Omni Cleaner · CashMate AI · CamperBoss · BeerClass AI · App Factory Dashboard
- **DCL-003**: World Days · Battery Guard · CashMate AI · FocusSense · SleepMax Coach
- **DCL-004**: Anna's Diary · Notes-Ecosistema · Android Omni Cleaner · CamperBoss · Deskland Android
- **DCL-005**: Android Omni Cleaner · Battery Guard · CashMate AI · FocusSense · TrailPath · SleepMax Coach · App Factory Dashboard
- **DCL-006**: Anna's Diary · Android Omni Cleaner · Wonderlog · FrameLab · BeerClass AI
- **DCL-007**: Anna's Diary · Notes-Ecosistema · Android Omni Cleaner · World Days · CashMate AI · Wonderlog · CamperBoss · TrailPath
- **DCL-008**: Battery Guard · FocusSense · Deskland Android
- **DCL-009**: SleepMax Coach
- **DCL-010**: Notes-Ecosistema · Wonderlog · FrameLab · CamperBoss · App Factory Dashboard
- **DCL-011**: Anna's Diary · Notes-Ecosistema · World Days · Battery Guard
- **DCL-012**: FrameLab · Deskland Android

Le stesse fonti possono ispirare più app; i singoli pattern possono associarsi a più stili senza duplicare asset. Mappature valide soltanto dopo verifica delle Product Bible.
