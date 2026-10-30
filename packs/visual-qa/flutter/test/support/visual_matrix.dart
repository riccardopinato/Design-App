import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

/// Reusable screen scenarios, matched to the Factory responsive Visual QA Golden.
class VisualScenario {
  const VisualScenario({
    required this.id,
    required this.size,
    this.themeMode = ThemeMode.light,
    this.textScale = 1.0,
    this.insets = EdgeInsets.zero,
    this.padding = EdgeInsets.zero,
    this.longLocale = false,
    this.withAdSlot = false,
  });

  final String id;
  final Size size;
  final ThemeMode themeMode;
  final double textScale;
  final EdgeInsets insets;
  final EdgeInsets padding;
  final bool longLocale;
  final bool withAdSlot;

  static const smallPhone = VisualScenario(
    id: 'phone-small',
    size: Size(360, 800),
  );
  static const largePhone = VisualScenario(
    id: 'phone-large',
    size: Size(412, 915),
  );
  static const tablet = VisualScenario(
    id: 'tablet',
    size: Size(800, 1200),
  );
  static const landscape = VisualScenario(
    id: 'landscape',
    size: Size(800, 360),
  );
  static const largeText = VisualScenario(
    id: 'large-text',
    size: Size(360, 800),
    textScale: 1.6,
    longLocale: true,
  );
  static const extremeText = VisualScenario(
    id: 'extreme-text',
    size: Size(360, 800),
    textScale: 2.0,
    longLocale: true,
  );
  static const dark = VisualScenario(
    id: 'dark-phone',
    size: Size(360, 800),
    themeMode: ThemeMode.dark,
  );
  static const keyboardAndInsets = VisualScenario(
    id: 'keyboard-insets',
    size: Size(360, 800),
    padding: EdgeInsets.only(top: 30, bottom: 24),
    insets: EdgeInsets.only(bottom: 250),
  );
  static const banner = VisualScenario(
    id: 'banner',
    size: Size(360, 800),
    withAdSlot: true,
  );
}

/// Deterministic Flutter test host without application-specific design tokens.
///
/// IMPORTANT: call in a testWidgets callback; view teardown restores the host.
/// The callback can pass an actual product screen instead of the demo fixture.
Future<void> pumpVisualScenario(
  WidgetTester tester, {
  required VisualScenario scenario,
  required Widget child,
}) async {
  tester.view.devicePixelRatio = 1;
  tester.view.physicalSize = scenario.size;
  addTearDown(tester.view.resetPhysicalSize);
  addTearDown(tester.view.resetDevicePixelRatio);

  final data = MediaQueryData.fromView(tester.view).copyWith(
    size: scenario.size,
    textScaler: TextScaler.linear(scenario.textScale),
    padding: scenario.padding,
    viewInsets: scenario.insets,
    disableAnimations: true,
  );

  await tester.pumpWidget(MaterialApp(
    theme: ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
    ),
    darkTheme: ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(
        seedColor: Colors.indigo,
        brightness: Brightness.dark,
      ),
    ),
    themeMode: scenario.themeMode,
    home: MediaQuery(data: data, child: child),
  ));
  // Finite implicit widget animation durations settle; no indefinite
  // pumpAndSettle during a loading spinner.
  await tester.pump(const Duration(milliseconds: 350));
}

/// Fail on any framework exception (including RenderFlex overflow).
void expectNoVisualException(WidgetTester tester) {
  final exception = tester.takeException();
  expect(exception, isNull, reason: 'Unexpected layout/paint error: $exception');
}
