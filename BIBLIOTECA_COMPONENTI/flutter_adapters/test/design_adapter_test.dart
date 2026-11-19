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
}
