// Gentleface "archive" (line-round), MIT. https://gentleface.com/icons/archive
import 'package:flutter/widgets.dart';

class ArchiveIcon extends StatelessWidget {
  const ArchiveIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _ArchiveIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _ArchiveIconPainter extends CustomPainter {
  _ArchiveIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(14.707, 5.707)
      ..cubicTo(14.512, 5.902, 14.276, 6, 14, 6)
      ..lineTo(14, 13)
      ..cubicTo(14, 13.276, 13.902, 13.512, 13.707, 13.707)
      ..cubicTo(13.512, 13.902, 13.276, 14, 13, 14)
      ..lineTo(3, 14)
      ..cubicTo(2.724, 14, 2.488, 13.902, 2.293, 13.707)
      ..cubicTo(2.098, 13.512, 2, 13.276, 2, 13)
      ..lineTo(2, 6)
      ..cubicTo(1.724, 6, 1.488, 5.902, 1.293, 5.707)
      ..cubicTo(1.098, 5.512, 1, 5.276, 1, 5)
      ..lineTo(1, 4)
      ..cubicTo(1, 3.746, 1.047, 3.5, 1.14, 3.264)
      ..cubicTo(1.242, 3.007, 1.391, 2.781, 1.586, 2.586)
      ..cubicTo(1.781, 2.391, 2.007, 2.242, 2.264, 2.14)
      ..cubicTo(2.5, 2.047, 2.746, 2, 3, 2)
      ..lineTo(13, 2)
      ..cubicTo(13.254, 2, 13.5, 2.047, 13.736, 2.14)
      ..cubicTo(13.993, 2.242, 14.219, 2.391, 14.414, 2.586)
      ..cubicTo(14.609, 2.781, 14.758, 3.007, 14.86, 3.264)
      ..cubicTo(14.953, 3.5, 15, 3.746, 15, 4)
      ..lineTo(15, 5)
      ..cubicTo(15, 5.276, 14.902, 5.512, 14.707, 5.707)
      ..close()
      ..moveTo(2.5, 5.131)
      ..cubicTo(2.584, 5.047, 2.699, 5, 2.818, 5)
      ..lineTo(13.182, 5)
      ..cubicTo(13.301, 5, 13.416, 5.047, 13.5, 5.131)
      ..cubicTo(13.649, 5.044, 13.815, 5, 14, 5)
      ..lineTo(14, 4)
      ..cubicTo(14, 3.724, 13.902, 3.488, 13.707, 3.293)
      ..cubicTo(13.512, 3.098, 13.276, 3, 13, 3)
      ..lineTo(3, 3)
      ..cubicTo(2.724, 3, 2.488, 3.098, 2.293, 3.293)
      ..cubicTo(2.098, 3.488, 2, 3.724, 2, 4)
      ..lineTo(2, 5)
      ..cubicTo(2.185, 5, 2.351, 5.044, 2.5, 5.131)
      ..close()
      ..moveTo(13, 13)
      ..lineTo(13, 6)
      ..lineTo(3, 6)
      ..lineTo(3, 13)
      ..lineTo(13, 13)
      ..close()
      ..moveTo(9.856, 8.144)
      ..cubicTo(9.952, 8.241, 10, 8.359, 10, 8.5)
      ..cubicTo(10, 8.641, 9.952, 8.759, 9.856, 8.856)
      ..cubicTo(9.759, 8.952, 9.641, 9, 9.5, 9)
      ..lineTo(6.5, 9)
      ..cubicTo(6.359, 9, 6.241, 8.952, 6.144, 8.856)
      ..cubicTo(6.048, 8.759, 6, 8.641, 6, 8.5)
      ..cubicTo(6, 8.359, 6.048, 8.241, 6.144, 8.144)
      ..cubicTo(6.241, 8.048, 6.359, 8, 6.5, 8)
      ..lineTo(9.5, 8)
      ..cubicTo(9.641, 8, 9.759, 8.048, 9.856, 8.144)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_ArchiveIconPainter old) => old.color != color;
}
