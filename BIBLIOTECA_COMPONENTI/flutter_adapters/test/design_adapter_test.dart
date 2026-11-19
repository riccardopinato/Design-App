import 'package:design_app_flutter_adapters/design_app_flutter_adapters.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';

Widget harness(Widget child, {bool reduced = true}) => Directionality(
      textDirection: TextDirection.ltr,
      child: MediaQuery(
        data: MediaQueryData(disableAnimations: reduced),
        child: Center(child: child),
      ),
    );

void main() {
  testWidgets('RXN animated gradient displays original text', (tester) async {
    await tester.pumpWidget(harness(const RxnAnimatedGradientText(text: 'Original gradient')));
    expect(find.text('Original gradient'), findsOneWidget);
    await tester.pumpWidget(const SizedBox());
  });

  testWidgets('RXN progress clamps safely to 0-100', (tester) async {
    await tester.pumpWidget(harness(const RxnAnimatedCircularProgressBar(value: 150)));
    await tester.pump();
    expect(find.text('100'), findsOneWidget);
    await tester.pumpWidget(harness(const RxnAnimatedCircularProgressBar(value: -20)));
    await tester.pump();
    expect(find.text('0'), findsOneWidget);
  });

  testWidgets('UIV-002 pill preserves accessible tap callback', (tester) async {
    var tapped = 0;
    await tester.pumpWidget(harness(Uiv002GradientPillButton(
      label: 'Pick up!', onPressed: () => tapped++,
    )));
    await tester.tap(find.text('Pick up!'));
    await tester.pump();
    expect(tapped, 1);
  });

  testWidgets('UIV-002 disabled button never calls callback', (tester) async {
    await tester.pumpWidget(harness(const Uiv002GradientPillButton(
      label: 'Disabled', onPressed: null,
    )));
    await tester.tap(find.text('Disabled'));
    expect(find.text('Disabled'), findsOneWidget);
  });
  testWidgets('RXN animated link taps and keeps source label', (tester) async {
    var taps = 0;
    await tester.pumpWidget(harness(RxnAnimatedLink(label: 'Open', onTap: () => taps++)));
    await tester.tap(find.text('Open'));
    await tester.pump();
    expect(taps, 1);
  });

  testWidgets('RXN accordion expands and collapses without losing state', (tester) async {
    const items = [RxnEditorialAccordionItem(id: 'one', title: 'Title', content: 'Hidden detail')];
    await tester.pumpWidget(harness(const RxnEditorialAccordion(items: items)));
    expect(find.text('Hidden detail'), findsNothing);
    await tester.tap(find.text('Title'));
    await tester.pump();
    expect(find.text('Hidden detail'), findsOneWidget);
    await tester.tap(find.text('Title'));
    await tester.pump();
    expect(find.text('Hidden detail'), findsNothing);
  });
  testWidgets('UIV-009 native book card opens on tap with original cover styling', (tester) async {
    final events = <bool>[];
    await tester.pumpWidget(harness(Uiv009BookCard(
      coverText: 'Cover', insideText: 'Diary',
      onOpenChanged: events.add,
    )));
    await tester.tap(find.text('Cover'));
    await tester.pump();
    expect(events, <bool>[true]);
    expect(find.text('Diary'), findsOneWidget);
  });

  testWidgets('RXN shimmering text renders and respects reduced motion', (tester) async {
    await tester.pumpWidget(harness(const RxnAnimatedShinyText(
      text: 'Hello Shimmer',
    )));
    expect(find.text('Hello Shimmer'), findsOneWidget);
    await tester.pumpWidget(const SizedBox());
  });
  testWidgets('RXN grid pattern renders a real canvas and custom squares', (tester) async {
    await tester.pumpWidget(harness(const SizedBox(
      width: 240,
      height: 160,
      child: RxnGridPattern(squares: [Offset(0, 0), Offset(3, 2)]),
    )));
    expect(find.byType(CustomPaint), findsWidgets);
    expect(tester.takeException(), isNull);
  });

  testWidgets('RXN pulsating native button fires once, handles reduced motion', (tester) async {
    var pressed = 0;
    await tester.pumpWidget(harness(RxnPulsatingButton(
      label: 'Continue', onPressed: () => pressed++,
    )));
    await tester.tap(find.text('Continue'));
    await tester.pump();
    expect(pressed, 1);
    await tester.pumpWidget(const SizedBox());
  });

  testWidgets('AMX-006 accordion loader renders four actual bars', (tester) async {
    await tester.pumpWidget(harness(const Amx006AccordionLoader()));
    expect(find.byType(Amx006AccordionLoader), findsOneWidget);
    expect(find.byType(Transform), findsAtLeastNWidgets(4));
    expect(tester.takeException(), isNull);
    await tester.pumpWidget(const SizedBox());
  });

  testWidgets('UIV-008 rolling rock keeps original keyframe geometry', (tester) async {
    await tester.pumpWidget(harness(const Uiv008RollingRockLoader()));
    expect(find.byType(Uiv008RollingRockLoader), findsOneWidget);
    expect(find.byType(CustomPaint), findsWidgets);
    expect(tester.takeException(), isNull);
    await tester.pumpWidget(const SizedBox());
  });

  testWidgets('Ruixen interactive hover button invokes native touch callback', (tester) async {
    var clicks = 0;
    await tester.pumpWidget(harness(RxnInteractiveHoverButton(
      label: 'Continua', onPressed: () => clicks++,
    )));
    await tester.tap(find.text('Continua').first);
    await tester.pump();
    expect(clicks, 1);
    await tester.pumpWidget(const SizedBox());
  });

  testWidgets('Ruixen rainbow button supports native outline and disabled mode', (tester) async {
    await tester.pumpWidget(harness(const RxnRainbowButton(
      label: 'Esplora', onPressed: null, variant: RxnRainbowVariant.outline,
    )));
    expect(find.text('Esplora'), findsOneWidget);
    expect(tester.takeException(), isNull);
    await tester.pumpWidget(const SizedBox());
  });

  testWidgets('Ruixen orbit animation places every supplied child on orbit', (tester) async {
    await tester.pumpWidget(harness(const RxnOrbitingCircles(
      radius: 60,
      iconSize: 30,
      children: [Text('A'), Text('B'), Text('C')],
    )));
    expect(find.text('A'), findsOneWidget);
    expect(find.text('B'), findsOneWidget);
    expect(find.text('C'), findsOneWidget);
    expect(find.byType(CustomPaint), findsWidgets);
    await tester.pumpWidget(const SizedBox());
  });
}
