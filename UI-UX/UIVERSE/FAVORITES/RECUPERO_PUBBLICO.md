# Uiverse — prova autonoma di recupero pubblico dei sorgenti

Questo strumento sperimentale tenta di leggere **solo risorse pubbliche** da `uiverse.io` senza sessione autenticata. È indipendente dai favoriti privati già esportati dall'utente: legge soltanto gli URL canonici dei 43 originali mancanti in `UI-UX/UIVERSE/REGISTRO_COMPONENTI.json`.

## Prova in due componenti

La workflow GitHub Actions `.github/workflows/uiverse-public-recovery.yml` esegue una prova **read-only, senza secret**, a partire da `UIV-005` e `UIV-006`. Lo script usa la pagina dati Remix di Uiverse e, se il loader non restituisce il codice, il suo endpoint `/resource/post/code/{id}`, entrambi su host `uiverse.io`. Base tecnica: [DevSissi/uiverse-tool](https://github.com/DevSissi/uiverse-tool/blob/main/scripts/fetch-post.py), tool pubblico MIT, ispezionato il 18/11/2026.

Non avviene alcuna modifica a Uiverse, nessuna scrittura su Design-App e nessun utilizzo di cookie, credenziali o GitHub token da parte dello script. I risultati salvati nell'artefatto restano non verificati finché lo snapshot originale, il copyright per-post e i checksum non sono convalidati e integrati con PR separata.

## Esiti

- `UIVERSE_RECOVERY_STATUS`: restituisce solo errori sanitizzati o esito positivo per ID.
- `UIVERSE_RECOVERY_DATA`: dati di codice originali in base64 per consentire il trasferimento verificabile a un intervento GitHub successivo.
- `UIVERSE_RECOVERY_SUMMARY`: numero totale tentati / riusciti.

**Non etichettare il codice come pronto per Flutter/Compose**. La sua destinazione è la sottosezione HTML/CSS originale MIT con licenze, DOI dei dati e source snapshots, non le app consumer. In caso di blocco della rete pubblica, non aggirare autenticazione e non inventare snippet; usare l'esportatore locale dell'utente solo se strettamente necessario.
