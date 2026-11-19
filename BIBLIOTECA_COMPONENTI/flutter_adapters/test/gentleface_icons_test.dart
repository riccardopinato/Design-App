import 'package:design_app_flutter_adapters/design_app_flutter_adapters.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('28 Gentleface native Flutter icon sources, source-only QA', () {
    testWidgets('ICO-001 BellRingIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: BellRingIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(BellRingIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-002 CalendarIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: CalendarIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(CalendarIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-003 BatteryChargingIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: BatteryChargingIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(BatteryChargingIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-004 BatteryLowIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: BatteryLowIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(BatteryLowIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-005 DownloadIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: DownloadIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(DownloadIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-006 ExportIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: ExportIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(ExportIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-007 ImportIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: ImportIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(ImportIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-008 ImagesIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: ImagesIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(ImagesIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-009 VideoIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: VideoIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(VideoIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-010 BookmarkIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: BookmarkIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(BookmarkIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-011 SearchIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: SearchIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(SearchIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-012 AppsSparkleIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: AppsSparkleIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(AppsSparkleIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-013 LoaderIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: LoaderIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(LoaderIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-014 CheckIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: CheckIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(CheckIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-015 HeartPulseIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: HeartPulseIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(HeartPulseIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-016 MapPinIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: MapPinIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(MapPinIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-017 CloudIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: CloudIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(CloudIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-018 GaugeIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: GaugeIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(GaugeIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-019 StarIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: StarIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(StarIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-020 PlayIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: PlayIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(PlayIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-021 PauseIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: PauseIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(PauseIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-022 RepeatIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: RepeatIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(RepeatIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-023 EyeIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: EyeIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(EyeIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-024 ArchiveIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: ArchiveIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(ArchiveIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-025 MessagesIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: MessagesIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(MessagesIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-026 HomeIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: HomeIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(HomeIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-027 ShieldCheckIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: ShieldCheckIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(ShieldCheckIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
    testWidgets('ICO-028 LockIcon paints using the archived MIT source', (tester) async {
      await tester.pumpWidget(const Directionality(
        textDirection: TextDirection.ltr,
        child: Center(child: LockIcon(size: 28, color: Color(0xFF223344))),
      ));
      expect(find.byType(LockIcon), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
  });
}
