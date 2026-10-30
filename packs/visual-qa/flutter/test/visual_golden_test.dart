import 'package:factory_visual_qa/factory_visual_qa.dart';
import 'package:flutter_test/flutter_test.dart';

import 'support/visual_matrix.dart';
import 'support/real_fonts.dart';

void main() {
  setUpAll(loadLinuxVisualQaFonts);
  final snapshots = [
    (
      id: 'phone-light-content',
      scenario: VisualScenario.smallPhone,
      state: QaUiState.content,
    ),
    (
      id: 'phone-dark-empty',
      scenario: VisualScenario.dark,
      state: QaUiState.empty,
    ),
    (
      id: 'tablet-content',
      scenario: VisualScenario.tablet,
      state: QaUiState.content,
    ),
    (
      id: 'large-text-error',
      scenario: VisualScenario.largeText,
      state: QaUiState.error,
    ),
  ];

  for (final shot in snapshots) {
    testWidgets('pixel baseline: ${shot.id}', (tester) async {
      await pumpVisualScenario(
        tester,
        scenario: shot.scenario,
        child: QaFixture(
          state: shot.state,
          longLocale: shot.scenario.longLocale,
          withAdSlot: shot.scenario.withAdSlot,
        ),
      );
      expectNoVisualException(tester);
      await expectLater(
        find.byType(QaFixture),
        matchesGoldenFile('goldens/${shot.id}.png'),
      );
    });
  }
}
