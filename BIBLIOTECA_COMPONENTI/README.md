# BIBLIOTECA COMPONENTI — App Factory

**Data iniziale: 19/11/2026.** Biblioteca operativa dentro Design-App; non e' un nuovo repository, un nuovo Golden o un secondo Product Bible.

## Cosa contiene

- **CATALOGO.json**: indice canonico consultabile di 480 componenti, deduplicazione con 4 alias storici, collegamenti ad app e fonti, linguaggio, stato e percorso del codice.
- **INDICE.md**: panoramica per famiglie e sorgenti.
- **sorgenti/ruixen/**: 277 file **originali** TSX/React acquisiti da `ruixenui/ruixen.com@f6b20860623fa39122ac2b5f0e5bd29a9eb10941`, verificati contro SHA Git dei 277 file, con `LICENSE.md` MIT e `PROVENIENZA.json`. Non sono widget Flutter.
- **Uiverse**: 111 file originali HTML/CSS gia' conservati in `UI-UX/UIVERSE/CODICE_SORGENTE/`; il catalogo vi punta, senza salvarne copie. Due varianti con identico blob sono rappresentate da un ID e alias.
- **Amicro / DevLibraries:** 30 sorgenti React/TSX originali recuperati e verificati dal repository MIT al commit bloccato, con `LICENSE` conservata in `sorgenti/amicro/`.
- **Watermelon:** 7 sorgenti React/TSX originali recuperati (incluso View On Map), licenza MIT in `sorgenti/watermelon/`.
- **EaseUI:** 1 sorgente React/TSX originale Theme Toggle, MIT in `sorgenti/easeui/`.
- **Manifest del nuovo lotto:** [38 file con SHA di origine](sorgenti/PROVENIENZA_OSS_EXTRA_2026-11-19.json), ancora senza port Flutter né test consumer.
- **Altre fonti**: Flutter Component Library, Flutter Gems, Forui, DevLibraries, Watermelon, Amicro, Gentleface, ecc. I portali senza codice originale recuperato restano `REFERENCE_ONLY`, per evitare di spacciarli per pacchetti pronti.

## Avanzamento acquisizione

**425** voci canoniche hanno ora un sorgente fisico archiviato, **53** sono ancora solo riferimenti. Il nuovo lotto include **38** file originali; i codici TSX/React non sono automaticamente widget Flutter.

## Anteprime visive per ogni componente e per ogni app

La nuova [tabella completa con colonna **Anteprima**](./TABELLA_478.md) contiene
tutti i 478 record canonici. Le [tabelle generate per app](./PER_APP/README.md)
mostrano ogni associazione componente/app con una miniatura cliccabile o uno
stato esplicito quando la cattura manca. Sono presenti **26 identificativi app** nei collegamenti originari,
normalizzati in **25 viste per prodotto**: `anna-s-diary` e `annas-diary`
sono due alias storici dello stesso prodotto. Non vengono modificati gli ID
nel catalogo sorgente.

Il [visualizzatore HTML interattivo](../docs/componenti.html) offre ricerca,
filtri per app/fonte/disponibilita' immagine e lightbox. Su GitHub la vista
`blob` mostra solo il codice HTML; per usarla nel browser avviare un server
locale dalla root del repository (`python -m http.server 8000`, poi
`http://localhost:8000/docs/componenti.html`) oppure abilitare GitHub Pages
dalla cartella `docs/` (vedi [istruzioni](../docs/README.md)).

**Copertura del primo lotto:** 110 PNG Uiverse provenienti da rendering locale
dei 110 HTML/CSS originali, con JavaScript disabilitato e asset remoti bloccati.
Sono anteprime documentali **CAPTURED_LOCAL_HTML_UNREVIEWED**: non dimostrano
correttezza della UI su mobile ne' includono automaticamente media esterni.
Per le altre 368 voci `NO_VERIFIED_IMAGE` resta visibile finche' non si recupera
una cattura valida; nessun placeholder grafico viene spacciato per il componente
vero. Le 277 sorgenti Ruixen sono archiviate ma ancora prive di immagini e di
assegnazioni ad app nel catalogo canonico.

**Fonte di verita' immagini:** `ANTEPRIME.json`, alimentato soltanto da PNG
reali in `docs/assets/componenti/` tramite
`genera_anteprime.py --write`; `--check` rileva drift tra manifest, tabelle
e screenshot. Per Uiverse la ricattura isolata usa
`render_uiverse_previews.py` nel workflow
`.github/workflows/component-preview-capture.yml`.
Immagine visualizzata, licenza del componente e grado di maturita' del
codice restano evidenze indipendenti.

## Uso immediato degli UID

Ogni componente possiede un ID canonico stabile e un **UID-0001...UID-0478**
che identifica la stessa sorgente in tutte le app. Il registro
[UID_REGISTRY.json](./UID_REGISTRY.json) non rinumera mai gli ID gia' assegnati.
Il comando [uid.py](./uid.py) restituisce codice originale, immagine,
provenienza, target e ragioni per cui l'adattamento e' necessario.

Esempi:

\`\`\`bash
python BIBLIOTECA_COMPONENTI/uid.py lookup UID-0127
python BIBLIOTECA_COMPONENTI/uid.py lookup RXN-button-copy
python BIBLIOTECA_COMPONENTI/uid.py search --text password --limit 12
python BIBLIOTECA_COMPONENTI/uid.py plan UID-0350 --app annas-diary --stack flutter --role "input codice"
python BIBLIOTECA_COMPONENTI/uid.py plan UID-0127 --app world-days --stack flutter --role "pulsante copia"
python BIBLIOTECA_COMPONENTI/uid.py validate
\`\`\`

Nella chat: **"Usa UID-0127 per il pulsante Copia di World Days"**;
l'agente risolve lo stesso componente nella libreria, verifica il Product
Bible e lo stack, poi puo' implementare l'adapter nel repo dell'app con PR
e test. Il resolver non effettua modifiche alle app da solo.

**Stati:** \`PLAN_ONLY_NOT_IMPLEMENTED\`, \`SOURCE_UNAVAILABLE\`,
\`ADAPTER_REQUIRED\`, \`SOURCE_REVIEW_REQUIRED\`. Non attribuisce mai
\`COPY_READY\` a un TSX archiviato in un progetto Flutter solo perche' esiste
il file. Anche Forui nativo richiede verifica delle dipendenze/versioni e
integrazione col design approvato.

## Ricerca locale

```bash
python BIBLIOTECA_COMPONENTI/cerca.py --testo button
python BIBLIOTECA_COMPONENTI/cerca.py --app annas-diary
python BIBLIOTECA_COMPONENTI/cerca.py --fonte RUIXEN --solo-sorgente --limite 5
python BIBLIOTECA_COMPONENTI/cerca.py --linguaggio flutter --formato json
python BIBLIOTECA_COMPONENTI/cerca.py --id UIV-107
python BIBLIOTECA_COMPONENTI/validate.py
```

## Status: cosa significa

| Stato | Significato |
|---|---|
| ARCHIVED_SOURCE | Codice originale recuperato e presente nel repo; NON implica compatibilita' Flutter, dipendenze risolte o test runtime. |
| REFERENCE_ONLY | Solo metadati/link o demo; non esiste un codice originale vendorizzato nel catalogo. |
| COPY_READY | **Nessuna nuova voce** raggiunge automaticamente questa maturita'; serve validazione della versione adattata. |

## Processo di adozione

1. Leggere Product Bible e stile approvato dell'app; preferire reference selezionate dall'utente e verificare Golden/donor interni.
2. Cercare il componente nel catalogo, identificare origine, file, lingua, license e dipendenze.
3. Per sorgenti React, CSS o TSX realizzare un adapter o una reimplementazione Flutter/Compose idonea; non rinominare `.tsx` in `.dart`.
4. Controllare caso per caso licenza originaria e asset esterni: codice pubblicamente visibile non autorizza sempre redistribuzione. Materiale senza diritti dimostrati resta linkato, non copiato.
5. Svolgere build, analisi semantica/accessibilita', responsive, reduced-motion, screenshot before/after e QA su target reale. Soltanto dopo classificare una versione adattata come LIBRARY_VERIFIED/COPY_READY e, se giustificato, candidarla ai Golden di Core.
6. Aggiornare il catalogo quando si importano nuovi componenti, evitando duplicati per ID, URL/commit/path o sorgente identico; conservare gli alias di vecchi registri.

## Confini

- Nessun package installato in app consumer; nessuna modifica alle app.
- Gli originali Ruixen sono TSX/React con possibili dipendenze e asset esterni non verificati; conservare MIT e attribution quando riutilizzati. L'origine Uiverse ha un archivio con proprio registro licenze.
- Le 15 schede Flutter Component Library censite non espongono attualmente, nell'audit svolto, file Dart originali e licenza verificabile: pertanto non sono state copiate.
- Il catalogo e' un indice leggero: non contiene una seconda copia dei file Uiverse e non incorpora download inutili di asset dimostrativi.

**Principio:** archiviare originali quando accessibili e legittimamente riutilizzabili, catalogare ogni fonte utile, certificare solo l'adattamento effettivamente testato.

## Integrazione nativa Forui (non ancora certificata su app)

- `UID-0479` / `FUI-001`: pulsante Flutter `FButton`, codice MIT originale con dipendenze Forui.
- `UID-0480` / `FUI-002`: esempio form email/password con validazione locale; non è autenticazione funzionante.
- Codice, licenze e immagini originali in `sorgenti/forui/` e `ANTEPRIME_ORIGINI_FORUI.json`.
- Nessuna installazione nelle app o Golden: il riuso richiede controllo package, tema, font, SDK, dimensione APK e test nel consumer.
