# DevLibraries Bookmarks — intake controllato per App Factory

**Collegamento segnalato dall'utente (17/11/2026):** https://devlibraries.com/bookmarks

## Evidenza e limiti

La pagina esatta `https://devlibraries.com/bookmarks` è stata tentata tramite navigazione web il 17/11/2026, ma ha restituito **Cache miss**. Nessuna lista personale, nessun titolo di preferito, nessuna scheda e nessuna opzione di esportazione sono stati accessibili o verificati. Non possiamo dedurre che un elenco sia pubblico o disponibile per terzi dal semplice link alla pagina.

**Stato di questo registro:** `INTAKE_WORKFLOW_ONLY` (zero bookmark importati e zero connessioni DevLibraries autorizzate). È una procedura, non un catalogo dei preferiti dell'utente.

## Flusso di raccolta — solo se i dati vengono condivisi

1. L'utente apre la propria raccolta https://devlibraries.com/bookmarks nel browser dove è disponibile.
2. Condivide in chat **i link diretti ai componenti** (copiati o esportati se il sito lo consente) oppure una schermata leggibile con nomi/URL. Non condividere session cookie, token, password, link di login magic o dati privati.
3. Normalizzare ogni voce: `provider`, `original_url`, `title`, `component_id` (se verificato), `source_repo`, `source_path`, `source_commit/blob`, `license`, `framework`, `preview_url` e `evidence`. Non dichiarare verificato un URL ricostruito da una sola immagine.
4. Confrontare con `UI-UX/`, `ICONE/`, `sources/DESIGN_RESEARCH_SITES.json` e `registry/OSS_DESIGN_SOURCES.yaml`: deduplicare per URL canonico e SHA, **non** per sola etichetta. Un portale aggregatore non è il proprietario delle licenze dei singoli componenti.
5. Per ogni app pertinente aggiungere una relazione molti-a-molti con `fit`, `surface`, `animation_behavior`, `constraints`, `status` e `provenance` nel catalogo specifico e in `PER_APP/REGISTRO_APP_DESIGN.json`. Aggiornare la scheda `PER_APP/<slug>.md` e il changelog **nella stessa PR**.
6. Usare `PROPOSED_ONLY` per abbinamenti, `REFERENCE` per sorgenti ancora non integrate. `IMPLEMENTED` e `VERIFIED` richiedono rispettivamente prove nel repository consumer e collaudo effettivo. La Product Bible prevale per scelte e vincoli.
7. Gate prima del merge: validazione Design-App, cinque controlli CI quando applicabili, evidenza delle fonti, assenza di URL privati, collisioni o claim di licenza; controllo GitHub del commit della PR.

## Cosa non è possibile dedurre dal link

- Numero di preferiti, nomi, date di salvataggio, categorie o ordinamento.
- Se i preferiti siano salvati in un account, in sessione o nel browser.
- Se il sito offra esportazione o condivisione pubblica della lista.
- Che i componenti già citati nella conversazione siano automaticamente *presenti* nella raccolta Bookmarks.

## Obiettivo

Consentire un futuro **intake batch** dei preferiti DevLibraries senza perdere le relazioni app↔design o creare duplicati nei registri esistenti. Questo file non importa né conserva contenuti personali non condivisi.

**Riferimenti interni:** [Fonte DevLibraries](./DEVLIBRARIES_DISCOVERY_2026-11-17.md) · [Siti di ricerca](./DESIGN_RESEARCH_SITES.json) · [Dossier per app](../PER_APP/README.md) · [Audit sorgenti](./README.md).
