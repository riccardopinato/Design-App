// Gentleface "repeat" (line-round), MIT. https://gentleface.com/icons/repeat
import 'package:flutter/widgets.dart';

class RepeatIcon extends StatelessWidget {
  const RepeatIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _RepeatIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _RepeatIconPainter extends CustomPainter {
  _RepeatIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(14.003, 3.5)
      ..cubicTo(14.003, 3.636, 13.953, 3.754, 13.854, 3.854)
      ..lineTo(11.854, 5.854)
      ..cubicTo(11.754, 5.953, 11.636, 6.003, 11.5, 6.003)
      ..cubicTo(11.364, 6.003, 11.246, 5.953, 11.146, 5.854)
      ..cubicTo(11.049, 5.756, 11, 5.638, 11, 5.5)
      ..cubicTo(11, 5.362, 11.049, 5.244, 11.146, 5.146)
      ..lineTo(12.293, 4)
      ..lineTo(4, 4)
      ..cubicTo(3.724, 4, 3.488, 4.098, 3.293, 4.293)
      ..cubicTo(3.098, 4.488, 3, 4.724, 3, 5)
      ..lineTo(3, 7.5)
      ..cubicTo(3, 7.641, 2.952, 7.759, 2.856, 7.856)
      ..cubicTo(2.759, 7.952, 2.641, 8, 2.5, 8)
      ..cubicTo(2.359, 8, 2.241, 7.952, 2.144, 7.856)
      ..cubicTo(2.048, 7.759, 2, 7.641, 2, 7.5)
      ..lineTo(2, 5)
      ..cubicTo(2, 4.746, 2.047, 4.5, 2.14, 4.264)
      ..cubicTo(2.242, 4.007, 2.391, 3.781, 2.586, 3.586)
      ..cubicTo(2.781, 3.391, 3.007, 3.242, 3.264, 3.14)
      ..cubicTo(3.5, 3.047, 3.746, 3, 4, 3)
      ..lineTo(12.293, 3)
      ..lineTo(11.146, 1.854)
      ..cubicTo(11.049, 1.756, 11, 1.638, 11, 1.5)
      ..cubicTo(11, 1.362, 11.049, 1.244, 11.146, 1.146)
      ..cubicTo(11.246, 1.047, 11.364, 0.997, 11.5, 0.997)
      ..cubicTo(11.636, 0.997, 11.754, 1.047, 11.854, 1.146)
      ..lineTo(13.854, 3.146)
      ..cubicTo(13.953, 3.246, 14.003, 3.364, 14.003, 3.5)
      ..close()
      ..moveTo(12.86, 10.736)
      ..cubicTo(12.758, 10.993, 12.609, 11.219, 12.414, 11.414)
      ..cubicTo(12.219, 11.609, 11.993, 11.758, 11.736, 11.86)
      ..cubicTo(11.5, 11.953, 11.254, 12, 11, 12)
      ..lineTo(2.707, 12)
      ..lineTo(3.854, 13.146)
      ..cubicTo(3.953, 13.246, 4.003, 13.364, 4.003, 13.5)
      ..cubicTo(4.003, 13.636, 3.953, 13.754, 3.854, 13.854)
      ..cubicTo(3.756, 13.951, 3.638, 14, 3.5, 14)
      ..cubicTo(3.362, 14, 3.244, 13.951, 3.146, 13.854)
      ..lineTo(1.146, 11.854)
      ..cubicTo(1.047, 11.754, 0.997, 11.636, 0.997, 11.5)
      ..cubicTo(0.997, 11.364, 1.047, 11.246, 1.146, 11.146)
      ..lineTo(3.146, 9.146)
      ..cubicTo(3.244, 9.049, 3.362, 9, 3.5, 9)
      ..cubicTo(3.638, 9, 3.756, 9.049, 3.854, 9.146)
      ..cubicTo(3.953, 9.246, 4.003, 9.364, 4.003, 9.5)
      ..cubicTo(4.003, 9.636, 3.953, 9.754, 3.854, 9.854)
      ..lineTo(2.707, 11)
      ..lineTo(11, 11)
      ..cubicTo(11.276, 11, 11.512, 10.902, 11.707, 10.707)
      ..cubicTo(11.902, 10.512, 12, 10.276, 12, 10)
      ..lineTo(12, 7.5)
      ..cubicTo(12, 7.359, 12.048, 7.241, 12.144, 7.144)
      ..cubicTo(12.241, 7.048, 12.359, 7, 12.5, 7)
      ..cubicTo(12.641, 7, 12.759, 7.048, 12.856, 7.144)
      ..cubicTo(12.952, 7.241, 13, 7.359, 13, 7.5)
      ..lineTo(13, 10)
      ..cubicTo(13, 10.254, 12.953, 10.5, 12.86, 10.736)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_RepeatIconPainter old) => old.color != color;
}
