import 'dart:io';
import 'dart:typed_data';
import 'package:flutter/services.dart';

/// The Flutter test Ahem font makes fake block text. Load a real system
/// font explicitly, limited to Linux CI. No font files are vendored.
Future<void> loadLinuxVisualQaFonts() async {
  const path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
  final font = File(path);
  if (!font.existsSync()) {
    throw StateError('Missing $path; install fonts-dejavu-core on Linux.');
  }
  final bytes = await font.readAsBytes();
  final loader = FontLoader('Roboto')
    ..addFont(Future.value(ByteData.sublistView(Uint8List.fromList(bytes))));
  await loader.load();
}
