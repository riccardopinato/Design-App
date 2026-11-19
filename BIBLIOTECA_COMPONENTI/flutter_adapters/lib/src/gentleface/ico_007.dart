// Gentleface "import" (line-round), MIT. https://gentleface.com/icons/import
import 'package:flutter/widgets.dart';

class ImportIcon extends StatelessWidget {
  const ImportIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _ImportIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _ImportIconPainter extends CustomPainter {
  _ImportIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(2.14, 3.264)
      ..cubicTo(2.242, 3.007, 2.391, 2.781, 2.586, 2.586)
      ..cubicTo(2.781, 2.391, 3.007, 2.242, 3.264, 2.14)
      ..cubicTo(3.5, 2.047, 3.746, 2, 4, 2)
      ..lineTo(12, 2)
      ..cubicTo(12.254, 2, 12.5, 2.047, 12.736, 2.14)
      ..cubicTo(12.993, 2.242, 13.219, 2.391, 13.414, 2.586)
      ..cubicTo(13.609, 2.781, 13.758, 3.007, 13.86, 3.264)
      ..cubicTo(13.953, 3.5, 14, 3.746, 14, 4)
      ..lineTo(14, 12)
      ..cubicTo(14, 12.254, 13.953, 12.5, 13.86, 12.736)
      ..cubicTo(13.758, 12.993, 13.609, 13.219, 13.414, 13.414)
      ..cubicTo(13.219, 13.609, 12.993, 13.758, 12.736, 13.86)
      ..cubicTo(12.5, 13.953, 12.254, 14, 12, 14)
      ..lineTo(4, 14)
      ..cubicTo(3.746, 14, 3.5, 13.953, 3.264, 13.86)
      ..cubicTo(3.007, 13.758, 2.781, 13.609, 2.586, 13.414)
      ..cubicTo(2.391, 13.219, 2.242, 12.993, 2.14, 12.736)
      ..cubicTo(2.047, 12.5, 2, 12.254, 2, 12)
      ..lineTo(2, 9.5)
      ..cubicTo(2, 9.359, 2.048, 9.241, 2.144, 9.144)
      ..cubicTo(2.241, 9.048, 2.359, 9, 2.5, 9)
      ..cubicTo(2.641, 9, 2.759, 9.048, 2.856, 9.144)
      ..cubicTo(2.952, 9.241, 3, 9.359, 3, 9.5)
      ..lineTo(3, 12)
      ..cubicTo(3, 12.276, 3.098, 12.512, 3.293, 12.707)
      ..cubicTo(3.488, 12.902, 3.724, 13, 4, 13)
      ..lineTo(12, 13)
      ..cubicTo(12.276, 13, 12.512, 12.902, 12.707, 12.707)
      ..cubicTo(12.902, 12.512, 13, 12.276, 13, 12)
      ..lineTo(13, 4)
      ..cubicTo(13, 3.724, 12.902, 3.488, 12.707, 3.293)
      ..cubicTo(12.512, 3.098, 12.276, 3, 12, 3)
      ..lineTo(4, 3)
      ..cubicTo(3.724, 3, 3.488, 3.098, 3.293, 3.293)
      ..cubicTo(3.098, 3.488, 3, 3.724, 3, 4)
      ..lineTo(3, 5.5)
      ..cubicTo(3, 5.641, 2.952, 5.759, 2.856, 5.856)
      ..cubicTo(2.759, 5.952, 2.641, 6, 2.5, 6)
      ..cubicTo(2.359, 6, 2.241, 5.952, 2.144, 5.856)
      ..cubicTo(2.048, 5.759, 2, 5.641, 2, 5.5)
      ..lineTo(2, 4)
      ..cubicTo(2, 3.746, 2.047, 3.5, 2.14, 3.264)
      ..close()
      ..moveTo(10.854, 7.146)
      ..cubicTo(10.953, 7.246, 11.003, 7.364, 11.003, 7.5)
      ..cubicTo(11.003, 7.636, 10.953, 7.754, 10.854, 7.854)
      ..lineTo(7.854, 10.854)
      ..cubicTo(7.756, 10.951, 7.638, 11, 7.5, 11)
      ..cubicTo(7.362, 11, 7.244, 10.951, 7.146, 10.854)
      ..cubicTo(7.047, 10.754, 6.997, 10.636, 6.997, 10.5)
      ..cubicTo(6.997, 10.364, 7.047, 10.246, 7.146, 10.146)
      ..lineTo(9.293, 8)
      ..lineTo(1.5, 8)
      ..cubicTo(1.359, 8, 1.241, 7.952, 1.144, 7.856)
      ..cubicTo(1.048, 7.759, 1, 7.641, 1, 7.5)
      ..cubicTo(1, 7.359, 1.048, 7.241, 1.144, 7.144)
      ..cubicTo(1.241, 7.048, 1.359, 7, 1.5, 7)
      ..lineTo(9.293, 7)
      ..lineTo(7.146, 4.854)
      ..cubicTo(7.047, 4.754, 6.997, 4.636, 6.997, 4.5)
      ..cubicTo(6.997, 4.364, 7.047, 4.246, 7.146, 4.146)
      ..cubicTo(7.246, 4.047, 7.364, 3.997, 7.5, 3.997)
      ..cubicTo(7.636, 3.997, 7.754, 4.047, 7.854, 4.146)
      ..lineTo(10.854, 7.146)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_ImportIconPainter old) => old.color != color;
}
