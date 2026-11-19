// Gentleface "bell-ring" (line-round), MIT. https://gentleface.com/icons/bell-ring
import 'package:flutter/widgets.dart';

class BellRingIcon extends StatelessWidget {
  const BellRingIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _BellRingIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _BellRingIconPainter extends CustomPainter {
  _BellRingIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(2.638, 1.501)
      ..cubicTo(2.728, 1.393, 2.841, 1.333, 2.977, 1.321)
      ..cubicTo(3.112, 1.309, 3.234, 1.348, 3.342, 1.439)
      ..cubicTo(3.448, 1.528, 3.507, 1.641, 3.519, 1.778)
      ..cubicTo(3.531, 1.916, 3.492, 2.038, 3.404, 2.143)
      ..cubicTo(3.002, 2.623, 2.682, 3.152, 2.445, 3.731)
      ..cubicTo(2.209, 4.311, 2.066, 4.912, 2.018, 5.536)
      ..cubicTo(2.007, 5.674, 1.95, 5.787, 1.845, 5.877)
      ..cubicTo(1.74, 5.967, 1.618, 6.007, 1.481, 5.996)
      ..cubicTo(1.34, 5.985, 1.226, 5.928, 1.137, 5.824)
      ..cubicTo(1.049, 5.721, 1.01, 5.599, 1.021, 5.459)
      ..cubicTo(1.077, 4.731, 1.244, 4.029, 1.52, 3.353)
      ..cubicTo(1.796, 2.677, 2.168, 2.06, 2.638, 1.501)
      ..close()
      ..moveTo(13.982, 5.536)
      ..cubicTo(13.934, 4.912, 13.791, 4.311, 13.555, 3.731)
      ..cubicTo(13.318, 3.152, 12.998, 2.623, 12.596, 2.143)
      ..cubicTo(12.508, 2.038, 12.469, 1.916, 12.481, 1.778)
      ..cubicTo(12.493, 1.641, 12.552, 1.528, 12.658, 1.439)
      ..cubicTo(12.764, 1.35, 12.885, 1.312, 13.023, 1.324)
      ..cubicTo(13.16, 1.336, 13.274, 1.395, 13.362, 1.501)
      ..cubicTo(13.832, 2.06, 14.204, 2.677, 14.48, 3.353)
      ..cubicTo(14.756, 4.029, 14.923, 4.731, 14.979, 5.459)
      ..cubicTo(14.99, 5.596, 14.95, 5.718, 14.86, 5.822)
      ..cubicTo(14.771, 5.927, 14.657, 5.985, 14.519, 5.996)
      ..cubicTo(14.379, 6.007, 14.257, 5.968, 14.153, 5.879)
      ..cubicTo(14.05, 5.791, 13.993, 5.677, 13.982, 5.536)
      ..close()
      ..moveTo(4, 8.5)
      ..lineTo(4, 6)
      ..cubicTo(4, 5.491, 4.094, 5.001, 4.281, 4.528)
      ..cubicTo(4.484, 4.014, 4.781, 3.562, 5.172, 3.172)
      ..cubicTo(5.562, 2.781, 6.014, 2.484, 6.528, 2.281)
      ..cubicTo(7.001, 2.094, 7.491, 2, 8, 2)
      ..cubicTo(8.509, 2, 8.999, 2.094, 9.472, 2.281)
      ..cubicTo(9.986, 2.484, 10.438, 2.781, 10.828, 3.172)
      ..cubicTo(11.219, 3.562, 11.516, 4.014, 11.719, 4.528)
      ..cubicTo(11.906, 5.001, 12, 5.491, 12, 6)
      ..lineTo(12, 8.5)
      ..cubicTo(12, 9.088, 12.131, 9.645, 12.394, 10.171)
      ..lineTo(12.809, 11)
      ..lineTo(13.5, 11)
      ..cubicTo(13.641, 11, 13.759, 11.048, 13.856, 11.144)
      ..cubicTo(13.952, 11.241, 14, 11.359, 14, 11.5)
      ..cubicTo(14, 11.641, 13.952, 11.759, 13.856, 11.856)
      ..cubicTo(13.759, 11.952, 13.641, 12, 13.5, 12)
      ..lineTo(10, 12)
      ..cubicTo(10, 12.254, 9.953, 12.5, 9.86, 12.736)
      ..cubicTo(9.758, 12.993, 9.609, 13.219, 9.414, 13.414)
      ..cubicTo(9.219, 13.609, 8.993, 13.758, 8.736, 13.86)
      ..cubicTo(8.5, 13.953, 8.254, 14, 8, 14)
      ..cubicTo(7.746, 14, 7.5, 13.953, 7.264, 13.86)
      ..cubicTo(7.007, 13.758, 6.781, 13.609, 6.586, 13.414)
      ..cubicTo(6.391, 13.219, 6.242, 12.993, 6.14, 12.736)
      ..cubicTo(6.047, 12.5, 6, 12.254, 6, 12)
      ..lineTo(2.5, 12)
      ..cubicTo(2.359, 12, 2.241, 11.952, 2.144, 11.856)
      ..cubicTo(2.048, 11.759, 2, 11.641, 2, 11.5)
      ..cubicTo(2, 11.359, 2.048, 11.241, 2.144, 11.144)
      ..cubicTo(2.241, 11.048, 2.359, 11, 2.5, 11)
      ..lineTo(3.191, 11)
      ..lineTo(3.606, 10.171)
      ..cubicTo(3.869, 9.645, 4, 9.088, 4, 8.5)
      ..close()
      ..moveTo(11, 8.5)
      ..lineTo(11, 6)
      ..cubicTo(11, 5.619, 10.93, 5.25, 10.789, 4.896)
      ..cubicTo(10.637, 4.511, 10.414, 4.172, 10.121, 3.879)
      ..cubicTo(9.828, 3.586, 9.489, 3.363, 9.104, 3.211)
      ..cubicTo(8.75, 3.07, 8.381, 3, 8, 3)
      ..cubicTo(7.619, 3, 7.25, 3.07, 6.896, 3.211)
      ..cubicTo(6.511, 3.363, 6.172, 3.586, 5.879, 3.879)
      ..cubicTo(5.586, 4.172, 5.363, 4.511, 5.211, 4.896)
      ..cubicTo(5.07, 5.25, 5, 5.619, 5, 6)
      ..lineTo(5, 8.5)
      ..cubicTo(5, 9.245, 4.833, 9.951, 4.5, 10.618)
      ..lineTo(4.309, 11)
      ..lineTo(11.691, 11)
      ..lineTo(11.5, 10.618)
      ..cubicTo(11.167, 9.951, 11, 9.245, 11, 8.5)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_BellRingIconPainter old) => old.color != color;
}
