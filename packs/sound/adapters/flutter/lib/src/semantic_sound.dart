/// Stable sound meanings, not filenames or voice announcements.
///
/// The six bundled files are CC0, catalogued in
/// packs/sound/semantic/manifest.json in Design-App.
enum SemanticSound {
  selection('selection.wav'),
  success('success.wav'),
  warning('warning.wav'),
  error('error.wav'),
  completion('completion.wav'),
  notificationSoft('notification_soft.wav');

  const SemanticSound(this.fileName);

  final String fileName;

  /// Absolute Flutter bundle key for assets published from this package.
  String get assetKey => 'packages/factory_sound_flutter/assets/$fileName';
}
