// Gentleface "lock" (line-round), MIT. https://gentleface.com/icons/lock
import 'package:flutter/widgets.dart';

class LockIcon extends StatelessWidget {
  const LockIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _LockIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _LockIconPainter extends CustomPainter {
  _LockIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(12.86, 12.736)
      ..cubicTo(12.758, 12.993, 12.609, 13.219, 12.414, 13.414)
      ..cubicTo(12.219, 13.609, 11.993, 13.758, 11.736, 13.86)
      ..cubicTo(11.5, 13.953, 11.254, 14, 11, 14)
      ..lineTo(5, 14)
      ..cubicTo(4.746, 14, 4.5, 13.953, 4.264, 13.86)
      ..cubicTo(4.007, 13.758, 3.781, 13.609, 3.586, 13.414)
      ..cubicTo(3.391, 13.219, 3.242, 12.993, 3.14, 12.736)
      ..cubicTo(3.047, 12.5, 3, 12.254, 3, 12)
      ..lineTo(3, 9)
      ..cubicTo(3, 8.746, 3.047, 8.5, 3.14, 8.264)
      ..cubicTo(3.242, 8.007, 3.391, 7.781, 3.586, 7.586)
      ..cubicTo(3.781, 7.391, 4.007, 7.242, 4.264, 7.14)
      ..cubicTo(4.5, 7.047, 4.746, 7, 5, 7)
      ..lineTo(5, 5)
      ..cubicTo(5, 4.619, 5.07, 4.25, 5.211, 3.896)
      ..cubicTo(5.363, 3.511, 5.586, 3.172, 5.879, 2.879)
      ..cubicTo(6.172, 2.586, 6.511, 2.363, 6.896, 2.211)
      ..cubicTo(7.25, 2.07, 7.619, 2, 8, 2)
      ..cubicTo(8.381, 2, 8.75, 2.07, 9.104, 2.211)
      ..cubicTo(9.489, 2.363, 9.828, 2.586, 10.121, 2.879)
      ..cubicTo(10.414, 3.172, 10.637, 3.511, 10.789, 3.896)
      ..cubicTo(10.93, 4.25, 11, 4.619, 11, 5)
      ..lineTo(11, 7)
      ..cubicTo(11.254, 7, 11.5, 7.047, 11.736, 7.14)
      ..cubicTo(11.993, 7.242, 12.219, 7.391, 12.414, 7.586)
      ..cubicTo(12.609, 7.781, 12.758, 8.007, 12.86, 8.264)
      ..cubicTo(12.953, 8.5, 13, 8.746, 13, 9)
      ..lineTo(13, 12)
      ..cubicTo(13, 12.254, 12.953, 12.5, 12.86, 12.736)
      ..close()
      ..moveTo(10, 5)
      ..cubicTo(10, 4.746, 9.953, 4.5, 9.86, 4.264)
      ..cubicTo(9.758, 4.007, 9.609, 3.781, 9.414, 3.586)
      ..cubicTo(9.219, 3.391, 8.993, 3.242, 8.736, 3.14)
      ..cubicTo(8.5, 3.047, 8.254, 3, 8, 3)
      ..cubicTo(7.746, 3, 7.5, 3.047, 7.264, 3.14)
      ..cubicTo(7.007, 3.242, 6.781, 3.391, 6.586, 3.586)
      ..cubicTo(6.391, 3.781, 6.242, 4.007, 6.14, 4.264)
      ..cubicTo(6.047, 4.5, 6, 4.746, 6, 5)
      ..lineTo(6, 7)
      ..lineTo(10, 7)
      ..lineTo(10, 5)
      ..close()
      ..moveTo(4.293, 12.707)
      ..cubicTo(4.488, 12.902, 4.724, 13, 5, 13)
      ..lineTo(11, 13)
      ..cubicTo(11.276, 13, 11.512, 12.902, 11.707, 12.707)
      ..cubicTo(11.902, 12.512, 12, 12.276, 12, 12)
      ..lineTo(12, 9)
      ..cubicTo(12, 8.724, 11.902, 8.488, 11.707, 8.293)
      ..cubicTo(11.512, 8.098, 11.276, 8, 11, 8)
      ..lineTo(5, 8)
      ..cubicTo(4.724, 8, 4.488, 8.098, 4.293, 8.293)
      ..cubicTo(4.098, 8.488, 4, 8.724, 4, 9)
      ..lineTo(4, 12)
      ..cubicTo(4, 12.276, 4.098, 12.512, 4.293, 12.707)
      ..close()
      ..moveTo(8.707, 11.707)
      ..cubicTo(8.512, 11.902, 8.276, 12, 8, 12)
      ..cubicTo(7.724, 12, 7.488, 11.902, 7.293, 11.707)
      ..cubicTo(7.098, 11.512, 7, 11.276, 7, 11)
      ..lineTo(7, 10)
      ..cubicTo(7, 9.724, 7.098, 9.488, 7.293, 9.293)
      ..cubicTo(7.488, 9.098, 7.724, 9, 8, 9)
      ..cubicTo(8.276, 9, 8.512, 9.098, 8.707, 9.293)
      ..cubicTo(8.902, 9.488, 9, 9.724, 9, 10)
      ..lineTo(9, 11)
      ..cubicTo(9, 11.276, 8.902, 11.512, 8.707, 11.707)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_LockIconPainter old) => old.color != color;
}
