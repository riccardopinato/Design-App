import 'package:factory_motion/factory_motion.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

Widget _host(Widget child, {bool reduced = false, bool dark = false}) {
  return MaterialApp(
    theme: ThemeData(
      useMaterial3: true,
      brightness: dark ? Brightness.dark : Brightness.light,
    ),
    home: MediaQuery(
      data: MediaQueryData(disableAnimations: reduced),
      child: Scaffold(body: Center(child: child)),
    ),
  );
}

void main() {
  testWidgets('policy respects the OS disableAnimations preference', (tester) async {
    late BuildContext captured;
    await tester.pumpWidget(_host(Builder(builder: (context) {
      captured = context;
      return const Text('Ready');
    }), reduced: true));

    expect(FactoryMotionPolicy.reduceMotion(captured), isTrue);
    expect(
      FactoryMotionPolicy.duration(captured, FactoryMotionTokens.standard),
      Duration.zero,
    );
  });

  testWidgets('policy respects accessible navigation preference', (tester) async {
    late BuildContext captured;
    await tester.pumpWidget(MaterialApp(
      home: MediaQuery(
        data: const MediaQueryData(accessibleNavigation: true),
        child: Builder(builder: (context) {
          captured = context;
          return const Text('Accessible');
        }),
      ),
    ));
    expect(FactoryMotionPolicy.reduceMotion(captured), isTrue);
  });

  for (final effect in FactoryMotionEffect.values) {
    testWidgets('MotionSwap renders new keyed content for $effect', (tester) async {
      Widget page(String label) => _host(MotionSwap(
            motionKey: label,
            effect: effect,
            child: Text(label),
          ));
      await tester.pumpWidget(page('One'));
      expect(find.text('One'), findsOneWidget);
      await tester.pumpWidget(page('Two'));
      await tester.pumpAndSettle();
      expect(find.text('Two'), findsOneWidget);
      expect(find.text('One'), findsNothing);
    });
  }

  testWidgets('MotionSwap bypasses AnimatedSwitcher for reduced motion',
      (tester) async {
    await tester.pumpWidget(_host(
      const MotionSwap(motionKey: 1, child: Text('One')),
      reduced: true,
    ));
    expect(find.byType(AnimatedSwitcher), findsNothing);
    await tester.pumpWidget(_host(
      const MotionSwap(motionKey: 2, child: Text('Two')),
      reduced: true,
    ));
    expect(find.text('Two'), findsOneWidget);
    expect(find.text('One'), findsNothing);
  });

  testWidgets('MotionExpand reveals and removes interactive descendants',
      (tester) async {
    Widget page(bool expanded) => _host(MotionExpand(
          expanded: expanded,
          child: TextButton(onPressed: () {}, child: const Text('Action')),
        ));
    await tester.pumpWidget(page(true));
    expect(find.text('Action'), findsOneWidget);
    await tester.pumpWidget(page(false));
    await tester.pumpAndSettle();
    expect(find.text('Action'), findsNothing);
  });

  testWidgets('MotionExpand removes collapsed content immediately with reduce',
      (tester) async {
    await tester.pumpWidget(_host(
      const MotionExpand(expanded: false, child: Text('Hidden')),
      reduced: true,
    ));
    expect(find.text('Hidden'), findsNothing);
    expect(find.byType(AnimatedSize), findsNothing);
  });

  testWidgets('completion badge announces localized success', (tester) async {
    final handle = tester.ensureSemantics();
    await tester.pumpWidget(_host(
      const MotionCompletionBadge(
        completed: true,
        semanticLabel: 'Salvataggio completato',
      ),
    ));
    expect(find.bySemanticsLabel('Salvataggio completato'), findsOneWidget);
    expect(find.byIcon(Icons.check_rounded), findsOneWidget);
    handle.dispose();
  });

  testWidgets('selection tile responds to tap and meets minimum height',
      (tester) async {
    bool selected = false;
    await tester.pumpWidget(_host(StatefulBuilder(builder: (context, setState) {
      return MotionSelectionTile(
        selected: selected,
        onTap: () => setState(() => selected = !selected),
        child: const Text('Choose'),
      );
    })));
    expect(tester.getSize(find.byType(MotionSelectionTile)).height,
        greaterThanOrEqualTo(48));
    await tester.tap(find.text('Choose'));
    await tester.pumpAndSettle();
    expect(selected, isTrue);
  });

  testWidgets('selection tile has minimum 48dp width with a tiny child',
      (tester) async {
    await tester.pumpWidget(_host(
      const Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          MotionSelectionTile(
            selected: false,
            child: SizedBox(width: 0, height: 0),
          ),
        ],
      ),
    ));
    final hitSize = tester.getSize(find.byType(MotionSelectionTile));
    expect(hitSize.width, greaterThanOrEqualTo(48));
    expect(hitSize.height, greaterThanOrEqualTo(48));
  });

  testWidgets('skeleton respects dimensions and optional semantics',
      (tester) async {
    final handle = tester.ensureSemantics();
    await tester.pumpWidget(_host(
      const MotionSkeleton(
        width: 140,
        height: 28,
        semanticLabel: 'Caricamento',
      ),
      dark: true,
    ));
    expect(find.bySemanticsLabel('Caricamento'), findsOneWidget);
    expect(tester.getSize(find.byType(MotionSkeleton)).width, 140);
    expect(tester.getSize(find.byType(MotionSkeleton)).height, 28);
    handle.dispose();
  });

  testWidgets('MotionHero disables flights under reduced motion',
      (tester) async {
    await tester.pumpWidget(_host(
      const MotionHero(tag: 'thumbnail', child: Text('Photo')),
      reduced: true,
    ));
    expect(tester.widget<HeroMode>(find.byType(HeroMode)).enabled, isFalse);
  });

  testWidgets('motion primitives work in dark mode', (tester) async {
    await tester.pumpWidget(_host(
      const Column(
        children: [
          MotionSelectionTile(selected: true, child: Text('Selected')),
          MotionCompletionBadge(completed: true, semanticLabel: 'Done'),
          MotionSkeleton(width: 64, height: 24),
        ],
      ),
      dark: true,
    ));
    expect(tester.takeException(), isNull);
    expect(find.text('Selected'), findsOneWidget);
  });
}
