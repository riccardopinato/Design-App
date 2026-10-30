import 'package:factory_sound_flutter/factory_sound_flutter.dart';
import 'package:flutter/material.dart';

void main() => runApp(const SoundShowcaseApp());

class SoundShowcaseApp extends StatefulWidget {
  const SoundShowcaseApp({super.key});

  @override
  State<SoundShowcaseApp> createState() => _SoundShowcaseAppState();
}

class _SoundShowcaseAppState extends State<SoundShowcaseApp> {
  final SemanticSoundController controller = SemanticSoundController();
  String state = 'Sound is off by default';

  @override
  void dispose() {
    // Disposing a player is async; widget disposal has no async lifecycle.
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Factory Sound Preview',
      theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo),
      home: Scaffold(
        appBar: AppBar(title: const Text('Factory Semantic Sound')),
        body: ListView(
          padding: const EdgeInsets.all(24),
          children: [
            SwitchListTile(
              title: const Text('Enable optional UI sounds'),
              subtitle: const Text('All other app feedback stays visual'),
              value: controller.enabled,
              onChanged: (value) async {
                await controller.setEnabled(value);
                if (mounted) setState(() {});
              },
            ),
            Text('Volume: ${(controller.volume * 100).round()}%'),
            Slider(
              value: controller.volume,
              onChanged: (value) => setState(() => controller.setVolume(value)),
            ),
            for (final cue in SemanticSound.values)
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 6),
                child: FilledButton.tonal(
                  onPressed: () async {
                    final result = await controller.play(cue);
                    if (mounted) setState(() => state = '${cue.name}: ${result.name}');
                  },
                  child: Text('Preview ${cue.name}'),
                ),
              ),
            const SizedBox(height: 24),
            Text(state),
            const SizedBox(height: 24),
            const Text(
              'Preview only: UI sounds are never critical alarms. '
              'Test native playback, audio focus and volume on real devices '
              'before using in a production app.',
            ),
          ],
        ),
      ),
    );
  }
}
