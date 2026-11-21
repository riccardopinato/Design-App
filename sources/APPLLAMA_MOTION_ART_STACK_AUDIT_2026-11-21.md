# Appllama · Dissolve · Another Boring Day · Libraries.dev · 10 librerie UI + 3 video

**21 novembre 2026** · App Factory baseline `4df94ac3b3ea22a2323634fe83c3c7770fe3b835` · Design-App base `3966ebbfd14daa87f277703c066a6734764670d8`.

## Esito intake e dedup

- **18 URL** effettivi (due Appllama, due Libraries.dev, un link abbreviato non risolto; tre URL di fonti già censite). **3 video** allegati analizzati mediante campionamento dei frame, durata e hash SHA-256.
- **11 nuove voci Design-App**: `DESIGN-SITE-049…059` per Appllama, Dissolve, AnotherBoring, Libraries.dev, Magic UI, 21st, shadcn/ui, Motion Primitives, Cult UI, Animate UI, Kibo UI.
- **3 siti già censiti e NON duplicati**: React Bits `DESIGN-SITE-034`, Aceternity `DESIGN-SITE-040`, Scrolltide `DESIGN-SITE-035`.
- **6 nuovi source repository OSS** registrabili con commit+licenza: Appllama/appllama-skills, seo-skills/seo-audit-skill, ibelick/motion-primitives, nolly-studio/cult-ui, imskyleen/animate-ui, shadcnblocks/kibo.
- **2 source repository già presenti**: magicuidesign/magicui e shadcn-ui/ui. NON duplicati; nuova pagina sito dedicata.
- **Un link t.co non risolto** `https://t.co/fRjCLeHI5m`: il claim '2.000 siti di design' resta NON VERIFICATO. Non creare voce canonica per una destinazione che non si conosce.

## Fonti principali / verifiche indipendenti

| Sorgente | Cosa è utile | Tecnologia | Diritti e limiti |
|---|---|---|---|
| [Appllama MCP](https://appllama.io/mcp) e [skills](https://github.com/Appllama/appllama-skills) | Studio mirato di schermate app reali, video e flussi; skill playbook e quality bar | MCP remoto a pagamento; skill Expo/React Native | **MCP richiede Pro** con crediti; termini vietano scraping, mirror, dataset o training; il repo skill è **MIT** ma non trasferisce diritti sulle schermate; non connesso a questa sessione. Fonte [terms](https://appllama.io/terms). |
| [Dissolve](https://dissolve.rselmi.com) | Animazioni particle-dissolve di viste | React Native Skia/Reanimated 4, React secondo descrizione `dissolve-ui` npm | Fonte dominio non ispezionabile; indice npm afferma MIT, **licenza ufficiale di codice/source da ricontrollare** prima di ogni import. No Flutter drop-in. |
| [Another Boring Day](https://anotherboring.day/) | Catalogo arte selezionata quotidianamente con background/rotation | Sito e app macOS esistenti | Confermato da [pagina del prodotto originale](https://basalt.yevgenglukhov.com/) e [listing App Store Mac](https://apps.apple.com/lu/app/another-boring-art-wallpaper/id6757328187?mt=12). Arte, immagini, metadata, brand, curatela e UI **NON liberi da copiare**. L'idea Android deve essere indipendente. |
| [Libraries.dev/Waves](https://libraries.dev/waves) | Distortion Waves, layer shader/glow/riflessi, transitions | React Web/desktop **e SwiftUI** (documentazione); Flutter serve riscrittura | 7 pacchetti pubblicati sono MIT secondo [terms](https://libraries.dev/terms); Pro studio/skill non sono automaticamente MIT. Verificare singola versione/package prima dell'integrazione. |
| [SEOmator](https://github.com/seo-skills/seo-audit-skill) | Audit per pagine Web, Core Web Vitals, structured data e accessibilità | CLI Node, Electron desktop e Agent Skill | Repo MIT @`f43ba12d65898cea8f043ec2d87fc413c4ca9e0c`; **tool QA per Web**, non stile di app Flutter. Numero regole dichiarate variabile con la revisione: non fissato come KPI. |
| [Scrolltide](https://www.scrolltide.co/) | Prompt Web di landing e 3D scroll | React/Next.js/Tailwind/GSAP/WebGL | Già registrato, mix free/premium, progetti reali con licenza propria; non copiare pacchetti. |
| [Magic UI](https://magicui.design/) | Bento, hero, highlights, CTA | React | Codice di `magicuidesign/magicui` MIT @`b0b2e4974b1b68cd5278277c6837a27736e20c3a`; Pro separato/proprietario. |
| [21st.dev](https://21st.dev/) | Marketplace reference e confronto componenti, anche mobile | Dipende dal singolo risultato | Verificare repo e licenza **per elemento**. |
| [shadcn/ui](https://ui.shadcn.com/) | Standard UX per dialog, form, cards | React | Repo `shadcn-ui/ui` MIT @`45bbf9ba23c9c0f63d38887947e5fb06f59c7da3`; già presente nei source OSS. |
| [Motion Primitives](https://motion-primitives.com/) | Primitives di motion minimal | React | MIT @`120f64f6ca60348e251f929e9c81f11ccbe45eda`. |
| [Cult UI](https://cult-ui.com/) | Tactile cards e animazioni d'identità Web | React/Tailwind | MIT @`d71b1428b811c2779d46ea41b7ef8c9f9c9991c2`. |
| [Animate UI](https://animate-ui.com/) | Animate controls and accessible motion | React/Tailwind | **MIT + Commons Clause** verificato in `imskyleen/animate-ui@9873c628afdcdb030e74dc2930774a2aa473bd39`: sì in prodotti, **no vendita/redistribuzione componenti originali come libreria**. |
| [Kibo UI](https://kibo-ui.com/) | Richer forms/cards/advanced controls | React/shadcn | `shadcnblocks/kibo@3d63cdb15b79d972e3dc38a10997987672f9b263`, licenza permissiva equivalente a MIT nel file `license.md`. |

**React Bits** e **Aceternity UI** già presenti: non duplicati. React Bits MIT+Commons Clause, Aceternity licensing per classe/repo/prodotto.

## Video allegati, ispezione reale

L'ordine è quello dell'upload dell'utente, **non** dimostra corrispondenza certa con uno specifico URL/post X. Il file video rimane fuori GitHub per i diritti media di terzi; registriamo invece hash, dimensioni, frame osservati e idee. Verificare originale/licenza prima di ricopiare codici o media.

| Video | Metadati | Pattern osservati | Destinazioni |
|---|---|---|---|
| 1 | 21.7 s · 480×360 · SHA256 `d862f547835e715a3ddc889a4c2c4c8a60c362fb7dd21f8289e27441923bd84f` | Prima/dopo di una richiesta delete-account: titolo plain question, conseguenze e dati persi, azione rossa, Cancel evidente; logo appllama visibile, **l'autore non identificato** | Omni Cleaner, Anna's Diary |
| 2 | 9.77 s · 428×360 · SHA256 `a4128660146f7ce2356bfc05bd1114a852426659bb08102e730c608b1b2f6e40` | ThinkingOrb: Idle/Thinking/Searching/Listening/Done/Error; particle sphere, success green tick, error red | Agent, Notes |
| 3 | 20.83 s · 540×540 · SHA256 `c256f03ecd7ee5e7d82e6c9aaa7336d5fb2d544d22ca2fdb496de658431c546a` | Sei demo parallele con carte prodotto, device card, ventaglio di libri, anello rotante, gallery musica e orbit layout; panel parametri visibile | Wonderlog, Deskland, Web landing |

## AnotherBoring → idea propria Android

**ID proposta: `ART-2026-001`**, registrare in repository Idee-app-Archivi-riferimenti nella `11-NUOVE-IDEE/INBOX_IDEE.md`. Idea originale: **Atelier del Giorno** (nome provvisorio), app Flutter di esplorazione opere d'arte, scheda curata giornaliera, tavolozze di colore/filtri locali, wallpaper Android opzionale tramite plugin nativo, archivio preferiti offline. **Non** usare brand/visual/codice/asset/feed automatico di AnotherBoring. Fonti legali indipendenti: open-access per opere con licenza e attribuzione verificata in record (API Met/AIC, ecc. valutare singoli diritti). Distinta da `AL-ANDROID-2026-001` Adaptive Landscape (sfondi dinamici ispirati a un launcher, non diario d'arte).

**MVP proposto:** 1 opera/dì + scelta alternativa, scheda artista/data/provenienza, preferiti, crop per smartphone, imposta sfondo Home/Lock nel rispetto dei vincoli Android, cache/consenso e notifiche facoltative. **Riservati** prima di decisione: API data license, copyright immagini/didacalie, pubblico dominio per opera digitale, font, costi CDN, differenza monetizzazione vs raccolte gratuite.

## Quality boundary

Tutte le mappe per app: `PROPOSED_ONLY`; zero UID; zero file video, wallpaper o componenti di terze parti importati; nessuna app, Store, Factory, Golden modificata. [Mappa per app](../UI-UX/APPLLAMA_MOTION_ART_APP_MAP_2026-11-21.md). Target Flutter riusa *idee* e adapter originali, **mai codice React/SwiftUI come se fosse Dart**.
