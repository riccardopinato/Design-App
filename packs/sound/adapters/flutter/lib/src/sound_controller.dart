import 'audio_backend.dart';
import 'semantic_sound.dart';

/// The status of a user-interface sound request.
///
/// A sound is always optional; app state and accessibility semantics must not
/// depend on successful sound playback.
enum SoundPlayStatus {
  played,
  skippedDisabled,
  skippedMuted,
  skippedCooldown,
  failed,
  disposed,
}

/// User-facing audio policy with an injectable backend and test clock.
///
/// No persisted preferences are stored here. The consuming app owns settings,
/// audio-session/focus rules, localization, and critical alarm delivery.
class SemanticSoundController {
  SemanticSoundController({
    SemanticSoundBackend? backend,
    bool enabled = false,
    double volume = 0.35,
    this.minRepeatInterval = const Duration(milliseconds: 120),
    DateTime Function()? now,
  })  : _backend = backend ?? AudioplayersSemanticSoundBackend(),
        _now = now ?? DateTime.now,
        _enabled = enabled,
        _volume = _validatedVolume(volume);

  final SemanticSoundBackend _backend;
  final DateTime Function() _now;
  final Duration minRepeatInterval;
  final Map<SemanticSound, DateTime> _lastRequested = {};
  bool _enabled;
  bool _disposed = false;
  double _volume;

  bool get enabled => _enabled;
  bool get isDisposed => _disposed;
  double get volume => _volume;

  static double _validatedVolume(double volume) {
    if (!volume.isFinite || volume < 0 || volume > 1) {
      throw RangeError.value(volume, 'volume', 'Must be finite and between 0 and 1');
    }
    return volume;
  }

  void setVolume(double volume) {
    if (_disposed) throw StateError('SemanticSoundController is disposed');
    _volume = _validatedVolume(volume);
  }

  /// Persist this setting in the app's own preferences if the user chooses to.
  ///
  /// Disabling sound also stops any cue currently playing.
  Future<void> setEnabled(bool enabled) async {
    if (_disposed) throw StateError('SemanticSoundController is disposed');
    _enabled = enabled;
    if (!enabled) await _backend.stop();
  }

  Future<SoundPlayStatus> play(SemanticSound sound) async {
    if (_disposed) return SoundPlayStatus.disposed;
    if (!_enabled) return SoundPlayStatus.skippedDisabled;
    if (_volume == 0) return SoundPlayStatus.skippedMuted;

    final now = _now();
    final previous = _lastRequested[sound];
    if (previous != null &&
        !now.isBefore(previous) &&
        now.difference(previous) < minRepeatInterval) {
      return SoundPlayStatus.skippedCooldown;
    }

    // Reserve the slot before asynchronous playback to prevent rapid double taps.
    _lastRequested[sound] = now;
    try {
      await _backend.play(sound, volume: _volume);
      return SoundPlayStatus.played;
    } catch (_) {
      // Audio must not crash the user's actual action. Callers can log this
      // status without routing exceptions through the widget tree.
      return SoundPlayStatus.failed;
    }
  }

  Future<void> stop() async {
    if (_disposed) return;
    await _backend.stop();
  }

  Future<void> dispose() async {
    if (_disposed) return;
    _disposed = true;
    await _backend.dispose();
  }
}
