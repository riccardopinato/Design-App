// Gentleface "download" (line-round), MIT. https://gentleface.com/icons/download
import 'package:flutter/widgets.dart';

class DownloadIcon extends StatelessWidget {
  const DownloadIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _DownloadIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _DownloadIconPainter extends CustomPainter {
  _DownloadIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(7.144, 1.144)
      ..cubicTo(7.241, 1.048, 7.359, 1, 7.5, 1)
      ..cubicTo(7.641, 1, 7.759, 1.048, 7.856, 1.144)
      ..cubicTo(7.952, 1.241, 8, 1.359, 8, 1.5)
      ..lineTo(8, 9.293)
      ..lineTo(11.146, 6.146)
      ..cubicTo(11.246, 6.047, 11.364, 5.997, 11.5, 5.997)
      ..cubicTo(11.636, 5.997, 11.754, 6.047, 11.854, 6.146)
      ..cubicTo(11.951, 6.244, 12, 6.362, 12, 6.5)
      ..cubicTo(12, 6.638, 11.951, 6.756, 11.854, 6.854)
      ..lineTo(7.854, 10.854)
      ..cubicTo(7.754, 10.953, 7.636, 11.003, 7.5, 11.003)
      ..cubicTo(7.364, 11.003, 7.246, 10.953, 7.146, 10.854)
      ..lineTo(3.146, 6.854)
      ..cubicTo(3.047, 6.754, 2.997, 6.636, 2.997, 6.5)
      ..cubicTo(2.997, 6.364, 3.047, 6.246, 3.146, 6.146)
      ..cubicTo(3.244, 6.049, 3.362, 6, 3.5, 6)
      ..cubicTo(3.638, 6, 3.756, 6.049, 3.854, 6.146)
      ..lineTo(7, 9.293)
      ..lineTo(7, 1.5)
      ..cubicTo(7, 1.359, 7.048, 1.241, 7.144, 1.144)
      ..close()
      ..moveTo(13, 9.5)
      ..cubicTo(13, 9.359, 13.048, 9.241, 13.144, 9.144)
      ..cubicTo(13.241, 9.048, 13.359, 9, 13.5, 9)
      ..cubicTo(13.641, 9, 13.759, 9.048, 13.856, 9.144)
      ..cubicTo(13.952, 9.241, 14, 9.359, 14, 9.5)
      ..lineTo(14, 13)
      ..cubicTo(14, 13.276, 13.902, 13.512, 13.707, 13.707)
      ..cubicTo(13.512, 13.902, 13.276, 14, 13, 14)
      ..lineTo(2, 14)
      ..cubicTo(1.724, 14, 1.488, 13.902, 1.293, 13.707)
      ..cubicTo(1.098, 13.512, 1, 13.276, 1, 13)
      ..lineTo(1, 9.5)
      ..cubicTo(1, 9.359, 1.048, 9.241, 1.144, 9.144)
      ..cubicTo(1.241, 9.048, 1.359, 9, 1.5, 9)
      ..cubicTo(1.641, 9, 1.759, 9.048, 1.856, 9.144)
      ..cubicTo(1.952, 9.241, 2, 9.359, 2, 9.5)
      ..lineTo(2, 13)
      ..lineTo(13, 13)
      ..lineTo(13, 9.5)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_DownloadIconPainter old) => old.color != color;
}
