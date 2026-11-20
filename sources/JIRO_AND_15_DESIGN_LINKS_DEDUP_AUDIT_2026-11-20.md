# Lotto 15 link Web design — deduplica e Jiro Build

**Data:** 20/11/2026 · **Factory baseline:** `App-Factory-Core@4df94ac3b3ea22a2323634fe83c3c7770fe3b835` (CURRENT Master 27, Golden Index 31, Registry v2). **Design-App base:** `c34483036b2ca5ad068e9568a3a8ce3b6294296f`.

## Deduplica

15 URL ricevuti: **13 già catalogati**, **1 nuovo sito canonico** `DESIGN-SITE-044` Jiro.build, e **1 sottopagina distinta del medesimo provider** `DESIGN-SUBL-003` [Jiro Builder](https://jiro.build/builder). `godly.website` e' un alias che reindirizza a `recent.design` e va al canonical `DESIGN-SITE-018`, non una nuova fonte. Non sono state ripetute analisi approfondite delle 13 risorse esistenti.

| # | URL ricevuto | Decisione |
|---|---|---|
| 1 | https://jiro.build/ | **NUOVO: DESIGN-SITE-044** — libreria di prompt / landing page |
| 2 | https://jiro.build/builder | **NUOVA SOTTOPAGINA: DESIGN-SUBL-003** sotto il sito Jiro, non un nuovo dominio |
| 3 | https://godly.website/ | **GIÀ PRESENTE** `DESIGN-SITE-018` (Recent Design) — alias/redirect ufficiale |
| 4 | https://land-book.com/ | **GIÀ PRESENTE** `DESIGN-SITE-017` (Land-book) |
| 5 | https://landdding.com/ | **GIÀ PRESENTE** `DESIGN-SITE-019` (Landdding) |
| 6 | https://recent.design/ | **GIÀ PRESENTE** `DESIGN-SITE-018` (Recent Design) |
| 7 | https://60fps.design/ | **GIÀ PRESENTE** `DESIGN-SITE-021` (60FPS) |
| 8 | https://cosmos.so/ | **GIÀ PRESENTE** `DESIGN-SITE-028` (Cosmos) |
| 9 | https://fontshare.com/ | **GIÀ PRESENTE** `DESIGN-SITE-022` (Fontshare) |
| 10 | https://fontinlogo.com/ | **GIÀ PRESENTE** `DESIGN-SITE-020` (Font in Logo) |
| 11 | https://coolors.co/ | **GIÀ PRESENTE** `DESIGN-SITE-024` (Coolors) |
| 12 | https://realtimecolors.com/ | **GIÀ PRESENTE** `DESIGN-SITE-023` (Realtime Colors) |
| 13 | https://lucide.dev/ | **GIÀ PRESENTE** `DESIGN-SITE-025` (Lucide) |
| 14 | https://svgl.app/ | **GIÀ PRESENTE** `DESIGN-SITE-026` (SVGL) |
| 15 | https://shots.so/ | **GIÀ PRESENTE** `DESIGN-SITE-027` (Shots) |

## 1. Jiro Design Prompt Library — DESIGN-SITE-044

URL: https://jiro.build/ · Tipologia: design prompt library per Bolt/Lovable/Replit/Cursor, ispirazione landing e componenti Web, template completi e singole sezioni (hero, FAQ, testimonial, pricing, feature, CTA, background).

**Promesse marketing vs evidenza:** il messaggio dell'utente riporta **1.500+ prompt, 180+ landing e 1.000+ sezioni**; la pagina ufficiale corrente in lettura dinamica presenta numeri differenti (es. Builder **100+ template e 800+ sezioni**). Le quantità sono in evoluzione, **non è stato eseguito un censimento card per card** e non devono diventare un conteggio certificato. Sono invece osservate categorie e numerosi esempi di template. Non trattare la dichiarazione `prompt identico = codice identico` come test di riproducibilità.

**Accesso:** preview/pubblico e vari contenuti Free, prompt premium e **source code per template e sezioni** indicati dalla pagina nelle offerte a pagamento (in particolare piani annuali/lifetime). Nessun account, abbonamento o copia di codice/prompt pagato acquisiti. Il codice prodotto è orientato a Web/React e builder AI; non è un widget Flutter/Compose.

**Licenza ufficiale:** https://jiro.build/terms-conditions (aggiornata al 10/05/2026). Concede utilizzo personale e commerciale nel proprio progetto e progetti clienti, anche per prodotti venduti, ma non concede di:
- rivendere, sublicenziare o redistribuire standalone il catalogo Jiro, componenti o template;
- creare una **libreria concorrente di componenti o design** usando contenuti Jiro;
- effettuare copie/scraping massivo della piattaforma o asset;
- addestrare modelli IA sui contenuti senza autorizzazione preventiva.

**Conseguenza Design-App:** link, descrizioni originali, mapping e riferimenti estetici ammessi; **non archiviare i template/source o dump di prompt Jiro in BIBLIOTECA_COMPONENTI** come donor pubblico riutilizzabile. L'uso del singolo progetto licenziato richiede comunque piano, diritti di font/assets e privacy per immagini/file. `REFERENCE_ONLY` — nessun UID o source snapshot.

## 2. Jiro Builder — DESIGN-SUBL-003

URL: https://jiro.build/builder · **stesso provider**, funzionalità hosted builder con chat e pubblicazione; **non trattare come nuova azienda o donor OSS separato**.

Funzioni ufficiali consultate tramite pagina indicizzata e pagina template: creazione da descrizione/template, modifica con linguaggio naturale e selezione puntuale delle sezioni, cronologia/undo, preview desktop/tablet/mobile, SEO settings, pubblicazione su `name.jiro.host`, dominio proprio e download ZIP su piani idonei. La pagina specifica /builder non è stata apribile direttamente nella cache browser, ma il suo testo integrale indicizzato è stato consultato, inclusa la FAQ.

**Piano Free dichiarato:** 5 crediti/giorno **fino a 25/mese**, 2 indirizzi `jiro.host`, template free, pubblicazione su `jiro.host`, con **sospensione del sito Free dopo 30 giorni** secondo FAQ. **ZIP export / dominio personalizzato disponibili su piani a pagamento**; gli importi e le offerte cambiano, quindi verificarli prima di acquisti. Le funzioni reali richiedono account e non sono state usate, quindi **non dichiarare una build/pubblicazione eseguita**.

**Adozione App Factory:** per promozione Web di un'app già esistente, non per creare UI Android/Flutter, autenticazione, database, media sync o una dashboard operativa. Se si volesse usare il Builder su un sito reale, prima documentare termini, data/hosting, proprietà dei file generati, GDPR/privacy, export/backup, dipendenza da subscription, trasparenza sulla UI effettiva.

## Mappa e stato

**18 associazioni `PROPOSED_ONLY` a 9 dossier app**. [Matrice per-app](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.md) · [JSON e duplicati canonici](../UI-UX/JIRO_LIBRARY_BUILDER_APP_MAP_2026-11-20.json). Priorità alle preferenze di design già archiviate e ai mock-up approvati; Jiro non modifica automaticamente alcuna direzione estetica, Product Bible, Master, Golden o funzionalità.

**Nessun contenuto terzo scaricato/coperto da licenza Jiro copiato**, nessun UID, nessun codice app modificato, nessun test di integrazione Builder o performance UX rivendicato.

## Provenienza

- Home Jiro (pagina ufficiale con categorie, pricing e descrizione library): https://jiro.build/
- Jiro Builder (pagina ufficiale indicizzata): https://jiro.build/builder ; https://jiro.build/builder/templates
- Termini ufficiali: https://jiro.build/terms-conditions
- Godly redirect a Recent: https://godly.website/ → https://recent.design/
