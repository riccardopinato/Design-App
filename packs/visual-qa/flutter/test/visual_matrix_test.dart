import 'package:factory_visual_qa/factory_visual_qa.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'support/visual_matrix.dart';

void main() {
  final scenarios = [
    VisualScenario.smallPhone,
    VisualScenario.largePhone,
    VisualScenario.tablet,
    VisualScenario.landscape,
    VisualScenario.largeText,
    VisualScenario.extremeText,
    VisualScenario.dark,
    VisualScenario.keyboardAndInsets,
    VisualScenario.banner,
  ];

  for (final scenario in scenarios) {
    for (final state in QaUiState.values) {
      testWidgets('no overflow: ${scenario.id} / ${state.name}', (tester) async {
        await pumpVisualScenario(
          tester,
          scenario: scenario,
          child: QaFixture(
            state: state,
            longLocale: scenario.longLocale,
            withAdSlot: scenario.withAdSlot,
          ),
        );
        expectNoVisualException(tester);
      });
    }
  }

  testWidgets('semantic retry control appears on error', (tester) async {
    await pumpVisualScenario(
      tester,
      scenario: VisualScenario.smallPhone,
      child: const QaFixture(state: QaUiState.error),
    );
    expect(find.text('Unable to load'), findsOneWidget);
    expect(find.text('Try again'), findsOneWidget);
    expectNoVisualException(tester);
  });

  testWidgets('reserved banner stays visible in compact layout', (tester) async {
    await pumpVisualScenario(
      tester,
      scenario: VisualScenario.banner,
      child: const QaFixture(state: QaUiState.content, withAdSlot: true),
    );
    expect(find.text('Reserved banner slot'), findsOneWidget);
    final bannerBottom = tester.getBottomLeft(find.text('Reserved banner slot')).dy;
    final navTop = tester.getTopLeft(find.byType(NavigationBar)).dy;
    expect(bannerBottom, lessThan(navTop));
    expectNoVisualException(tester);
  });
}
