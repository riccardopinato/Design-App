# BestSaaSWebDesigns Curated Designs e UIColours — audit 20/11/2026

**Esito:** 2 nuove fonti in Design-App (`DESIGN-SITE-042` e `DESIGN-SITE-043`), non duplicate nei 41 siti precedenti. 22 proposte `PROPOSED_ONLY` per 13 app. Factory baseline `App-Factory-Core@4df94ac3b3ea22a2323634fe83c3c7770fe3b835`, CURRENT Master 27 / Golden Index 31 / Golden Registry v2, Design-App base `9974c2b855fc631bdd444c8d8941dfab4eb5184a`.

## 1. BestSaaSWebDesigns / Curated Designs — DESIGN-SITE-042

**URL originale:** https://bestsaaswebdesigns.com/curated-designs

**Distinzione importante:** il link non è la home della raccolta di 545+ SaaS reali. La **pagina Curated Designs** è una raccolta separata di progetti pubblicati su X con categorie **Web & App, 3D, Animation, Illustration**. La versione indicizzata della pagina descrive **1.200** riferimenti totali, ma il numero è dinamico (visibile come 823 Web & App, 63 3D, 156 Animation, 158 Illustration) e **non è stato verificato tramite una lettura diretta di tutte le card**. Ciascuna card rimanda al post originale dell'autore; immagini/video sono serviti da X, non concessi in licenza al catalogo.

**Evidenza:** i contenuti testuali di questa sottopagina sono stati letti tramite la ricerca Web indicizzata sull'esatto URL; l'apertura diretta ha dato un cache miss. Sono state consultate anche home, Terms e documentazione ufficiale. Non dichiarare originali/codice sorgente di singole card acquisiti o ispezionati.

**Vantaggio differenziale:** rispetto a Dribbble/Recent/Best Designs on X, l'organizzazione per quattro famiglie aiuta a cercare un riferimento più preciso. Il valore è la *motivazione documentata*: per ogni eventuale riferimento futuro annotare categoria, URL esatto del post X, autore, 1-2 pattern osservati, schermata candidata, licenza, data e stato di approvazione; nessun download/screenshot o copia creativa automatica.

**Servizio correlato da non confondere:** la **home** https://bestsaaswebdesigns.com/ è un catalogo diverso di siti SaaS con landing e sezioni, tech stack, colori e font, con MCP dichiarato gratuito senza login a https://mcp.bestsaaswebdesigns.com/mcp. L'MCP indicizza il catalogo dei siti, **non è stato verificato che esponga le 1.200 card di Curated Designs**. Nessuna connessione MCP attivata.

**Licenza:** Terms del 05/11/2026 https://bestsaaswebdesigns.com/terms vietano scraping indiscriminato e rivendita dei contenuti del sito; le card provengono dai creatori X e il portale stesso dice di usare i design come **reference**, non come asset da copiare. Valutazione: `REFERENCE_ONLY`. Non copiare schermate, marchi, illustrazioni, video, font o sorgenti nel repo o negli APK senza autorizzazione separata.

**Pattern prioritari:** composizione editoriale delle card, layout responsive non generici, typography-driven hero, microanimazioni funzionali, narrazione visuale, illustrazioni e motion leggeri; per Deskland/FrameLab non importare 3D o shaders senza budget GPU/FPS verificato.

## 2. UIColours — DESIGN-SITE-043

**URL:** https://uicolours.com/ — **non confondere** con `uicolors.app` o `uicolors.org`, servizi differenti.

**Verifica diretta:** home, sezione Brand Colours, Colour Systems, UI Theme Builder. Il catalogo brand alla lettura elencava **193 brand** e filtri per settore; è dinamico. Il sito dichiara creatore Steve Leggat (Front&Back).

**Funzionalità e pattern verificati:**

1. **Site Gallery e Brand Colours:** raccolta di palette cromatiche di siti e marchi, con identificazione degli hex, utilizzabile per benchmarking estetico; **i loghi e le identità non vengono automaticamente licenziati**. Fra i casi citati nella galleria sono presenti Linktree, Sentry, Discord, Razorpay, ma non è consentita la copia indiscriminata dell'arte brand.
2. **UI Theme Builder:** 12 temi chiari/scuri pronti, customizzazione dei colori per ruolo, anteprima reale su card, form, popover, grafici ed elementi UI. Esportazioni pubblicizzate come **shadcn/ui CSS/OKLCH**, DaisyUI v4/HSL, DaisyUI v5/OKLCH, Tailwind v4/OKLCH e **Figma Tokens JSON**. L'export automatizzato/runtime non è stato eseguito: non affermare di avere salvato token reali generati dal sito.
3. **Colour Systems:** guida tecnica RGB/HSL vs OKLCH con esempi percettivi. Distinguere **uniformità di luminosità apparente** e **compliance WCAG**: OKLCH non garantisce da solo il contrasto. La pagina Colour Explorer offre analisi dei contrasti per coppie, ma nessun audit di colori dell'app è stato eseguito.
4. **Design tokens candidati:** background/foreground, card/cardForeground, popover, primary/primaryForeground, secondary, accent, destructive, muted, border, input e focus/ring. Va applicata una vera matrice di contrasto su stati disabled, visited, error, loading, grafici, light/dark e testo ingrandito; non è un cambio di framework obbligatorio.

**Valore App Factory:** per i prossimi redesign, partire dalle palette e dai mock-up già **salvati e approvati** nel repo Design-App. Usare UIColours per verificare gerarchia e accessibilità della scelta cromatica, senza sostituire automaticamente l'identità cromatica dell'app (es. Rose di Anna's Diary o Color Bento/Linktree di Omni Cleaner). Per Flutter generare manualmente semantic color roles (es. ThemeExtensions) e validare i veri widget in app: **i CSS export Web e i JSON Figma non sono codice Dart pronto**.

**Stato licenze:** il copyright di brand/loghi e immagini resta ai rispettivi proprietari. Non sono stati individuati termini di esportazione/licenza esaustivi per i token generati specificamente da questo servizio: segnare `OUTPUT_RIGHTS_TO_VERIFY`; nessun JSON/CSS originale estratto.

## Esito complessivo

- **Due siti unici nuovi**: 042/043, catalogo totale previsto 43.
- **22 collegamenti su 13 profili** con idee `PROPOSED_ONLY`, senza cambiamento di Product Bible, app, Master, Golden o donor.
- **0** screenshot/post di X, immagini brand, file di palette, CSS e snippet di terzi copiati. Niente MCP installato, nessun nuovo UID.
- Nella successiva revisione estetica: consultare preferenze già registrate → scelta del caso d'uso → ispirazione originale citata → tokens semantici → test accessibilità/visivi → approvazione su consumer.

## Provenienza

- https://bestsaaswebdesigns.com/curated-designs (pagina esatta indicizzata, accesso diretto cache miss)
- https://bestsaaswebdesigns.com/ (home catalogo SaaS)
- https://bestsaaswebdesigns.com/terms (termini aggiornati il 05/11/2026)
- https://bestsaaswebdesigns.com/mcp (MCP del catalogo SaaS, non validato per Curated Designs)
- https://uicolours.com/ ; https://uicolours.com/brands ; https://uicolours.com/colour-systems ; https://uicolours.com/tools/theme-builder
