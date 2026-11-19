// Gentleface "pause" (line-round), MIT. https://gentleface.com/icons/pause
import 'package:flutter/widgets.dart';

class PauseIcon extends StatelessWidget {
  const PauseIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _PauseIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _PauseIconPainter extends CustomPainter {
  _PauseIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(2.144, 2.144)
      ..cubicTo(2.241, 2.048, 2.359, 2, 2.5, 2)
      ..lineTo(5.5, 2)
      ..cubicTo(5.641, 2, 5.759, 2.048, 5.856, 2.144)
      ..cubicTo(5.952, 2.241, 6, 2.359, 6, 2.5)
      ..lineTo(6, 12.5)
      ..cubicTo(6, 12.641, 5.952, 12.759, 5.856, 12.856)
      ..cubicTo(5.759, 12.952, 5.641, 13, 5.5, 13)
      ..lineTo(2.5, 13)
      ..cubicTo(2.359, 13, 2.241, 12.952, 2.144, 12.856)
      ..cubicTo(2.048, 12.759, 2, 12.641, 2, 12.5)
      ..lineTo(2, 2.5)
      ..cubicTo(2, 2.359, 2.048, 2.241, 2.144, 2.144)
      ..close()
      ..moveTo(12.856, 2.144)
      ..cubicTo(12.952, 2.241, 13, 2.359, 13, 2.5)
      ..lineTo(13, 12.5)
      ..cubicTo(13, 12.641, 12.952, 12.759, 12.856, 12.856)
      ..cubicTo(12.759, 12.952, 12.641, 13, 12.5, 13)
      ..lineTo(9.5, 13)
      ..cubicTo(9.359, 13, 9.241, 12.952, 9.144, 12.856)
      ..cubicTo(9.048, 12.759, 9, 12.641, 9, 12.5)
      ..lineTo(9, 2.5)
      ..cubicTo(9, 2.359, 9.048, 2.241, 9.144, 2.144)
      ..cubicTo(9.241, 2.048, 9.359, 2, 9.5, 2)
      ..lineTo(12.5, 2)
      ..cubicTo(12.641, 2, 12.759, 2.048, 12.856, 2.144)
      ..close()
      ..moveTo(5, 12)
      ..lineTo(5, 3)
      ..lineTo(3, 3)
      ..lineTo(3, 12)
      ..lineTo(5, 12)
      ..close()
      ..moveTo(12, 3)
      ..lineTo(10, 3)
      ..lineTo(10, 12)
      ..lineTo(12, 12)
      ..lineTo(12, 3)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_PauseIconPainter old) => old.color != color;
}
