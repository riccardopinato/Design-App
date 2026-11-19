// Gentleface "apps-sparkle" (line-round), MIT. https://gentleface.com/icons/apps-sparkle
import 'package:flutter/widgets.dart';

class AppsSparkleIcon extends StatelessWidget {
  const AppsSparkleIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _AppsSparkleIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _AppsSparkleIconPainter extends CustomPainter {
  _AppsSparkleIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(0.439, 0.439)
      ..cubicTo(0.732, 0.146, 1.086, 0, 1.5, 0)
      ..cubicTo(1.914, 0, 2.268, 0.146, 2.561, 0.439)
      ..cubicTo(2.854, 0.732, 3, 1.086, 3, 1.5)
      ..cubicTo(3, 1.914, 2.854, 2.268, 2.561, 2.561)
      ..cubicTo(2.268, 2.854, 1.914, 3, 1.5, 3)
      ..cubicTo(1.086, 3, 0.732, 2.854, 0.439, 2.561)
      ..cubicTo(0.146, 2.268, 0, 1.914, 0, 1.5)
      ..cubicTo(0, 1.086, 0.146, 0.732, 0.439, 0.439)
      ..close()
      ..moveTo(5.439, 0.439)
      ..cubicTo(5.732, 0.146, 6.086, 0, 6.5, 0)
      ..cubicTo(6.914, 0, 7.268, 0.146, 7.561, 0.439)
      ..cubicTo(7.854, 0.732, 8, 1.086, 8, 1.5)
      ..cubicTo(8, 1.914, 7.854, 2.268, 7.561, 2.561)
      ..cubicTo(7.268, 2.854, 6.914, 3, 6.5, 3)
      ..cubicTo(6.086, 3, 5.732, 2.854, 5.439, 2.561)
      ..cubicTo(5.146, 2.268, 5, 1.914, 5, 1.5)
      ..cubicTo(5, 1.086, 5.146, 0.732, 5.439, 0.439)
      ..close()
      ..moveTo(12.561, 0.439)
      ..cubicTo(12.854, 0.732, 13, 1.086, 13, 1.5)
      ..cubicTo(13, 1.914, 12.854, 2.268, 12.561, 2.561)
      ..cubicTo(12.268, 2.854, 11.914, 3, 11.5, 3)
      ..cubicTo(11.086, 3, 10.732, 2.854, 10.439, 2.561)
      ..cubicTo(10.146, 2.268, 10, 1.914, 10, 1.5)
      ..cubicTo(10, 1.086, 10.146, 0.732, 10.439, 0.439)
      ..cubicTo(10.732, 0.146, 11.086, 0, 11.5, 0)
      ..cubicTo(11.914, 0, 12.268, 0.146, 12.561, 0.439)
      ..close()
      ..moveTo(2.561, 5.439)
      ..cubicTo(2.854, 5.732, 3, 6.086, 3, 6.5)
      ..cubicTo(3, 6.914, 2.854, 7.268, 2.561, 7.561)
      ..cubicTo(2.268, 7.854, 1.914, 8, 1.5, 8)
      ..cubicTo(1.086, 8, 0.732, 7.854, 0.439, 7.561)
      ..cubicTo(0.146, 7.268, 0, 6.914, 0, 6.5)
      ..cubicTo(0, 6.086, 0.146, 5.732, 0.439, 5.439)
      ..cubicTo(0.732, 5.146, 1.086, 5, 1.5, 5)
      ..cubicTo(1.914, 5, 2.268, 5.146, 2.561, 5.439)
      ..close()
      ..moveTo(7.561, 5.439)
      ..cubicTo(7.854, 5.732, 8, 6.086, 8, 6.5)
      ..cubicTo(8, 6.914, 7.854, 7.268, 7.561, 7.561)
      ..cubicTo(7.268, 7.854, 6.914, 8, 6.5, 8)
      ..cubicTo(6.086, 8, 5.732, 7.854, 5.439, 7.561)
      ..cubicTo(5.146, 7.268, 5, 6.914, 5, 6.5)
      ..cubicTo(5, 6.086, 5.146, 5.732, 5.439, 5.439)
      ..cubicTo(5.732, 5.146, 6.086, 5, 6.5, 5)
      ..cubicTo(6.914, 5, 7.268, 5.146, 7.561, 5.439)
      ..close()
      ..moveTo(10.439, 5.439)
      ..cubicTo(10.732, 5.146, 11.086, 5, 11.5, 5)
      ..cubicTo(11.914, 5, 12.268, 5.146, 12.561, 5.439)
      ..cubicTo(12.854, 5.732, 13, 6.086, 13, 6.5)
      ..cubicTo(13, 6.888, 12.872, 7.222, 12.615, 7.503)
      ..cubicTo(12.569, 7.296, 12.526, 7.074, 12.486, 6.836)
      ..cubicTo(12.396, 6.291, 11.88, 5.923, 11.336, 6.014)
      ..cubicTo(10.914, 6.084, 10.584, 6.414, 10.514, 6.836)
      ..cubicTo(10.474, 7.074, 10.431, 7.296, 10.385, 7.503)
      ..cubicTo(10.128, 7.222, 10, 6.888, 10, 6.5)
      ..cubicTo(10, 6.086, 10.146, 5.732, 10.439, 5.439)
      ..close()
      ..moveTo(11.5, 16)
      ..cubicTo(11, 13, 10, 12, 7, 11.5)
      ..cubicTo(10, 11, 11, 10, 11.5, 7)
      ..cubicTo(12, 10, 13, 11, 16, 11.5)
      ..cubicTo(13, 12, 12, 13, 11.5, 16)
      ..close()
      ..moveTo(0.439, 10.439)
      ..cubicTo(0.732, 10.146, 1.086, 10, 1.5, 10)
      ..cubicTo(1.914, 10, 2.268, 10.146, 2.561, 10.439)
      ..cubicTo(2.854, 10.732, 3, 11.086, 3, 11.5)
      ..cubicTo(3, 11.914, 2.854, 12.268, 2.561, 12.561)
      ..cubicTo(2.268, 12.854, 1.914, 13, 1.5, 13)
      ..cubicTo(1.086, 13, 0.732, 12.854, 0.439, 12.561)
      ..cubicTo(0.146, 12.268, 0, 11.914, 0, 11.5)
      ..cubicTo(0, 11.086, 0.146, 10.732, 0.439, 10.439)
      ..close()
      ..moveTo(6.836, 10.514)
      ..cubicTo(6.291, 10.604, 5.923, 11.12, 6.014, 11.664)
      ..cubicTo(6.084, 12.086, 6.414, 12.416, 6.836, 12.486)
      ..cubicTo(7.074, 12.526, 7.296, 12.569, 7.503, 12.615)
      ..cubicTo(7.222, 12.872, 6.888, 13, 6.5, 13)
      ..cubicTo(6.086, 13, 5.732, 12.854, 5.439, 12.561)
      ..cubicTo(5.146, 12.268, 5, 11.914, 5, 11.5)
      ..cubicTo(5, 11.086, 5.146, 10.732, 5.439, 10.439)
      ..cubicTo(5.732, 10.146, 6.086, 10, 6.5, 10)
      ..cubicTo(6.888, 10, 7.222, 10.128, 7.503, 10.385)
      ..cubicTo(7.296, 10.431, 7.074, 10.474, 6.836, 10.514)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_AppsSparkleIconPainter old) => old.color != color;
}
