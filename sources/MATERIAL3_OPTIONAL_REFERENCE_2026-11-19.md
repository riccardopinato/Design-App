# Material Design 3 — opzione selettiva, non default (19/11/2026)

**Stato:** REFERENCE, PROPOSED_ONLY. Non significa che M3 sia presente nelle app candidate o che sia stato approvato il redesign.

## Fonte ed evidenze
- Portale ufficiale: https://m3.material.io/ — rendering JavaScript richiesto; non e' stato possibile estrarre direttamente tutte le sezioni dalla homepage.
- Guida ufficiale Kotlin/Compose: https://developer.android.com/develop/ui/compose/designsystems/material3 — composables, temi, palette dinamiche Android 12+, accessibilita', M3 Expressive. Consultare versioni supportate.
- Flutter: https://docs.flutter.dev/ui/design/material , https://docs.flutter.dev/ui/widgets/material e https://docs.flutter.dev/release/breaking-changes/material-3-default — UI Material disponibile in Flutter; il default tecnico della libreria NON e' un obbligo estetico per tutte le app.
- Golden interno Flutter: https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/ui/GOLDEN_THEME_M3_FLUTTER_v1.txt . E' un template COPY-READY disponibile quando l'app sceglie M3, non un componente Kotlin/Compose.

## Regola di scelta
1. La Product Bible e le reference selezionate dall'utente in Design-App sono prioritarie per il risultato estetico.
2. M3 e' **un'opzione**: nessuna ripartenza da M3 obbligatoria, nessun divieto. Puo' servire per tutta la shell oppure solo per settings, filtri, dialoghi, switch, pulsanti e controlli utilitaristici.
3. Le scelte tecnologiche Flutter/Kotlin-Compose e stilistiche sono separate. Un'app gia' M3 non va riscritta per il solo desiderio di non sembrare stock; una nuova app non va forzata su M3.
4. Personalizzare token di colore, tipografia, spaziature, bordi, icone, interazione e motion quando si adotta M3. L'obiettivo anti-AI-stock resta vincolante.
5. Non attivare automaticamente dynamic color o Material 3 Expressive; usarli solo quando compatibili con branding, piattaforme, contrasto, performance e preferenze.
6. Prima di modificare: verificare il codice consumer, la Product Bible, le reference Design-App, licenze/SDK; creare mock-up o prove runtime e collaudo visivo/accessibilita'.

## Candidati indicati dall'utente
| App | Valutazione orientativa | Possibile ruolo M3 | Limite |
| --- | --- | --- | --- |
| FocusSense | HIGH | strumenti di produttivita', impostazioni, filtri e componenti di stato | conservare identita' focus e dati reali |
| Tabletop Motion Alarm | HIGH | allarme armato/disarmato, countdown, alert e PIN | sicurezza e risposta rapida prima del look |
| The Luminous Infinite Circle | MEDIUM | preferenze e configurazione | AOD/luci mantengono direzione grafica originale |
| Battery Guard | MEDIUM | diagnostica, interruttori e impostazioni | UI distintiva, peso APK e privacy |

**NOT_VERIFIED:** qui non sono stati letti gli attuali file di tema, widget o dipendenze delle quattro app. Non e' stato verificato se utilizzino M3 oggi. Anche le classificazioni HIGH/MEDIUM sono suggerimenti di fit, non approvazioni di progetto.

[Associazioni bidirezionali in JSON](../UI-UX/MATERIAL3_OPTIONAL_APP_MAP_2026-11-19.json). Nessuna nuova dipendenza, donor, Golden o componente installato.
