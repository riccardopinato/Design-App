// Gentleface "bookmark" (line-round), MIT. https://gentleface.com/icons/bookmark
import 'package:flutter/widgets.dart';

class BookmarkIcon extends StatelessWidget {
  const BookmarkIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _BookmarkIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _BookmarkIconPainter extends CustomPainter {
  _BookmarkIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(11.856, 14.856)
      ..cubicTo(11.759, 14.952, 11.641, 15, 11.5, 15)
      ..cubicTo(11.362, 15, 11.244, 14.951, 11.146, 14.854)
      ..lineTo(7.5, 11.207)
      ..lineTo(3.854, 14.854)
      ..cubicTo(3.754, 14.953, 3.636, 15.003, 3.5, 15.003)
      ..cubicTo(3.364, 15.003, 3.246, 14.953, 3.146, 14.854)
      ..cubicTo(3.049, 14.756, 3, 14.638, 3, 14.5)
      ..lineTo(3, 3)
      ..cubicTo(3, 2.746, 3.047, 2.5, 3.14, 2.264)
      ..cubicTo(3.242, 2.007, 3.391, 1.781, 3.586, 1.586)
      ..cubicTo(3.781, 1.391, 4.007, 1.242, 4.264, 1.14)
      ..cubicTo(4.5, 1.047, 4.746, 1, 5, 1)
      ..lineTo(10, 1)
      ..cubicTo(10.254, 1, 10.5, 1.047, 10.736, 1.14)
      ..cubicTo(10.993, 1.242, 11.219, 1.391, 11.414, 1.586)
      ..cubicTo(11.609, 1.781, 11.758, 2.007, 11.86, 2.264)
      ..cubicTo(11.953, 2.5, 12, 2.746, 12, 3)
      ..lineTo(12, 14.5)
      ..cubicTo(12, 14.641, 11.952, 14.759, 11.856, 14.856)
      ..close()
      ..moveTo(6.793, 10.5)
      ..cubicTo(6.988, 10.305, 7.224, 10.207, 7.5, 10.207)
      ..cubicTo(7.776, 10.207, 8.012, 10.305, 8.207, 10.5)
      ..lineTo(11, 13.293)
      ..lineTo(11, 3)
      ..cubicTo(11, 2.724, 10.902, 2.488, 10.707, 2.293)
      ..cubicTo(10.512, 2.098, 10.276, 2, 10, 2)
      ..lineTo(5, 2)
      ..cubicTo(4.724, 2, 4.488, 2.098, 4.293, 2.293)
      ..cubicTo(4.098, 2.488, 4, 2.724, 4, 3)
      ..lineTo(4, 13.293)
      ..lineTo(6.793, 10.5)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_BookmarkIconPainter old) => old.color != color;
}
