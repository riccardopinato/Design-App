# AppLlama MCP → benchmark UX e app originale Flutter (prompt per App Factory)

**Stato:** REFERENCE / PROMPT_TEMPLATE · 21/11/2026 · codice/non eseguito · Source of truth App Factory: [CURRENT](https://github.com/riccardopinato/App-Factory-Core/blob/main/CURRENT.yaml) (baseline del lotto `4df94ac3b3ea22a2323634fe83c3c7770fe3b835`).

## Testo originale fornito dall'utente

> «utilizzando appllama mcp, leggi tutti gli schermi e i video di (nome app), e crea un'app ispirata a esso.»

Fonte: messaggio utente 21/11/2026. È uno **spunto di workflow**, non autorizzazione a copiare un prodotto commerciale, a pagare un abbonamento o a importare un'intera libreria protetta.

## Prompt operativo migliorato — Flutter-first

```text
Studia [NOME APP DI RIFERIMENTO] come benchmark UX usando esclusivamente Appllama MCP già autorizzato
(e la skill ufficiale Appllama Usage, se disponibile). App target ORIGINALE da creare: [NOME NOSTRA APP].
Piattaforme: Android Flutter come primo target; iOS soltanto se richiesto e verificato.

FASE A — Ricerca circoscritta e documentata
1) Verifica che Appllama MCP sia collegato dall'utente e che il piano/crediti lo permettano.
   Non aggirare paywall, rate limit o API non pubbliche, non attivare acquisti.
2) Esamina le schermate, i video e i flow pertinenti di UNA app target per volta.
   Se la richiesta è di analizzare tutti gli schermi della singola app, lavora nel limite
   dei crediti e termini dell'accesso, registrando copertura e lacune: niente estrazione
   o mirroring massivo del catalogo, download permanente, screenshot rehosting, training.
3) Per ogni flow rilevante documenta: ingresso, navigazione, contenuto essenziale,
   IA gerarchia, feedback, stati vuoto/loading/errore/offline, paywall, sicurezza,
   riduzione motion, a11y, failure modes. Annotare fonte/ID/link senza salvare media protetti.
4) Analizza cosa funziona e cosa NO: non riprodurre difetti, dark patterns, testi,
   asset, marchi, icone, illustrazioni, struttura pixel-to-pixel o contenuti del prodotto fonte.

FASE B — Progettazione indipendente App Factory
5) Leggi Product Bible della NOSTRA app, repository e baseline App Factory CURRENT;
   usa Design-App come priorità per lo stile personale già curato.
6) Presenta un design brief, i differenziali del nostro prodotto, flussi originali
   e reference motivatamente scelte con stato DIRETTA / ADATTATA / NON ADATTA.
   Se il prodotto è nuovo, prepara Product Bible/roadmap candidata, non app consumer
   esistente senza conferma dello scope.
7) Traduci gli apprendimenti in componenti originali Flutter (Dart); non incollare TSX
   o codice Expo/React Native. Riduci dipendenze, peso APK e ridisegna funzionalmente
   solo ciò che abbiamo diritto di implementare.

FASE C — Build e prova, solo se sviluppo autorizzato
8) Procedi in PR scoped con tracciabilità per singolo flow, design tokens, error/offline,
   test widget/integration e confronto visivo solo con asset autorizzati.
9) Rispetta a11y e reduced-motion, prestazioni reali Android, dimensione APK,
   test fisici e validazione esatta del commit; non dichiarare screenshot/mock Web
   prova di collaudo nativo.
10) Consegnare relazione: schermate della fonte analizzate (ID + copertura), video
    e pattern studiati, originalità differenziale, fonte delle reference, dipendenze,
    licenze, codice realmente implementato, QA PASS/FAIL e punti ancora da verificare.

Se Appllama non è connesso, esegui soltanto lo studio documentale da fonti liberamente
accessibili e marca l'analisi interna delle schermate MCP come NON ESEGUITA.
```

## Provider e confini

- Endpoint ufficiale dichiarato da Appllama: `https://mcp.appllama.io/mcp`. Pagina intro: https://appllama.io/mcp.
- Skill ufficiali: https://github.com/Appllama/appllama-skills — commit del lotto `dd5caaec3d5d50ad7fc0324da238119c6b7c3707`, repo MIT. La seconda skill ha orientamento **Expo/React Native** e va usata solo come criterio UX se il target è Flutter, senza import diretto.
- **Appllama Pro** richiesto per MCP; i crediti sono personali, un chiamata ne usa uno salvo `get_credits`. URL media temporanei, divieti di esportazione/archiviazione massiva, ripubblicazione e training. Termini ufficiali: https://appllama.io/terms.
- La skill/repo MIT NON rende MIT lo screenshot o il video delle app di terzi. L'originalità del prodotto finale è requisito, non opzionale.
- Nessun MCP collegato o chiamato in questo intake; template registrato, non applicato a un consumer.

## Rinforzo dai tre video forniti in questo lotto

Le tre analisi sono in [registro video](./APPLLAMA_MOTION_ART_STACK_REGISTRY_2026-11-21.json):
- conferma distruttiva ben progettata (video #1),
- animazione di stato ThinkingOrb (video #2),
- sei layout/carousel/prospettive 3D (video #3).

Gli MP4 non vengono pubblicati nella libreria perché la proprietà/distribuzione dei media terzi non è accertata.
