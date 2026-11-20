# Design sources: Best Designs on X, Figma Community, ReUI + Bento Widget Templates

**Data:** 20/11/2026. **Contesto:** proseguimento del lotto da 15 fonti Design-App registrato nella [PR #58](https://github.com/riccardopinato/Design-App/pull/58). Nuove fonti: **3 siti** e **1 file Figma specifico**, non un quarto portale. Nessun consumer modificato, nessuna libreria runtime installata, nessun Golden promosso.

**Factory baseline fissata:** `riccardopinato/App-Factory-Core@4df94ac3b3ea22a2323634fe83c3c7770fe3b835` — CURRENT Master v27, Index v31, Registry v2. Design-App baseline `638c5cfb06066981416b6098c321dfaf3209b635`.

## 1. Best Designs on X — DESIGN-SITE-029

**Link:** https://bestdesignsonx.com/

**Evidenza:** la home e' raggiungibile, ma la lettura HTTP non restituisce contenuto strutturato. Fonti indipendenti lo descrivono come aggregatore di design condiviso su X con raccolte frequenti. Non sono stati esaminati singoli post, autori o asset. **Stato:** REFERENCE / SITE_NOT_MACHINE_READABLE. Utilita': monitoraggio di visual trends, identita' per brand, app e icone; non e' una libreria Flutter ne' un OSS donor. Registrare sempre URL originale del post/autore se si seleziona una singola reference.

**Caveat:** immagini, screenshot e marchi di X non vengono licenziati da questo portale; non vendorizzare.

## 2. Figma Community — Mobile Apps — DESIGN-SITE-030

**Link:** https://www.figma.com/community/mobile-apps?resource_type=files&editor_type=figma

**Evidenza:** la directory generale non ha restituito risultati navigabili dal browser Web; verificate invece le regole ufficiali Figma Community. La directory e' un discovery pool, non un UI kit unico.

**Licenze:** per i file Community **gratuiti**, Figma dichiara CC BY 4.0 con attribuzione; i file a pagamento seguono la Community Paid Resource License, con condizioni proprie. I marchi, le foto di terzi e ulteriori licenze dell'autore non vanno assunti liberi. Non confondere Figma widgets con widget Android/iOS.

**Valore:** riferimento per UX di flussi mobile reali, onboarding, editor, impostazioni, accessibilita', responsive design e componenti. Per ogni nuovo file, URL esatto, nodo, autore, licenza e source/state distinti.

## 3. ReUI — DESIGN-SITE-031

**Link:** https://reui.io/ · **Repository:** https://github.com/keenthemes/reui · **Commit osservato:** `067aa0dc7f8bbfec1cd76fc5ad31f842be5f569a`.

**Evidenza:** sito ufficiale, catalogo, documentazione, changelog e README GitHub verificati. Changelog v2.9.0 del 19/11/2026 cita **1.265 esempi gratuiti**; il README del commit letto riporta 1.264. Il catalogo e' dinamico: non cristallizzare questi numeri come totale invariabile. ReUI e' una libreria **React/TypeScript + shadcn/ui + Tailwind** con componenti gratuiti; blocks/icone/template avanzati sono soggetti a piani premium separati. README dichiara licenza MIT del software free.

**Pattern altamente riusabili:**

- **Data Grid:** sorting, filtering, column pinning, in-place edit e stato persistente, ottimo per App Factory Dashboard/Notes Web, ma impone attenzione a virtualizzazione e accessibilita'.
- **Filters:** ricerca, select, multi-select, data e booleani; utile a cataloghi e archivio progetti.
- **Kanban + Gantt:** bacheche e dipendenze, per dashboard operativa. Non trasformare in nuova logica dati se esiste un task model.
- **Event Calendar:** varianti mese/settimana/giorno/agenda come **reference** per Anna, non sostituisce il calendario Flutter o la logica ricorrenze gia' implementata.
- **Timeline, Stepper, File Upload, Skeleton/Empty:** reference per cronologie, onboarding e stati resilienti.

**Riuso tecnico:** installazione/copia del sorgente soltanto in Web React compatibile, dietro dependency/permission/license gate. In Flutter, solo ADAPT/REWRITE originale e test su app; TSX non e' Dart. Non copiare i Pro blocks/Pro icons nel repo. Il MCP ReUI e' opzionale; nessuna installazione/connessione fatta.

## 4. Bento Widget Templates — FIGMA-BENTO-001 (file specifico)

**Prototipo originale:** https://www.figma.com/proto/4fm9HsfzmWpKjl6X9XAGO9/Bento-Widget-Templates--Community-?node-id=190-1470&t=FQ6JXZSQNCPEKe0G-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1

**Prova diretta:** accesso Figma alla chiave `4fm9HsfzmWpKjl6X9XAGO9`, screenshot di cover `190:1470` generato con successo, metadata delle pagine Components `104:232`, Inspiration `132:628`, Read Me `1:4` letti. L'accesso rivela un canvas con componenti Figma riutilizzabili; non crea un widget Flutter o AppWidget Android.

**Famiglie effettivamente identificate:**

- **Social:** 2x2, 4x2, 4x4, 2x4.
- **Artifact:** 2x2, 4x2, 4x4, 2x4.
- **Notes:** 2x2, 2x3, 2x5, 2x6 · Some node IDs are cover instances and should not be mistaken for master components..
- **Fitness:** 2x2, 4x2, 2x4.
- **Clear palette:** 2x2, 2x4 · stili Daylight, Noon, Sunset, Midnight.
- **Flighty:** 4x4.
- **Collage:** 4x4.
- **Business card:** 4x4.
- **QR code:** 4x2.
- **Device:** 2x2, 2x4.
- **Wordle:** 2x2, 4x2, 4x4, 2x4.

**Indicazioni dell'autore dal Read Me:** trascinare istanze nel canvas, cambiare le proprieta', adattare palette, esportare preferibilmente ad alta risoluzione; avviso: **gli elementi grafici dei widget di brand appartengono ai relativi marchi**. Presenza di `@madewithjello` nel footer; identita'/licenza del singolo file non confermate dalla pagina Community originaria. **License gate:** FILE_LEVEL_UNVERIFIED; disegni originali e brand asset separati. Non importare automaticamente screenshot nel repo pubblico.

**Pattern estratti:** adaptive asymmetric grid; information hierarchy by card footprint; small/medium/large tile contracts; mix media+text+stats+links; editable semantic widgets; user customization. Limitazione: il file ha un orientamento bento/portfolio, non una app consumer completa. Non applicare un layout a griglia densissimo a ogni schermo o a una schermata di sicurezza.

## Priorita' per App Factory

| Fonte/elemento | Priorita' per il progetto | Riuso operativo |
|---|---|---|
| Bento Figma | P1 visivo | Anna `Il tuo spazio`, Notes home, dashboard Factory; UI reference verificata |
| ReUI | P1 Web | Grid, Kanban, Filtri, stepper e timeline; source MIT per stack compatibili |
| Figma Community Mobile | P1 design discovery | Estrarre file precisi, non importare l'intera galleria |
| Best Designs on X | P2 discovery | Trend scouting con link a post e autore originari |

## Esito, stati e contatori

- Nuovi siti unici da inserire nel registro: **3** (DESIGN-SITE-029..031), piu' **1 asset Figma** (FIGMA-BENTO-001) con URL originale e nodi verificabili.
- **12** app collegate da **31** relazioni PROPOSED_ONLY, senza implementazione.
- Figma: metadata reali per 3 pagine e cover; **0** file Figma esportati, **0** SVG/foto di terzi copiati.
- ReUI: licenza OSS pubblicata e README consultati, **0** componenti TSX copiati, **0** pacchetti Flutter installati.
- Prima di qualsiasi port in app: confronto con preferenze/screenshot Design-App gia' approvati, Product Bible, scope, licenza, semantica UI, reduced motion, screenshot visual QA e test runtime.

## Fonti di verifica

- Best Designs on X: https://bestdesignsonx.com/ ; https://reftrove.com/resources/bestdesignsonx
- Figma Community licenze: https://help.figma.com/hc/en-us/articles/360042296374-Figma-Community-copyright-and-licensing
- ReUI Docs: https://reui.io/docs ; Free components: https://reui.io/components ; v2.9.0: https://reui.io/docs/changelog ; repository: https://github.com/keenthemes/reui
- Figma prototype e node IDs nel registro: `UI-UX/FIGMA_BENTO_WIDGET_TEMPLATES_2026-11-20.json`
