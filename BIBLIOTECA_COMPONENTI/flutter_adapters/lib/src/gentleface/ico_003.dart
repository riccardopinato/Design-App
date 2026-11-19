// Gentleface "battery-charging" (line-round), MIT. https://gentleface.com/icons/battery-charging
import 'package:flutter/widgets.dart';

class BatteryChargingIcon extends StatelessWidget {
  const BatteryChargingIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _BatteryChargingIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _BatteryChargingIconPainter extends CustomPainter {
  _BatteryChargingIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(7, 3)
      ..lineTo(7, 7)
      ..lineTo(9, 7)
      ..lineTo(8.546, 7.757)
      ..lineTo(8.546, 7.757)
      ..lineTo(6, 12)
      ..lineTo(6, 8)
      ..lineTo(4, 8)
      ..lineTo(4.454, 7.243)
      ..lineTo(4.454, 7.243)
      ..lineTo(7, 3)
      ..close()
      ..moveTo(8, 5)
      ..lineTo(8, 4)
      ..lineTo(11, 4)
      ..cubicTo(11.254, 4, 11.5, 4.047, 11.736, 4.14)
      ..cubicTo(11.993, 4.242, 12.219, 4.391, 12.414, 4.586)
      ..cubicTo(12.609, 4.781, 12.758, 5.007, 12.86, 5.264)
      ..cubicTo(12.953, 5.5, 13, 5.746, 13, 6)
      ..lineTo(14.5, 6)
      ..cubicTo(14.641, 6, 14.759, 6.048, 14.856, 6.144)
      ..cubicTo(14.952, 6.241, 15, 6.359, 15, 6.5)
      ..lineTo(15, 9.5)
      ..cubicTo(15, 9.641, 14.952, 9.759, 14.856, 9.856)
      ..cubicTo(14.759, 9.952, 14.641, 10, 14.5, 10)
      ..lineTo(13, 10)
      ..cubicTo(13, 10.254, 12.953, 10.5, 12.86, 10.736)
      ..cubicTo(12.758, 10.993, 12.609, 11.219, 12.414, 11.414)
      ..cubicTo(12.219, 11.609, 11.993, 11.758, 11.736, 11.86)
      ..cubicTo(11.5, 11.953, 11.254, 12, 11, 12)
      ..lineTo(7.166, 12)
      ..lineTo(7.766, 11)
      ..lineTo(11, 11)
      ..cubicTo(11.276, 11, 11.512, 10.902, 11.707, 10.707)
      ..cubicTo(11.902, 10.512, 12, 10.276, 12, 10)
      ..lineTo(12, 6)
      ..cubicTo(12, 5.724, 11.902, 5.488, 11.707, 5.293)
      ..cubicTo(11.512, 5.098, 11.276, 5, 11, 5)
      ..lineTo(8, 5)
      ..close()
      ..moveTo(5, 12)
      ..lineTo(3, 12)
      ..cubicTo(2.746, 12, 2.5, 11.953, 2.264, 11.86)
      ..cubicTo(2.007, 11.758, 1.781, 11.609, 1.586, 11.414)
      ..cubicTo(1.391, 11.219, 1.242, 10.993, 1.14, 10.736)
      ..cubicTo(1.047, 10.5, 1, 10.254, 1, 10)
      ..lineTo(1, 6)
      ..cubicTo(1, 5.746, 1.047, 5.5, 1.14, 5.264)
      ..cubicTo(1.242, 5.007, 1.391, 4.781, 1.586, 4.586)
      ..cubicTo(1.781, 4.391, 2.007, 4.242, 2.264, 4.14)
      ..cubicTo(2.5, 4.047, 2.746, 4, 3, 4)
      ..lineTo(5.234, 4)
      ..lineTo(4.634, 5)
      ..lineTo(3, 5)
      ..cubicTo(2.724, 5, 2.488, 5.098, 2.293, 5.293)
      ..cubicTo(2.098, 5.488, 2, 5.724, 2, 6)
      ..lineTo(2, 10)
      ..cubicTo(2, 10.276, 2.098, 10.512, 2.293, 10.707)
      ..cubicTo(2.488, 10.902, 2.724, 11, 3, 11)
      ..lineTo(5, 11)
      ..lineTo(5, 12)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_BatteryChargingIconPainter old) => old.color != color;
}
