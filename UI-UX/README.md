# UI/UX — Libreria grafica, componenti e layout

Catalogo specifico di interfacce, effetti, navigazione, composizione, controlli e micro-interazioni della App Factory. Questa directory tecnica si chiama `UI-UX` perché `/` separa directory in Git; il nome della sezione esposta resta **UI/UX**.

La sezione è distinta da [MOCKUP ESTETICI](../MOCKUP%20ESTETICI/README.md), che cataloga atmosfere e identità visive (ANIME, VINTAGE, NEON, ecc.). **Una stessa reference può essere classificata in entrambe**, con un solo file canonico, metadati di cross-link e nessun binario duplicato.

## Categorie iniziali

| Stile UI/UX | ID | Focus | App candidate |
|---|---|---|---:|
| [NEUMORPHISM](./NEUMORPHISM/README.md) | UIX-STYLE-001 | Controlli soft UI con elementi in rilievo/incassati, ombre doppie molto leggere e superfici omogenee. | 4 |
| [SOFT 3D](./SOFT%203D/README.md) | UIX-STYLE-002 | Componenti morbidi e volumetrici, forme gonfie, moduli quasi fisici e ombre soffuse; stile claymorphism. | 4 |
| [GLASSMORPHISM](./GLASSMORPHISM/README.md) | UIX-STYLE-003 | Pannelli semitrasparenti e sfocati sovrapposti a sfondi, con bordi luminosi, profondità e stratificazione. | 4 |
| [NEO-APPLE](./NEO-APPLE/README.md) | UIX-STYLE-004 | Composizioni iOS-like con contenitori floating, superfici dinamiche, rifrazione/glass soft e spaziatura premium. Non replicare loghi o UI proprietaria 1:1. | 4 |
| [NATURE-TECH](./NATURE-TECH/README.md) | UIX-STYLE-005 | UI digitale con sagome organiche, elementi naturali, composizione spaziale, superfici lattiginose e colori botanici. | 4 |
| [BENTO UI](./BENTO%20UI/README.md) | UIX-STYLE-006 | Composizioni con card di dimensioni diverse, funzioni raggruppate, griglie modulari e gerarchia per importanza. | 5 |
| [PASTEL UI](./PASTEL%20UI/README.md) | UIX-STYLE-007 | Interfacce con gradienti soffici, palette candy controllate, elementi levigati e transizioni di colore leggere. | 4 |
| [SPATIAL 3D](./SPATIAL%203D/README.md) | UIX-STYLE-008 | Elementi virtuali sospesi, layered depth, mock-up di dispositivi e presentazioni volumetriche di prodotti. | 4 |
| [MINIMAL CONTROLS](./MINIMAL%20CONTROLS/README.md) | UIX-STYLE-009 | Griglie e pannelli ad alta concentrazione di funzioni, con simboli essenziali, elevata precisione e feedback discreti. | 5 |

## Struttura ricorrente

Per ogni stile:
- `IMMAGINI/`: immagini **solo quando l'utilizzo e la redistribuzione sono autorizzati**;
- `APP SUGGERITE PER QUESTO STILE/`: matrice di compatibilità con le app (proposte, non roadmap);
- `COMPONENTI_UI.md`: pattern riproducibili, scelte tecniche e vincoli UX;
- `RIFERIMENTI_INCROCIATI.md`: associazioni secondarie con altre categorie, senza duplicazione degli asset;
- `README.md`: scheda dello stile.

Indici: [matrice app ⇄ stili](./MATRICE_APP_STILI.md), [registro stili](./REGISTRO_STILI.yaml), [catalogo immagini](./CATALOGO_IMMAGINI.yaml), [riferimenti estratti dallo screenshot](./RIFERIMENTI_DALLO_SCREENSHOT.md).

## Regole molti-a-molti

1. Ogni fonte può avere **uno stile UI/UX primario e più stili secondari**. Se un riferimento appartiene anche a MOCKUP ESTETICI, collegare l'ID e il percorso esistente fra i cataloghi.
2. Ogni app può ricevere proposte per più stili, e ogni stile può servire più app: distinguere sempre `HIGH / MEDIUM / LOW`, schermata d'uso, rischi e `PROPOSED_ONLY`.
3. In `CATALOGO_IMMAGINI.yaml` ogni asset ha ID stabile, classificazioni, URL e autore originali se disponibili, licenza/diritti, uso consentito, path canonico e destinazioni. Copiare un file binario solo con diritti verificati.
4. Senza permessi di riuso: salvare solo link, descrizione e classificazione; niente screenshot Pinterest/asset esterni nel repository pubblico.
5. Studiare e **reimplementare indipendentemente** pattern generici (grid, blur, radius, motion) usando Design-App, Golden e licenze compatibili. Non clonare marchi, illustrazioni o prodotto concorrente.
6. Prima dell'integrazione nelle app, verificare Product Bible, roadmap, accessibilità, responsività, light/dark, gesture, reduced motion, memoria, FPS e APK footprint.
7. Una proposta non significa `APPROVED`, `IMPLEMENTED`, `SOURCE_VERIFIED` o `COPY_READY`. Nessuna app viene modificata dalla catalogazione.

**Prima fonte:** screenshot UI/UX del 12/11/2026 (bacheca con 25 Pin, soltanto 11 esempi visibili/parziali classificati). **Zero immagini copiate nel repo**.
