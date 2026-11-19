// Gentleface "home" (line-round), MIT. https://gentleface.com/icons/home
import 'package:flutter/widgets.dart';

class HomeIcon extends StatelessWidget {
  const HomeIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _HomeIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _HomeIconPainter extends CustomPainter {
  _HomeIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(6.086, 2.207)
      ..cubicTo(6.266, 2.027, 6.472, 1.887, 6.706, 1.786)
      ..cubicTo(6.959, 1.676, 7.224, 1.621, 7.5, 1.621)
      ..cubicTo(7.776, 1.621, 8.041, 1.676, 8.294, 1.786)
      ..cubicTo(8.528, 1.887, 8.734, 2.027, 8.914, 2.207)
      ..lineTo(12.146, 5.439)
      ..cubicTo(12.42, 5.713, 12.63, 6.028, 12.778, 6.385)
      ..cubicTo(12.926, 6.742, 13, 7.114, 13, 7.5)
      ..lineTo(13, 12)
      ..cubicTo(13, 12.254, 12.953, 12.5, 12.86, 12.736)
      ..cubicTo(12.758, 12.993, 12.609, 13.219, 12.414, 13.414)
      ..cubicTo(12.219, 13.609, 11.993, 13.758, 11.736, 13.86)
      ..cubicTo(11.5, 13.953, 11.254, 14, 11, 14)
      ..lineTo(10, 14)
      ..cubicTo(9.724, 14, 9.488, 13.902, 9.293, 13.707)
      ..cubicTo(9.098, 13.512, 9, 13.276, 9, 13)
      ..lineTo(9, 10)
      ..lineTo(6, 10)
      ..lineTo(6, 13)
      ..cubicTo(6, 13.276, 5.902, 13.512, 5.707, 13.707)
      ..cubicTo(5.512, 13.902, 5.276, 14, 5, 14)
      ..lineTo(4, 14)
      ..cubicTo(3.746, 14, 3.5, 13.953, 3.264, 13.86)
      ..cubicTo(3.007, 13.758, 2.781, 13.609, 2.586, 13.414)
      ..cubicTo(2.391, 13.219, 2.242, 12.993, 2.14, 12.736)
      ..cubicTo(2.047, 12.5, 2, 12.254, 2, 12)
      ..lineTo(2, 7.5)
      ..cubicTo(2, 7.114, 2.074, 6.742, 2.222, 6.385)
      ..cubicTo(2.37, 6.028, 2.58, 5.713, 2.854, 5.439)
      ..lineTo(6.086, 2.207)
      ..close()
      ..moveTo(5, 10)
      ..cubicTo(5, 9.724, 5.098, 9.488, 5.293, 9.293)
      ..cubicTo(5.488, 9.098, 5.724, 9, 6, 9)
      ..lineTo(9, 9)
      ..cubicTo(9.276, 9, 9.512, 9.098, 9.707, 9.293)
      ..cubicTo(9.902, 9.488, 10, 9.724, 10, 10)
      ..lineTo(10, 13)
      ..lineTo(11, 13)
      ..cubicTo(11.276, 13, 11.512, 12.902, 11.707, 12.707)
      ..cubicTo(11.902, 12.512, 12, 12.276, 12, 12)
      ..lineTo(12, 7.5)
      ..cubicTo(12, 7.246, 11.951, 7.002, 11.854, 6.767)
      ..cubicTo(11.757, 6.533, 11.619, 6.326, 11.439, 6.146)
      ..lineTo(8.207, 2.914)
      ..cubicTo(8.012, 2.719, 7.776, 2.621, 7.5, 2.621)
      ..cubicTo(7.224, 2.621, 6.988, 2.719, 6.793, 2.914)
      ..lineTo(3.561, 6.146)
      ..cubicTo(3.381, 6.326, 3.243, 6.533, 3.146, 6.767)
      ..cubicTo(3.049, 7.002, 3, 7.246, 3, 7.5)
      ..lineTo(3, 12)
      ..cubicTo(3, 12.276, 3.098, 12.512, 3.293, 12.707)
      ..cubicTo(3.488, 12.902, 3.724, 13, 4, 13)
      ..lineTo(5, 13)
      ..lineTo(5, 10)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_HomeIconPainter old) => old.color != color;
}
