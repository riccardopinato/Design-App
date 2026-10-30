import 'package:audioplayers/audioplayers.dart';

import 'semantic_sound.dart';

/// Inject this contract in tests or when a product already owns audio playback.
abstract interface class SemanticSoundBackend {
  Future<void> play(SemanticSound sound, {required double volume});
  Future<void> stop();
  Future<void> dispose();
}

/// audioplayers is an optional dependency **only of this Flutter adapter**.
///
/// Uses a single player: a new UI cue interrupts the previous cue rather than
/// layering repeated feedback sounds. Platform audio focus is owned by the app.
class AudioplayersSemanticSoundBackend implements SemanticSoundBackend {
  AudioplayersSemanticSoundBackend({AudioPlayer? player})
      : _player = player ?? AudioPlayer() {
    _player.audioCache = AudioCache(prefix: '');
  }

  final AudioPlayer _player;

  @override
  Future<void> play(SemanticSound sound, {required double volume}) async {
    await _player.play(
      AssetSource(sound.assetKey, mimeType: 'audio/wav'),
      volume: volume,
    );
  }

  @override
  Future<void> stop() => _player.stop();

  @override
  Future<void> dispose() => _player.dispose();
}
