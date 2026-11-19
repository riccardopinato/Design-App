// Gentleface "check" (line-round), MIT. https://gentleface.com/icons/check
import 'package:flutter/widgets.dart';

class CheckIcon extends StatelessWidget {
  const CheckIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _CheckIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _CheckIconPainter extends CustomPainter {
  _CheckIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(5.5, 10.793)
      ..lineTo(12.146, 4.146)
      ..cubicTo(12.246, 4.047, 12.364, 3.997, 12.5, 3.997)
      ..cubicTo(12.636, 3.997, 12.754, 4.047, 12.854, 4.146)
      ..cubicTo(12.951, 4.244, 13, 4.362, 13, 4.5)
      ..cubicTo(13, 4.638, 12.951, 4.756, 12.854, 4.854)
      ..lineTo(5.854, 11.854)
      ..cubicTo(5.754, 11.953, 5.636, 12.003, 5.5, 12.003)
      ..cubicTo(5.364, 12.003, 5.246, 11.953, 5.146, 11.854)
      ..lineTo(2.146, 8.854)
      ..cubicTo(2.047, 8.754, 1.997, 8.636, 1.997, 8.5)
      ..cubicTo(1.997, 8.364, 2.047, 8.246, 2.146, 8.146)
      ..cubicTo(2.244, 8.049, 2.362, 8, 2.5, 8)
      ..cubicTo(2.638, 8, 2.756, 8.049, 2.854, 8.146)
      ..lineTo(5.5, 10.793)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_CheckIconPainter old) => old.color != color;
}
