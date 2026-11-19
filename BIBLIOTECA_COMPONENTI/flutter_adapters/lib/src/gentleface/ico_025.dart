// Gentleface "messages" (line-round), MIT. https://gentleface.com/icons/messages
import 'package:flutter/widgets.dart';

class MessagesIcon extends StatelessWidget {
  const MessagesIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _MessagesIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _MessagesIconPainter extends CustomPainter {
  _MessagesIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(9.86, 7.736)
      ..cubicTo(9.758, 7.993, 9.609, 8.219, 9.414, 8.414)
      ..cubicTo(9.219, 8.609, 8.993, 8.758, 8.736, 8.86)
      ..cubicTo(8.5, 8.953, 8.254, 9, 8, 9)
      ..lineTo(5.5, 9)
      ..cubicTo(5.246, 9, 5.002, 9.049, 4.767, 9.146)
      ..cubicTo(4.533, 9.243, 4.326, 9.381, 4.146, 9.561)
      ..lineTo(1.854, 11.854)
      ..cubicTo(1.754, 11.953, 1.636, 12.003, 1.5, 12.003)
      ..cubicTo(1.364, 12.003, 1.246, 11.953, 1.146, 11.854)
      ..cubicTo(1.049, 11.756, 1, 11.638, 1, 11.5)
      ..lineTo(1, 3)
      ..cubicTo(1, 2.746, 1.047, 2.5, 1.14, 2.264)
      ..cubicTo(1.242, 2.007, 1.391, 1.781, 1.586, 1.586)
      ..cubicTo(1.781, 1.391, 2.007, 1.242, 2.264, 1.14)
      ..cubicTo(2.5, 1.047, 2.746, 1, 3, 1)
      ..lineTo(8, 1)
      ..cubicTo(8.254, 1, 8.5, 1.047, 8.736, 1.14)
      ..cubicTo(8.993, 1.242, 9.219, 1.391, 9.414, 1.586)
      ..cubicTo(9.609, 1.781, 9.758, 2.007, 9.86, 2.264)
      ..cubicTo(9.953, 2.5, 10, 2.746, 10, 3)
      ..lineTo(10, 7)
      ..cubicTo(10, 7.254, 9.953, 7.5, 9.86, 7.736)
      ..close()
      ..moveTo(3.439, 8.854)
      ..cubicTo(3.713, 8.58, 4.028, 8.37, 4.385, 8.222)
      ..cubicTo(4.742, 8.074, 5.114, 8, 5.5, 8)
      ..lineTo(8, 8)
      ..cubicTo(8.276, 8, 8.512, 7.902, 8.707, 7.707)
      ..cubicTo(8.902, 7.512, 9, 7.276, 9, 7)
      ..lineTo(9, 3)
      ..cubicTo(9, 2.724, 8.902, 2.488, 8.707, 2.293)
      ..cubicTo(8.512, 2.098, 8.276, 2, 8, 2)
      ..lineTo(3, 2)
      ..cubicTo(2.724, 2, 2.488, 2.098, 2.293, 2.293)
      ..cubicTo(2.098, 2.488, 2, 2.724, 2, 3)
      ..lineTo(2, 10.293)
      ..lineTo(3.439, 8.854)
      ..close()
      ..moveTo(7.073, 10.927)
      ..cubicTo(7.122, 10.976, 7.181, 11, 7.25, 11)
      ..lineTo(10.879, 11)
      ..cubicTo(11.144, 11, 11.399, 11.051, 11.644, 11.152)
      ..cubicTo(11.889, 11.254, 12.105, 11.398, 12.293, 11.586)
      ..lineTo(14, 13.293)
      ..lineTo(14, 6)
      ..cubicTo(14, 5.724, 13.902, 5.488, 13.707, 5.293)
      ..cubicTo(13.512, 5.098, 13.276, 5, 13, 5)
      ..lineTo(11.5, 5)
      ..cubicTo(11.359, 5, 11.241, 4.952, 11.144, 4.856)
      ..cubicTo(11.048, 4.759, 11, 4.641, 11, 4.5)
      ..cubicTo(11, 4.359, 11.048, 4.241, 11.144, 4.144)
      ..cubicTo(11.241, 4.048, 11.359, 4, 11.5, 4)
      ..lineTo(13, 4)
      ..cubicTo(13.254, 4, 13.5, 4.047, 13.736, 4.14)
      ..cubicTo(13.993, 4.242, 14.219, 4.391, 14.414, 4.586)
      ..cubicTo(14.609, 4.781, 14.758, 5.007, 14.86, 5.264)
      ..cubicTo(14.953, 5.5, 15, 5.746, 15, 6)
      ..lineTo(15, 14.5)
      ..cubicTo(15, 14.638, 14.951, 14.756, 14.854, 14.854)
      ..cubicTo(14.754, 14.953, 14.636, 15.003, 14.5, 15.003)
      ..cubicTo(14.364, 15.003, 14.246, 14.953, 14.146, 14.854)
      ..lineTo(11.586, 12.293)
      ..cubicTo(11.391, 12.098, 11.155, 12, 10.879, 12)
      ..lineTo(7.25, 12)
      ..cubicTo(7.091, 12, 6.938, 11.971, 6.79, 11.912)
      ..cubicTo(6.629, 11.849, 6.488, 11.756, 6.366, 11.634)
      ..cubicTo(6.244, 11.512, 6.151, 11.371, 6.088, 11.21)
      ..cubicTo(6.029, 11.062, 6, 10.909, 6, 10.75)
      ..lineTo(6, 10.5)
      ..cubicTo(6, 10.359, 6.048, 10.241, 6.144, 10.144)
      ..cubicTo(6.241, 10.048, 6.359, 10, 6.5, 10)
      ..cubicTo(6.641, 10, 6.759, 10.048, 6.856, 10.144)
      ..cubicTo(6.952, 10.241, 7, 10.359, 7, 10.5)
      ..lineTo(7, 10.75)
      ..cubicTo(7, 10.819, 7.024, 10.878, 7.073, 10.927)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_MessagesIconPainter old) => old.color != color;
}
