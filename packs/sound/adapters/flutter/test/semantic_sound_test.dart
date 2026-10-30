import 'package:factory_sound_flutter/factory_sound_flutter.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

class FakeBackend implements SemanticSoundBackend {
  final calls = <SemanticSound>[];
  final volumes = <double>[];
  int stops = 0;
  int disposals = 0;
  bool failing = false;
  @override
  Future<void> play(SemanticSound sound, {required double volume}) async {
    if (failing) throw StateError('No audio device');
    calls.add(sound);
    volumes.add(volume);
  }
  @override
  Future<void> stop() async { stops++; }
  @override
  Future<void> dispose() async { disposals++; }
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('six unique semantic asset keys load correctly', () async {
    expect(SemanticSound.values.length, 6);
    final keys = SemanticSound.values.map((s) => s.assetKey).toSet();
    expect(keys.length, 6);
    for (final cue in SemanticSound.values) {
      final bytes = await rootBundle.load(cue.assetKey);
      expect(bytes.lengthInBytes, greaterThan(44));
      expect(bytes.getUint8(0), 82);
      expect(bytes.getUint8(8), 87);
    }
  });

  test('off by default, with no playback', () async {
    final backend = FakeBackend();
    final sound = SemanticSoundController(backend: backend);
    expect(sound.enabled, false);
    expect(await sound.play(SemanticSound.success), SoundPlayStatus.skippedDisabled);
    expect(backend.calls, isEmpty);
    await sound.dispose();
  });

  test('explicit opt in, bounded volume, and muting', () async {
    final backend = FakeBackend();
    final sound = SemanticSoundController(backend: backend, enabled: true, volume: 0.2);
    expect(await sound.play(SemanticSound.success), SoundPlayStatus.played);
    expect(backend.calls, [SemanticSound.success]);
    expect(backend.volumes, [0.2]);
    sound.setVolume(0);
    expect(await sound.play(SemanticSound.error), SoundPlayStatus.skippedMuted);
    await sound.setEnabled(false);
    expect(backend.stops, 1);
    expect(await sound.play(SemanticSound.error), SoundPlayStatus.skippedDisabled);
    await sound.dispose();
  });

  test('invalid volume throws RangeError', () async {
    final backend = FakeBackend();
    expect(() => SemanticSoundController(backend: backend, volume: double.nan),
        throwsRangeError);
    final sound = SemanticSoundController(backend: backend);
    expect(() => sound.setVolume(-0.1), throwsRangeError);
    expect(() => sound.setVolume(1.1), throwsRangeError);
    expect(() => sound.setVolume(double.infinity), throwsRangeError);
    await sound.dispose();
  });

  test('cooldown applies per cue, not across different events', () async {
    final backend = FakeBackend();
    var instant = DateTime.utc(2026, 10, 30);
    final sound = SemanticSoundController(
      backend: backend, enabled: true, now: () => instant);
    expect(await sound.play(SemanticSound.selection), SoundPlayStatus.played);
    expect(await sound.play(SemanticSound.selection), SoundPlayStatus.skippedCooldown);
    expect(await sound.play(SemanticSound.error), SoundPlayStatus.played);
    instant = instant.add(const Duration(milliseconds: 150));
    expect(await sound.play(SemanticSound.selection), SoundPlayStatus.played);
    expect(backend.calls.length, 3);
    await sound.dispose();
  });

  test('backend failure cannot crash the originating app action', () async {
    final backend = FakeBackend()..failing = true;
    final sound = SemanticSoundController(backend: backend, enabled: true);
    expect(await sound.play(SemanticSound.warning), SoundPlayStatus.failed);
    await sound.dispose();
  });

  test('disposal is idempotent', () async {
    final backend = FakeBackend();
    final sound = SemanticSoundController(backend: backend, enabled: true);
    await sound.dispose();
    await sound.dispose();
    expect(backend.disposals, 1);
    expect(await sound.play(SemanticSound.success), SoundPlayStatus.disposed);
  });
}
