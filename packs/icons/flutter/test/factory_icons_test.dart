import 'package:factory_icons/factory_icons.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

Widget app(Widget child, {Brightness brightness = Brightness.light}) =>
    MaterialApp(
      theme: ThemeData(useMaterial3: true, brightness: brightness),
      home: Scaffold(body: Center(child: child)),
    );

void main() {
  test('all 24 semantic keys resolve to Material glyphs', () {
    expect(FactoryIconKey.values, hasLength(24));
    for (final key in FactoryIconKey.values) {
      expect(key.materialIcon.codePoint, greaterThan(0), reason: key.name);
    }
    expect(FactoryIconKey.back.materialIcon, Icons.arrow_back);
  });

  testWidgets('interactive icon has 48 dp min hit target and tooltip semantics',
      (tester) async {
    var taps = 0;
    final handle = tester.ensureSemantics();
    await tester.pumpWidget(app(FactoryIconButton(
      icon: FactoryIconKey.search,
      tooltip: 'Cerca nel diario',
      onPressed: () => taps++,
    )));
    expect(tester.getSize(find.byType(FactoryIconButton)).height, greaterThanOrEqualTo(48));
    expect(tester.getSize(find.byType(FactoryIconButton)).width, greaterThanOrEqualTo(48));
    expect(find.byTooltip('Cerca nel diario'), findsOneWidget);
    await tester.tap(find.byType(FactoryIconButton));
    expect(taps, 1);
    handle.dispose();
  });

  testWidgets('decorative icon does not provide redundant semantics', (tester) async {
    final handle = tester.ensureSemantics();
    await tester.pumpWidget(app(const FactoryIcon(icon: FactoryIconKey.calendar)));
    expect(find.byType(FactoryIcon), findsOneWidget);
    expect(find.bySemanticsLabel('calendar'), findsNothing);
    handle.dispose();
  });

  testWidgets('explicit semantic label can be localized for status icons',
      (tester) async {
    final handle = tester.ensureSemantics();
    await tester.pumpWidget(app(const FactoryIcon(
      icon: FactoryIconKey.warning, semanticLabel: 'Attenzione',
    )));
    expect(find.bySemanticsLabel('Attenzione'), findsOneWidget);
    handle.dispose();
  });

  testWidgets('light and dark themes both resolve semantic icons', (tester) async {
    for (final brightness in [Brightness.light, Brightness.dark]) {
      await tester.pumpWidget(app(
        const FactoryIcon(icon: FactoryIconKey.home),
        brightness: brightness,
      ));
      expect(find.byIcon(Icons.home), findsOneWidget);
      expect(tester.takeException(), isNull);
    }
  });

  testWidgets('disabled icon button stays noninteractive', (tester) async {
    await tester.pumpWidget(app(const FactoryIconButton(
      icon: FactoryIconKey.delete,
      tooltip: 'Elimina',
      onPressed: null,
    )));
    await tester.tap(find.byType(FactoryIconButton));
    expect(tester.takeException(), isNull);
  });

  testWidgets('RTL back arrow retains text-direction-aware Material glyph', (tester) async {
    await tester.pumpWidget(MaterialApp(
      home: Directionality(
        textDirection: TextDirection.rtl,
        child: const Scaffold(body: FactoryIcon(icon: FactoryIconKey.back)),
      ),
    ));
    expect(find.byIcon(Icons.arrow_back), findsOneWidget);
  });
}
