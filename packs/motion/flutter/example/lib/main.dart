import 'package:factory_motion/factory_motion.dart';
import 'package:flutter/material.dart';

void main() => runApp(const MotionShowcaseApp());

class MotionShowcaseApp extends StatefulWidget {
  const MotionShowcaseApp({super.key});

  @override
  State<MotionShowcaseApp> createState() => _MotionShowcaseAppState();
}

class _MotionShowcaseAppState extends State<MotionShowcaseApp> {
  bool dark = false;
  bool reduced = false;
  bool expanded = false;
  bool selected = false;
  bool completed = false;

  @override
  Widget build(BuildContext context) {
    const seed = Color(0xFF6A5ACD);

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Factory Motion Showcase',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: seed),
      ),
      darkTheme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: seed,
          brightness: Brightness.dark,
        ),
      ),
      themeMode: dark ? ThemeMode.dark : ThemeMode.light,
      builder: (context, child) => MediaQuery(
        data: MediaQuery.of(context).copyWith(disableAnimations: reduced),
        child: child!,
      ),
      home: Scaffold(
        appBar: AppBar(title: const Text('Factory Motion • Demo')),
        body: ListView(
          padding: const EdgeInsets.all(24),
          children: [
            SwitchListTile(
              title: const Text('Dark theme'),
              value: dark,
              onChanged: (value) => setState(() => dark = value),
            ),
            SwitchListTile(
              title: const Text('Reduce motion'),
              subtitle: const Text('Animations become immediate'),
              value: reduced,
              onChanged: (value) => setState(() => reduced = value),
            ),
            const SizedBox(height: 12),
            MotionSelectionTile(
              selected: selected,
              onTap: () => setState(() => selected = !selected),
              child: Text(selected ? 'Selected' : 'Tap to select'),
            ),
            const SizedBox(height: 24),
            FilledButton(
              onPressed: () => setState(() => expanded = !expanded),
              child: const Text('Toggle expanded details'),
            ),
            MotionExpand(
              expanded: expanded,
              child: const Padding(
                padding: EdgeInsets.all(16),
                child: Text('Additional details, without hidden focus targets.'),
              ),
            ),
            const SizedBox(height: 24),
            MotionSwap(
              motionKey: selected,
              effect: FactoryMotionEffect.fadeSlide,
              child: Text(
                selected ? 'The selection changed' : 'Nothing selected',
                style: Theme.of(context).textTheme.titleLarge,
              ),
            ),
            const SizedBox(height: 24),
            FilledButton.tonal(
              onPressed: () => setState(() => completed = !completed),
              child: const Text('Toggle completion'),
            ),
            const SizedBox(height: 12),
            Align(
              alignment: Alignment.centerLeft,
              child: MotionCompletionBadge(
                completed: completed,
                semanticLabel: 'Action completed',
              ),
            ),
            const SizedBox(height: 24),
            const MotionSkeleton(width: 250, height: 48),
          ],
        ),
      ),
    );
  }
}
