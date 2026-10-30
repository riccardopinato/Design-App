# Icon Adapter Pack — provenance ledger

componentId: PACK-ICONS-ADAPTER
componentVersion: 0.1.0
originType: NEW_IMPLEMENTATION
sourceProjectOrRepo: riccardopinato/Design-App
factoryBaseline: riccardopinato/App-Factory-Core@e9507056601c4a6751510da4c5d1f61601a5dc25 (Master v27 ACTIVE)
externalReferenceRepo: google/material-design-icons
externalReferenceSha: 10ecc14790612ca8fd164e3f4ffe9c16fc50d5b7
externalReferenceLicense: Apache-2.0
otherSourcesConsulted: lucide-icons/lucide, tabler/tabler-icons, ionic-team/ionicons (all catalogued as reference)
sourceCodeCopied: false
sourceAssetsCopied: false
manifest: packs/icons/manifest/icons.json
generator: packs/icons/manifest/generate.py
flutterEntrypoint: packs/icons/flutter/lib/factory_icons.dart
composeEntrypoint: packs/icons/compose/src/main/kotlin/factory/icons/FactoryIconWidgets.kt
externalRuntimeDependenciesFlutter: 0
newStandaloneIconDependenciesCompose: 0
sizeImpact: No bundled files; actual app icon-font/SDK footprint not measured
validation: PR workflow pending; GitHub Actions icon-manifest, icon-flutter, icon-compose
knownLimitations: Android physical rendering, RTL gestures and consuming-app integration NOT VERIFIED
status: IMPLEMENTED_PENDING_VALIDATION

Design decisions:
- semantic key is the stable cross-stack contract;
- Material Icons Filled core used for both frameworks;
- back key uses RTL-friendly native icons;
- only 24 common Material-core icons are admitted in v1;
- icon-only actions require localized semantics and >=48dp targets;
- no wholesale Lucide/Tabler/Ionicons redistribution or mixing;
- generated mapping is checked deterministically in CI.

The generator's source is original. It references publicly documented Material
icon property names. Do not claim that running CI on Design-App proves
any consuming app's release build or runtime visual quality.
