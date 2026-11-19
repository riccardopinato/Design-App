# Source triage — 10 reference-only UID senza PNG (19/11/2026)

Questo file e' una ricognizione **non un'acquisizione**. Nessuna PNG viene considerata recuperata senza il componente esatto, provenienza, diritti e QA.

- Amicro MIT: al commit `fa5f8ffbe39537a8db191806066b8773c47c82e9`, albero GitHub completo (816 file; non troncato) verificato: i percorsi **perspective-flip** e **spatial-door-portal** non figurano tra i path; il riferimento DevLibraries non prova l'equivalenza con un altro componente.
- Watermelon MIT (come registrato in catalogo): al commit `9d6defcf89880d0a00fbccad773c046bb51d7afb`, albero completo (2965 file; non troncato): nessun path per gli slug esatti **text-gradient**, **notification-list** o **flip-clock**. Esistono altri esempi di *notification* nel repository ma non e' provato che siano lo stesso UID.
- DBM-027/030 sono riferimenti da screenshot utente senza repository, URL o licenza file specifica. Il nome simile di un progetto trovato online non consente di dichiarare che sia l'originale.
- DSP-006 e' un'immagine personale non depositata: non e' ricostruibile come immagine identica da una descrizione.

| ID | Nome | Sorgente indicata | Gate e prossimo passo |
|---|---|---|---|
| AMX-003 | Perspective Flip | [Link](https://devlibraries.com/libraries/amicro/perspective-flip) | Slug esatto assente nell'albero Amicro pinnato; verificare fonte/versione prima di copiare |
| AMX-005 | Spatial Door Portal | [Link](https://devlibraries.com/libraries/amicro/spatial-door-portal) | Slug esatto assente nell'albero Amicro pinnato; verificare fonte/versione prima di copiare |
| DBM-027 | Helix Spinner | Nessuna URL originale | Fonte, commit e diritti non identificati; ricostruire link esatto dal riferimento originale |
| DBM-028 | Loader | Nessuna URL originale | Fonte, commit e diritti non identificati; ricostruire link esatto dal riferimento originale |
| DBM-029 | Particle Shape Morph | Nessuna URL originale | Fonte, commit e diritti non identificati; ricostruire link esatto dal riferimento originale |
| DBM-030 | Infinite Spiral | Nessuna URL originale | Fonte, commit e diritti non identificati; ricostruire link esatto dal riferimento originale |
| WML-006 | Text Gradient | [Link](https://devlibraries.com/libraries/watermelon/text-gradient) | Slug esatto assente nell'albero Watermelon pinnato; individuare source path affidabile |
| WML-008 | Notification List | [Link](https://devlibraries.com/libraries/watermelon/notification-list) | Slug esatto assente nell'albero Watermelon pinnato; individuare source path affidabile |
| WML-009 | Flip Clock | [Link](https://devlibraries.com/libraries/watermelon/flip-clock) | Slug esatto assente nell'albero Watermelon pinnato; individuare source path affidabile |
| DSP-006 | Loading & Waiting Visual References (user screenshot) | Nessuna URL originale | File personale originale non presente; occorre upload |

**Stato:** 10/10 casi nominati, 0 PNG aggiunte da questa ricerca, 0 sostituzioni inventate. I 9 originali di terzi non vengono promossi a MIT-sorgente verificato senza il file preciso. Il runtime React usa solo dipendenze effettivamente recuperate e licenziate.
