// Gentleface "export" (line-round), MIT. https://gentleface.com/icons/export
import 'package:flutter/widgets.dart';

class ExportIcon extends StatelessWidget {
  const ExportIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _ExportIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _ExportIconPainter extends CustomPainter {
  _ExportIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(12.927, 3.073)
      ..cubicTo(12.878, 3.024, 12.819, 3, 12.75, 3)
      ..lineTo(4, 3)
      ..cubicTo(3.724, 3, 3.488, 3.098, 3.293, 3.293)
      ..cubicTo(3.098, 3.488, 3, 3.724, 3, 4)
      ..lineTo(3, 12)
      ..cubicTo(3, 12.276, 3.098, 12.512, 3.293, 12.707)
      ..cubicTo(3.488, 12.902, 3.724, 13, 4, 13)
      ..lineTo(12.25, 13)
      ..cubicTo(12.457, 13, 12.634, 12.927, 12.78, 12.78)
      ..cubicTo(12.927, 12.634, 13, 12.457, 13, 12.25)
      ..lineTo(13, 11.5)
      ..cubicTo(13, 11.359, 13.048, 11.241, 13.144, 11.144)
      ..cubicTo(13.241, 11.048, 13.359, 11, 13.5, 11)
      ..cubicTo(13.641, 11, 13.759, 11.048, 13.856, 11.144)
      ..cubicTo(13.952, 11.241, 14, 11.359, 14, 11.5)
      ..lineTo(14, 12.25)
      ..cubicTo(14, 12.473, 13.959, 12.687, 13.877, 12.894)
      ..cubicTo(13.788, 13.119, 13.658, 13.317, 13.487, 13.487)
      ..cubicTo(13.317, 13.658, 13.119, 13.788, 12.894, 13.877)
      ..cubicTo(12.687, 13.959, 12.473, 14, 12.25, 14)
      ..lineTo(4, 14)
      ..cubicTo(3.746, 14, 3.5, 13.953, 3.264, 13.86)
      ..cubicTo(3.007, 13.758, 2.781, 13.609, 2.586, 13.414)
      ..cubicTo(2.391, 13.219, 2.242, 12.993, 2.14, 12.736)
      ..cubicTo(2.047, 12.5, 2, 12.254, 2, 12)
      ..lineTo(2, 4)
      ..cubicTo(2, 3.746, 2.047, 3.5, 2.14, 3.264)
      ..cubicTo(2.242, 3.007, 2.391, 2.781, 2.586, 2.586)
      ..cubicTo(2.781, 2.391, 3.007, 2.242, 3.264, 2.14)
      ..cubicTo(3.5, 2.047, 3.746, 2, 4, 2)
      ..lineTo(12.75, 2)
      ..cubicTo(12.909, 2, 13.062, 2.029, 13.21, 2.088)
      ..cubicTo(13.371, 2.151, 13.512, 2.244, 13.634, 2.366)
      ..cubicTo(13.756, 2.488, 13.849, 2.629, 13.912, 2.79)
      ..cubicTo(13.971, 2.938, 14, 3.091, 14, 3.25)
      ..lineTo(14, 3.5)
      ..cubicTo(14, 3.641, 13.952, 3.759, 13.856, 3.856)
      ..cubicTo(13.759, 3.952, 13.641, 4, 13.5, 4)
      ..cubicTo(13.359, 4, 13.241, 3.952, 13.144, 3.856)
      ..cubicTo(13.048, 3.759, 13, 3.641, 13, 3.5)
      ..lineTo(13, 3.25)
      ..cubicTo(13, 3.181, 12.976, 3.122, 12.927, 3.073)
      ..close()
      ..moveTo(15.003, 7.5)
      ..cubicTo(15.003, 7.636, 14.953, 7.754, 14.854, 7.854)
      ..lineTo(11.854, 10.854)
      ..cubicTo(11.754, 10.953, 11.636, 11.003, 11.5, 11.003)
      ..cubicTo(11.364, 11.003, 11.246, 10.953, 11.146, 10.854)
      ..cubicTo(11.047, 10.754, 10.997, 10.636, 10.997, 10.5)
      ..cubicTo(10.997, 10.364, 11.047, 10.246, 11.146, 10.146)
      ..lineTo(13.293, 8)
      ..lineTo(5.5, 8)
      ..cubicTo(5.359, 8, 5.241, 7.952, 5.144, 7.856)
      ..cubicTo(5.048, 7.759, 5, 7.641, 5, 7.5)
      ..cubicTo(5, 7.359, 5.048, 7.241, 5.144, 7.144)
      ..cubicTo(5.241, 7.048, 5.359, 7, 5.5, 7)
      ..lineTo(13.293, 7)
      ..lineTo(11.146, 4.854)
      ..cubicTo(11.049, 4.756, 11, 4.638, 11, 4.5)
      ..cubicTo(11, 4.362, 11.049, 4.244, 11.146, 4.146)
      ..cubicTo(11.246, 4.047, 11.364, 3.997, 11.5, 3.997)
      ..cubicTo(11.636, 3.997, 11.754, 4.047, 11.854, 4.146)
      ..lineTo(14.854, 7.146)
      ..cubicTo(14.953, 7.246, 15.003, 7.364, 15.003, 7.5)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_ExportIconPainter old) => old.color != color;
}
