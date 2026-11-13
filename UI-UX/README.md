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

## Nuovi riferimenti forniti dall'utente — 12/11/2026

Sono classificati [35 file, 33 immagini distinte](./RIFERIMENTI_UTENTE_2026-11-12.md) in entrambe le tassonomie, con [registro JSON](./REGISTRO_RIFERIMENTI_UTENTE_2026-11-12.json), [matrice inversa per app](./MATRICE_APP_RIFERIMENTI_2026-11-12.md) e indici per categoria. Aggiunte famiglie RETRO DESKTOP, TOGGLE & SWITCH, EDITORIAL UI, DESIGN SYSTEM, ILLUSTRATED CONTROLS, NAVIGATION UI, SKEUOMORPHISM. Originali JPG non importati nel repository pubblico senza verificare i diritti di redistribuzione.

## Intake grafico consolidato — 13/11/2026

[Catalogo 66 riferimenti](./RIFERIMENTI_UTENTE_2026-11-13.md), [registro sorgente/hashes](./REGISTRO_RIFERIMENTI_UTENTE_2026-11-13.json), [matrice app](./MATRICE_APP_RIFERIMENTI_2026-11-13.md). 77 upload, 11 duplicati SHA-256 esatti; 66 nuovi rispetto ai 33 distinti del 12/11. Le nuove etichette in tabella sono tag descrittivi, non nuove famiglie canoniche in REGISTRO_STILI.yaml. Nessun codice app/test/Golden importato.

## Matrici bidirezionali per app e stile

[App → Stili](./PER_APP_STILI_2026-11-13.md) · [Stile → App](./PER_STILE_APP_2026-11-13.md) · [JSON normalizzato di associazioni](./MATRICE_BIDIREZIONALE_APP_STILI_2026-11-13.json). Copertura: 99 riferimenti unici dei lotti 12/11 e 13/11; 18 famiglie tecniche, 10 famiglie estetiche, 19 app, 254 coppie distinte. Ogni coppia può avere più immagini. Non ci sono vincoli uno-a-uno e non si creano binari duplicati. Stili e app candidati sono PROPOSTA, non componenti approvati.

## Dichiarazione personale sulla licenza dei riferimenti — 13 novembre 2026

L'utente dichiara una **licenza personale** per tutte le immagini dei lotti 12–13/11/2026 (99 JPG distinti). La [dichiarazione e il perimetro](./DICHIARAZIONE_LICENZA_PERSONALE_2026-11-13.md) sono registrati nei due cataloghi JSON. Stato: `USER_DECLARED_PERSONAL_LICENSE`, non prova indipendente della licenza o di un permesso di redistribuzione pubblica. Le classificazioni e le associazioni molti-a-molti rimangono invariate.


## Anteprime UIR cliccabili

Le 99 schede possono aprire l'immagine direttamente cliccando l'ID `UIR-xxxx` nelle matrici; è inoltre disponibile la [galleria GitHub con anteprime espandibili](./ANTEPRIME_99.md). Il [visualizzatore HTML](../docs/index.html) permette una vera sovrimpressione con filtro per app e stile, dopo attivazione di GitHub Pages sul ramo `main` e cartella `/docs`. Le immagini della PR #17 rimangono identificate come **non ancora su main**.
