# MOCKUP ESTETICI — Design-App

Archivio visivo per le reference estetiche selezionate dall'utente. **La classificazione non equivale all'approvazione o all'implementazione in un'app.** La sezione integra — non sostituisce — i pattern `DS-*` e le famiglie di stile `STYLE-*` già presenti in `registry/DESIGN_REGISTRY.yaml`.

## Categorie iniziali

| Categoria | ID | Orientamento | App candidate |
|---|---|---|---:|
| [AESTHETIC](./AESTHETIC/README.md) | MOCK-STYLE-001 | Atmosfere morbide, palette armoniche, composizioni editoriali e spaziature ariose | 4 |
| [NEON](./NEON/README.md) | MOCK-STYLE-002 | Superfici scure con accenti luminosi, bagliori contenuti e gerarchia ad alto contrasto | 4 |
| [VINTAGE](./VINTAGE/README.md) | MOCK-STYLE-003 | Carta, grana fotografica, tipografia d'epoca e dettagli analogici | 4 |
| [PIXEL ART](./PIXEL%20ART/README.md) | MOCK-STYLE-004 | Grafica a pixel leggibili, silhouette nette, animazioni a frame e icone modulari | 4 |
| [POLAROID](./POLAROID/README.md) | MOCK-STYLE-005 | Foto con cornici analogiche, didascalie, data/luogo e composizioni collage | 4 |
| [ANIME](./ANIME/README.md) | MOCK-STYLE-006 | Illustrazione e storytelling ispirati al linguaggio anime: espressività, composizioni, palette e dettaglio illustrato | 4 |

Per le associazioni aggregate consultare [MATRICE_APP_STILI.md](./MATRICE_APP_STILI.md); per i dati strutturati [REGISTRO_STILI.yaml](./REGISTRO_STILI.yaml) e [CATALOGO_IMMAGINI.yaml](./CATALOGO_IMMAGINI.yaml).

## Regole di ingestione delle prossime immagini

1. Quando arriva un'immagine, valutarne estetica, palette, tipografia, layout, interazioni e tipo di app.
2. Assegnare **uno stile primario e zero o più stili secondari**; se non basta, creare una nuova categoria, senza forzature.
3. Salvare il file una sola volta in `<STILE_PRIMARIO>/IMMAGINI/` con identificativo stabile (`MOCK-0001` ecc.). Nelle altre categorie inserire un riferimento relativo nel file `RIFERIMENTI_INCROCIATI.md` per evitare duplicazioni di binari.
4. Registrare origine, URL, autore se conosciuto, data di acquisizione, titolarità/licenza o stato non verificato, ID, percorso, tag e app suggerite in `CATALOGO_IMMAGINI.yaml`.
5. **Diritti:** repository pubblico. Caricare asset terzi solo con base di utilizzo/redistribuzione verificata o esplicita autorizzazione; in caso contrario conservare esclusivamente link, metadati o note descrittive. La presenza su Pinterest NON costituisce licenza.
6. Per ogni app proposta indicare area di applicazione, compatibilità, limiti e stato `PROPOSTA`. Validare sempre Product Bible, roadmap, accessibilità, performance e brand prima dell'implementazione.
7. Gli stili non sono mutuamente esclusivi; anche un'app può comparire in più categorie. Le immagini non sono un Golden o un donor di codice.
8. Quando pertinente, distinguere uso di una reference estetica dalla riutilizzabilità di un asset (COPY/ADAPT/REFERENCE_ONLY).

**Stato iniziale (12/11/2026):** struttura e proposte create, **zero immagini importate**. Fonte Pinterest segnalata per successive consegne: https://it.pinterest.com/rikyjaypinaz/stili-grafici-per-app/ (non ancora acquisita).

## Collegamento al catalogo UI/UX

Per componenti, layout, gerarchie, effetti, controlli e interazioni consulta [UI/UX](../UI-UX/README.md). Una reference può appartenere sia a uno stile estetico sia a più stili UI/UX; registrare sempre un solo file canonico e associare gli ID senza duplicare binari.

## Nuovo lotto estetico — 12/11/2026

Consulta la [matrice estetica di 33 riferimenti unici](./RIFERIMENTI_UTENTE_2026-11-12.md); nuove famiglie Y2K RETRO, ORGANIC, CINEMATIC, ILLUSTRATED. Le immagini sono conservate solo nell'allegato-galleria privata della conversazione fino a prova di licenza/permesso.

## Nuove reference estetiche — 13/11/2026

[Indice estetico dei 66 riferimenti](./RIFERIMENTI_UTENTE_2026-11-13.md) con catalogo canonico, file e hash in [UI/UX](../UI-UX/REGISTRO_RIFERIMENTI_UTENTE_2026-11-13.json). Focus: palette editoriali, paper cut, ambient landscape e illustrazione giapponese/cinese. Diritti immagini non verificati: riferimenti solo testuali, nessun originale pubblicato; compatibilità per app in stato PROPOSTA.

## Ricerca per app e per famiglia estetica

La [matrice inversa App → Stili](../UI-UX/PER_APP_STILI_2026-11-13.md) e la [matrice diretta Stile → App](../UI-UX/PER_STILE_APP_2026-11-13.md) integrano il catalogo estetico con quello UI/UX. Un'immagine può avere stili estetici e UI complementari; uno stile appartiene a più app, un'app a più stili. L'indice usa lo stesso [JSON canonico relazionale](../UI-UX/MATRICE_BIDIREZIONALE_APP_STILI_2026-11-13.json), senza copiare i file originali delle opere terze.


## Anteprime associate alle famiglie estetiche

Gli ID `UIR-xxxx` delle schede sono link alle immagini. Per aprire una singola immagine *nella pagina GitHub* usa [Anteprime dei 99 UIR](../UI-UX/ANTEPRIME_99.md), con riquadri espandibili. Il [visualizzatore lightbox](../docs/index.html) aggiunge la sovrimpressione vera dopo pubblicazione mediante GitHub Pages; vedi [istruzioni di attivazione](../docs/README.md).
