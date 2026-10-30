import 'package:factory_visual_qa_showcase/main.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  for (final size in [const Size(800, 360), const Size(360, 800)]) {
    testWidgets('showcase renders viewport $size and menu without overflow',
        (tester) async {
      tester.view.physicalSize = size;
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      await tester.pumpWidget(const VisualQaShowcase());
      await tester.pump(const Duration(milliseconds: 350));
      expect(tester.takeException(), isNull);
      await tester.tap(find.byTooltip('QA preview options'));
      await tester.pumpAndSettle();
      expect(find.text('Long localization'), findsWidgets);
      expect(tester.takeException(), isNull);
    });
  }
}
