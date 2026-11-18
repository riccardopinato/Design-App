# Uiverse Favorites — importazione da pagina autenticata

**Stato: IN ATTESA DELL'ELENCO UTENTE.** La pagina [My Favorites](https://uiverse.io/favorites) non rende leggibili i componenti personali in una sessione non autenticata e mostra «Sign in to save posts to Favorites». Non dedurre i preferiti dal catalogo pubblico né dai nove link già selezionati in chat: possono sovrapporsi, ma non costituiscono l'elenco completo.

## Esportazione sicura in una sola volta

1. Sul proprio PC, aprire Chrome o Edge e accedere a [Uiverse Favorites](https://uiverse.io/favorites) mediante il login del sito.
2. Aprire DevTools con **F12** e selezionare **Console**. Se il browser mostra un avviso sui codici incollati, leggerlo e valutare il sorgente prima di procedere.
3. Aprire il file [`scripts/uiverse_favorites_export_browser.js`](../../../scripts/uiverse_favorites_export_browser.js), leggerlo e copiarne **tutto il contenuto** nella Console. Non inserire password o token nella chat e non usare script di terzi non verificati.
4. Lo script scorre la pagina, colleziona i link alle card (ove disponibili come anchor nel DOM) e genera il file **`uiverse-favorites-export.json`** sul PC. Non invia dati fuori dal browser e non cambia i tuoi preferiti.
5. **Controllare il numero** di elementi nel file e confrontarlo con il totale eventualmente mostrato dal sito. Se non coincidono, la raccolta è **PARTIAL**, non «tutti»: può esserci scroll interno, lazy load, componenti senza `href` o paginazione particolare. In quel caso inviare anche screenshot della lista e segnalare la differenza.
6. Allegare il JSON nella chat App Factory. L'elenco costituisce l'input necessario per il successivo harvest.

## Pipeline dopo l'allegato

- Deduplicare per URL normalizzato `https://uiverse.io/<author>/<slug>` contro [`REGISTRO_COMPONENTI.json`](../REGISTRO_COMPONENTI.json) e il resto di Design-App; **riutilizzare gli ID esistenti**.
- Per ciascun URL: analisi UI/UX, categoria (card, button, input, loader, switch, pattern...), preview e semantica, proposte su più app.
- Estrarre **HTML/CSS originale** ove accessibile e consentito, con autore, licenza MIT (verificando il contenuto), provenance URL + commit/blob SHA oppure hash; archiviare in [`CODICE_SORGENTE`](../CODICE_SORGENTE/README.md) senza etichettare gli adattamenti Flutter/Compose come già pronti.
- Dove manca la fonte, registrare **SOURCE_CODE_NOT_LOCATED** e continuare la ricerca; **mai** inventare snippet o assegnare `COPY_READY` senza test.
- Aggiornare nella stessa PR il registro JSON Uiverse, la matrice bidirezionale app ⇄ componente, tutti i dossier `PER_APP` pertinenti, le fonti, l'audit e la legenda. `PROPOSED_ONLY` finché Product Bible e codice consumer non attestino adozione reale.
- Verificare accessibilità (touch, tastiera, screen reader, reduced motion), prestazioni su telefono, colore e leggibilità; mantenere l'identità distinta di ogni app.

## Sicurezza, provenienza e limiti

Questo esportatore **legge soltanto la pagina aperta nel tuo browser**; non riceve cookie, token OAuth, account GitHub o dati di login. Non ha accesso autonomo alla tua sessione. L'assenza di accesso autenticato impedisce attualmente il censimento completo e qualsiasi dichiarazione di codice originale recuperato dai segnalibri non visti. Anche con il JSON serve verifica dell'effettivo totale, perché il sito può cambiare il markup.

**Baseline al momento della preparazione:** App-Factory-Core `a8d20ceb71ce9e9e16e6756d257d611fa6f1e0ec`, Design-App `7df6fb3782d0745ad13eed0bcb839b2d3e5d9d04`.
