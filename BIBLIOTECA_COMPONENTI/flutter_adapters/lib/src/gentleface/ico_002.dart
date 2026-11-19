// Gentleface "calendar" (line-round), MIT. https://gentleface.com/icons/calendar
import 'package:flutter/widgets.dart';

class CalendarIcon extends StatelessWidget {
  const CalendarIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _CalendarIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _CalendarIconPainter extends CustomPainter {
  _CalendarIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(10, 1.5)
      ..cubicTo(10, 1.359, 10.048, 1.241, 10.144, 1.144)
      ..cubicTo(10.241, 1.048, 10.359, 1, 10.5, 1)
      ..cubicTo(10.641, 1, 10.759, 1.048, 10.856, 1.144)
      ..cubicTo(10.952, 1.241, 11, 1.359, 11, 1.5)
      ..lineTo(11, 2)
      ..lineTo(12, 2)
      ..cubicTo(12.254, 2, 12.5, 2.047, 12.736, 2.14)
      ..cubicTo(12.993, 2.242, 13.219, 2.391, 13.414, 2.586)
      ..cubicTo(13.609, 2.781, 13.758, 3.007, 13.86, 3.264)
      ..cubicTo(13.953, 3.5, 14, 3.746, 14, 4)
      ..lineTo(14, 13)
      ..cubicTo(14, 13.254, 13.953, 13.5, 13.86, 13.736)
      ..cubicTo(13.758, 13.993, 13.609, 14.219, 13.414, 14.414)
      ..cubicTo(13.219, 14.609, 12.993, 14.758, 12.736, 14.86)
      ..cubicTo(12.5, 14.953, 12.254, 15, 12, 15)
      ..lineTo(4, 15)
      ..cubicTo(3.746, 15, 3.5, 14.953, 3.264, 14.86)
      ..cubicTo(3.007, 14.758, 2.781, 14.609, 2.586, 14.414)
      ..cubicTo(2.391, 14.219, 2.242, 13.993, 2.14, 13.736)
      ..cubicTo(2.047, 13.5, 2, 13.254, 2, 13)
      ..lineTo(2, 4)
      ..cubicTo(2, 3.746, 2.047, 3.5, 2.14, 3.264)
      ..cubicTo(2.242, 3.007, 2.391, 2.781, 2.586, 2.586)
      ..cubicTo(2.781, 2.391, 3.007, 2.242, 3.264, 2.14)
      ..cubicTo(3.5, 2.047, 3.746, 2, 4, 2)
      ..lineTo(5, 2)
      ..lineTo(5, 1.5)
      ..cubicTo(5, 1.359, 5.048, 1.241, 5.144, 1.144)
      ..cubicTo(5.241, 1.048, 5.359, 1, 5.5, 1)
      ..cubicTo(5.641, 1, 5.759, 1.048, 5.856, 1.144)
      ..cubicTo(5.952, 1.241, 6, 1.359, 6, 1.5)
      ..lineTo(6, 2)
      ..lineTo(10, 2)
      ..lineTo(10, 1.5)
      ..close()
      ..moveTo(3.293, 3.293)
      ..cubicTo(3.098, 3.488, 3, 3.724, 3, 4)
      ..lineTo(3, 5)
      ..lineTo(13, 5)
      ..lineTo(13, 4)
      ..cubicTo(13, 3.724, 12.902, 3.488, 12.707, 3.293)
      ..cubicTo(12.512, 3.098, 12.276, 3, 12, 3)
      ..lineTo(11, 3)
      ..lineTo(11, 3.5)
      ..cubicTo(11, 3.641, 10.952, 3.759, 10.856, 3.856)
      ..cubicTo(10.759, 3.952, 10.641, 4, 10.5, 4)
      ..cubicTo(10.359, 4, 10.241, 3.952, 10.144, 3.856)
      ..cubicTo(10.048, 3.759, 10, 3.641, 10, 3.5)
      ..lineTo(10, 3)
      ..lineTo(6, 3)
      ..lineTo(6, 3.5)
      ..cubicTo(6, 3.641, 5.952, 3.759, 5.856, 3.856)
      ..cubicTo(5.759, 3.952, 5.641, 4, 5.5, 4)
      ..cubicTo(5.359, 4, 5.241, 3.952, 5.144, 3.856)
      ..cubicTo(5.048, 3.759, 5, 3.641, 5, 3.5)
      ..lineTo(5, 3)
      ..lineTo(4, 3)
      ..cubicTo(3.724, 3, 3.488, 3.098, 3.293, 3.293)
      ..close()
      ..moveTo(3.293, 13.707)
      ..cubicTo(3.488, 13.902, 3.724, 14, 4, 14)
      ..lineTo(12, 14)
      ..cubicTo(12.276, 14, 12.512, 13.902, 12.707, 13.707)
      ..cubicTo(12.902, 13.512, 13, 13.276, 13, 13)
      ..lineTo(13, 6)
      ..lineTo(3, 6)
      ..lineTo(3, 13)
      ..cubicTo(3, 13.276, 3.098, 13.512, 3.293, 13.707)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_CalendarIconPainter old) => old.color != color;
}
