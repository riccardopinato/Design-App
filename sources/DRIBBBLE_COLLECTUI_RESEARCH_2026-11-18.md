# Dribbble + Collect UI — Design Research 2026/27
Data audit: 2026-11-18 · Stato: REFERENCE / PROPOSED_ONLY · Nessuna app consumer modificata

## Obiettivo
Sostituire il look predefinito e intercambiabile delle app con un linguaggio **product-owned**, elegante, pulito, fresco, veloce e leggibile. Flutter rimane lo stack mobile; la libreria visiva non impone un tema di framework. Catalogazione di idee visive, NON import di sorgenti o media.

## Fonti effettivamente ispezionate
| Rif. | URL preciso | Evidenza osservabile | Pattern deducibile |
|---|---|---|---|
| DRB-01 | https://dribbble.com/shots/25718292-Simple-Bento-Boxes | Bento a griglia con card eterogenee, timer, tracciamento e accenti blu/turchese | Bento con card-hero e CTA contestuale |
| DRB-02 | https://dribbble.com/shots/25275167-Inbox | Schermata mobile con tipografia grande, dati urgenti, blocchi colorati e card contestuali | Gerarchia primaria forte, dashboard più scansionabile |
| DRB-03 | https://dribbble.com/shots/26474699-Bento-grid-exploration | Fotografia dominante e formati di tile differenti con caption brevi | Storytelling visivo e memoria fotografica |
| DRB-04 | https://dribbble.com/shots/26994755-Articles-App-Concept | UI editoriale mobile con fotografia immersiva, categorie contenute e interfaccia dark | Hero fotografico e contenuto-first |
| CUI-01 | https://collectui.com/designs/sign-up-ui-design-inspiration | Raccolta di onboarding/sign-up e form mobile | Revisione dei first-run e composizione form |
| CUI-02 | https://collectui.com/designs/scroll-animation-ui-design-inspiration | Raccolta di scroll transition, reveal e progress bar mobili | Motion legato allo stato di scroll |
| CUI-03 | https://collectui.com/designs/infographic-ui-design-inspiration | Raccolta di statistiche, tracking cards e grafici | Data storytelling in dashboard |
| CUI-04 | https://collectui.com/trending | Catalogo dinamico di design curati, con titoli variabili | Solo discovery; verificare sempre il post originale |

**Limite di verifica:** alcune pagine di Collect UI caricano contenuti dinamicamente e alcune categorie risultano vuote. Qui non attribuiamo autori, licenze o screenshot specifici non risolti. Le proposte CUI sono pattern dedotti da categorie visibili, non moduli tecnici verificati. Dribbble shots possono essere concept statici, non proof di codice, accessibilità o performance.

## Dodici pattern proposti (ID permanenti nel JSON collegato)
- **DCL-001 · Editorial hero**: sezione principale fotografica o contenuto reale, titoli editoriali leggibili, massimo una CTA dominante; evitare foto decorative non pertinenti.
- **DCL-002 · Intentional bento**: tile asimmetriche soltanto per priorità reali; non una griglia casuale, non ripetere la stessa informazione.
- **DCL-003 · Semantic chroma**: superfici neutre + 1 accento brand + accenti semantici minimi; colore comunica stati.
- **DCL-004 · Quiet navigation**: 3–5 destinazioni canoniche; secondarie in una pagina propria; no comandi replicati su ogni card.
- **DCL-005 · Storytelling data**: un KPI in evidenza, trend e contesto accessibili; non grafici ornamentali o numeri inventati.
- **DCL-006 · Media-first gallery**: media a rapporto originale, preview contain e player dedicato; azioni distruttive reversibili.
- **DCL-007 · Contextual actions**: pulsante principale stabile, accesso progressivo alle azioni e conferma di stato comprensibile.
- **DCL-008 · Functional scroll motion**: transizioni leggere, animate solo su progressi reali; disabilitabili con reduced-motion.
- **DCL-009 · First value onboarding**: massimo contenuto utile, permessi contestuali, prima azione subito; niente carousel lunghissimi.
- **DCL-010 · Responsive editorial**: sul web/tablet pannelli distinti (indice, contenuto, dettaglio); no telefono stirato.
- **DCL-011 · Thoughtful empty states**: scenario zero dati che spiega vantaggio e un primo passo; stessa semantica offline/error/retry.
- **DCL-012 · Premium polish without slop**: tipografia, ombre molto basse, raggio coerente, haptic discreto; non glass/blur/gradienti ovunque.

## Design System 2026–27: contratto di qualità
Per ogni app definire e versionare `design_tokens` (colori/surfaces, typography, spacing, radii, borders/elevation, iconography, motion, responsive breakpoints), stato light/dark, qualità delle immagini, linguaggio di navigazione. Nessuna estetica predefinita obbligatoria. La Product Bible prevale sulle reference.

**Gate visivi:** primo avvio, normale uso, loading, zero dati, errore, offline, avvisi, upgrade/premium se esiste, dark, testo 150%, viewport compatto, tablet/web se applicabile, touch target e screen reader. Guardrail: no layout overflow, no high-jank animazioni, no permessi aggiunti per effetto estetico, no aumento dell'APK senza beneficio misurabile.

## Licenza e provenienza
I due siti sono **discovery/UI_UX_REFERENCE**, non CODE_DONOR. Una pagina pubblica o una tua licenza su immagini di altri lotti NON autorizza automaticamente redistribuzione dei design di terzi. Solo URL, note e trasposizioni originali; niente download di shot, immagini o icone per redistribuzione senza licenza/permesso dell'autore. Ogni implementazione deve essere differenziata; nessuna replica visiva 1:1.

## Stato operativo
- Fonti: VERIFIED_PAGE / VERIFIED_SHOT dove indicato.
- Pattern: REFERENCE, PROPOSED_ONLY; nessun codice implementato.
- App mapping: `UI-UX/DRIBBBLE_COLLECTUI_APP_MAP_2026-11-18.json` e .md.
- Prima di promuovere: Product Bible + mock-up + accessibilità + approvazione + codice consumer e QA + regressione.
