# Flutter CI toolchain pin — 2026-11-12

## Problema riscontrato
La PR #15 della libreria design ha evidenziato un problema **preesistente nelle pipeline non toccate dai cataloghi**: il runner `stable` aggiornato automaticamente a Flutter 3.50.0 segnala l'import `package:flutter/material.dart` come `deprecated_member_use` e `flutter analyze` termina con exit code 1 in tre pacchetti:
- `packs/icons/flutter`: `icon-flutter`;
- `packs/motion/flutter`: `motion-flutter`;
- `packs/sound/adapters/flutter`: `sound-pack`.

Lo stesso repository ha `flutter-visual-qa` già **fissato a Flutter 3.47.9** e quella pipeline è passata.

## Correzione temporanea e verificabile
Fissare esplicitamente Flutter **3.47.9** anche nei tre workflow interessati, mantenendo **intatti `flutter analyze` e `flutter test`**, e la piena matrice di CI. Così nessuna nuova release del toolchain rende il repository rosso a sorpresa.

## Migrazione futura
La soluzione strutturale non è ignorare il lint: Flutter 3.50 ha ufficializzato la deprecazione di `package:flutter/material.dart` e `package:flutter/cupertino.dart` in favore dei pacchetti separati `material_ui` e `cupertino_ui`. Pianificare una PR dedicata che:
1. verifichi i requisiti dell'SDK e le dipendenze dei tre pacchetti;
2. usi `dart fix --apply --code=migrate_design_widgets` su un branch isolato o applichi la modifica manualmente;
3. aggiorni i contratti pubblici/breaking changes dei pacchetti riusabili e i test;
4. collaudi nuovamente su Flutter 3.50 e rimuova/aggiorni il pin quando i gate sono tutti verdi.

Fonti ufficiali:
- https://flutter.dev/blog/whats-new-in-flutter-3-50
- https://docs.flutter.dev/release/breaking-changes/material-ui-and-cupertino-ui

**Nessun test è stato saltato o reso non-fatal**. Il pin è un vincolo temporaneo documentato, non certificazione del supporto Flutter 3.50.
