# Forui UID-0479 / UID-0480 — compatibilità e confini di riuso

Data: 19 novembre 2026. Stato: SOURCE_ARCHIVED / ORIGINAL_PREVIEW / CONSUMER_NOT_VERIFIED.

## Sorgente immutabile e licenze

- Repository: https://github.com/duobaseio/forui
- Commit sorgente: `5dbf97c926a53fcfe3436db1be6262ac40961db5`
- Forui package, versione nel `forui/pubspec.yaml` sorgente: `0.28.0`
- Copyright e licenza codice: MIT; il LICENSE archiviato contiene ulteriori avvisi per i font, da preservare.
- File originali e SHA Git: `PROVENIENZA.json`; immagini originali + SHA256: `../../ANTEPRIME_ORIGINI_FORUI.json`.
- Stato anteprime: `UNREVIEWED`, non mock-up approvati né prove di runtime su Android/iOS.

## Versioni minime e dipendenze verificate nel pubspec upstream

- Flutter: `>=3.50.0`; Dart SDK: `>=3.14.0 <4.0.0`.
- `forui`: dipende da `collection ^1.18.0`, `cupertino_ui ^1.0.0`, `forui_lucide ^0.28.0`, `material_ui ^1.0.0`, `meta ^1.19.0`, `sugar ^4.0.0`, `vector_math ^2.1.4`, `intl`, `flutter_localizations`.
- Il pacchetto dichiara asset font Inter. Verificare avvisi e peso dell'APK prima del consumer.
- Il progetto di demo `docs_snippets` richiede anche `auto_route ^11.0.0`, `docs_snippets` stesso, `material_ui`, oltre al pacchetto `forui`. Non trasferire automaticamente dipendenze di routing/demo a un'app.

Questi vincoli appartengono all'esatto commit archiviato: eventuali versioni future richiedono un nuovo audit, senza riscrivere la provenance.

## Significato dei due UID

- **UID-0479 / FUI-001:** `FButton` è un widget del pacchetto Forui, non un singolo file Dart autonomo. Le varianti richiedono tema e risorse della libreria.
- **UID-0480 / FUI-002:** esempio di campi email/password e bottone con validazione Flutter `Form`. Non gestisce login remoto, autenticazione, credenziali sicure o sessioni.

## Reuse gate

1. Verificare SDK/toolchain, `pubspec.lock`, dipendenze effettive e peso finale dell'app target.
2. Confrontare con i componenti Golden/donor interni e con le preferenze di design nel repository Design-App.
3. Evitare di importare routing `auto_route` o temi di demo se l'app dispone già di propri equivalenti.
4. Testare contrasto, focus, loading, error, form validation, tastiera, scale text, light/dark, navigazione e localizzazione.
5. Eseguire Flutter analyze/test/build, review visivo e acceptance sul consumer; non registrare `CERTIFIED` o `COPY_READY` prima di queste prove.

Nessuna applicazione consumer o Master/Golden è stata modificata da questo intake.
