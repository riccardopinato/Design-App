import 'dart:io';
import 'package:flutter/services.dart';

/// Golden tests otherwise use Ahem rectangles instead of real text/icons.
/// Deterministic Linux fixture fonts only; not shipped in product packages.
Future<void> loadLinuxVisualQaFonts() async {
  Future<void> load(String family, File file) async {
    if (!file.existsSync()) {
      throw StateError('Missing golden-test font: ${file.path}');
    }
    final bytes = await file.readAsBytes();
    await (FontLoader(family)
          ..addFont(Future.value(ByteData.sublistView(bytes))))
        .load();
  }

  await load('Roboto', File('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'));

  // uses-material-design bundles icon fonts in real Flutter apps; widget
  // tests additionally need the actual engine SDK OTF registered.
  final flutterSdk = Platform.environment['FLUTTER_ROOT'] ??
      File(Platform.resolvedExecutable).parent.parent.parent.parent.parent.path;
  final icons = File(
    '$flutterSdk/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf',
  );
  await load('MaterialIcons', icons);
}
