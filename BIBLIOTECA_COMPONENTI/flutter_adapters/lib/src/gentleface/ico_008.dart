// Gentleface "images" (line-round), MIT. https://gentleface.com/icons/images
import 'package:flutter/widgets.dart';

class ImagesIcon extends StatelessWidget {
  const ImagesIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _ImagesIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _ImagesIconPainter extends CustomPainter {
  _ImagesIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(13.736, 2.14)
      ..cubicTo(13.993, 2.242, 14.219, 2.391, 14.414, 2.586)
      ..cubicTo(14.609, 2.781, 14.758, 3.007, 14.86, 3.264)
      ..cubicTo(14.953, 3.5, 15, 3.746, 15, 4)
      ..lineTo(15, 11.5)
      ..cubicTo(15, 11.641, 14.952, 11.759, 14.856, 11.856)
      ..cubicTo(14.759, 11.952, 14.641, 12, 14.5, 12)
      ..cubicTo(14.359, 12, 14.241, 11.952, 14.144, 11.856)
      ..cubicTo(14.048, 11.759, 14, 11.641, 14, 11.5)
      ..lineTo(14, 4)
      ..cubicTo(14, 3.724, 13.902, 3.488, 13.707, 3.293)
      ..cubicTo(13.512, 3.098, 13.276, 3, 13, 3)
      ..lineTo(3.5, 3)
      ..cubicTo(3.359, 3, 3.241, 2.952, 3.144, 2.856)
      ..cubicTo(3.048, 2.759, 3, 2.641, 3, 2.5)
      ..cubicTo(3, 2.359, 3.048, 2.241, 3.144, 2.144)
      ..cubicTo(3.241, 2.048, 3.359, 2, 3.5, 2)
      ..lineTo(13, 2)
      ..cubicTo(13.254, 2, 13.5, 2.047, 13.736, 2.14)
      ..close()
      ..moveTo(12.86, 12.736)
      ..cubicTo(12.758, 12.993, 12.609, 13.219, 12.414, 13.414)
      ..cubicTo(12.219, 13.609, 11.993, 13.758, 11.736, 13.86)
      ..cubicTo(11.5, 13.953, 11.254, 14, 11, 14)
      ..lineTo(3, 14)
      ..cubicTo(2.746, 14, 2.5, 13.953, 2.264, 13.86)
      ..cubicTo(2.007, 13.758, 1.781, 13.609, 1.586, 13.414)
      ..cubicTo(1.391, 13.219, 1.242, 12.993, 1.14, 12.736)
      ..cubicTo(1.047, 12.5, 1, 12.254, 1, 12)
      ..lineTo(1, 6)
      ..cubicTo(1, 5.746, 1.047, 5.5, 1.14, 5.264)
      ..cubicTo(1.242, 5.007, 1.391, 4.781, 1.586, 4.586)
      ..cubicTo(1.781, 4.391, 2.007, 4.242, 2.264, 4.14)
      ..cubicTo(2.5, 4.047, 2.746, 4, 3, 4)
      ..lineTo(11, 4)
      ..cubicTo(11.254, 4, 11.5, 4.047, 11.736, 4.14)
      ..cubicTo(11.993, 4.242, 12.219, 4.391, 12.414, 4.586)
      ..cubicTo(12.609, 4.781, 12.758, 5.007, 12.86, 5.264)
      ..cubicTo(12.953, 5.5, 13, 5.746, 13, 6)
      ..lineTo(13, 12)
      ..cubicTo(13, 12.254, 12.953, 12.5, 12.86, 12.736)
      ..close()
      ..moveTo(4.086, 8.207)
      ..cubicTo(4.266, 8.027, 4.472, 7.887, 4.706, 7.786)
      ..cubicTo(4.959, 7.676, 5.224, 7.621, 5.5, 7.621)
      ..cubicTo(5.776, 7.621, 6.041, 7.676, 6.294, 7.786)
      ..cubicTo(6.528, 7.887, 6.734, 8.027, 6.914, 8.207)
      ..lineTo(11.547, 12.84)
      ..cubicTo(11.603, 12.802, 11.656, 12.758, 11.707, 12.707)
      ..cubicTo(11.902, 12.512, 12, 12.276, 12, 12)
      ..lineTo(12, 6)
      ..cubicTo(12, 5.724, 11.902, 5.488, 11.707, 5.293)
      ..cubicTo(11.512, 5.098, 11.276, 5, 11, 5)
      ..lineTo(3, 5)
      ..cubicTo(2.724, 5, 2.488, 5.098, 2.293, 5.293)
      ..cubicTo(2.098, 5.488, 2, 5.724, 2, 6)
      ..lineTo(2, 10.293)
      ..lineTo(4.086, 8.207)
      ..close()
      ..moveTo(9.293, 6.293)
      ..cubicTo(9.488, 6.098, 9.724, 6, 10, 6)
      ..cubicTo(10.276, 6, 10.512, 6.098, 10.707, 6.293)
      ..cubicTo(10.902, 6.488, 11, 6.724, 11, 7)
      ..cubicTo(11, 7.276, 10.902, 7.512, 10.707, 7.707)
      ..cubicTo(10.512, 7.902, 10.276, 8, 10, 8)
      ..cubicTo(9.724, 8, 9.488, 7.902, 9.293, 7.707)
      ..cubicTo(9.098, 7.512, 9, 7.276, 9, 7)
      ..cubicTo(9, 6.724, 9.098, 6.488, 9.293, 6.293)
      ..close()
      ..moveTo(2, 11.707)
      ..lineTo(2, 12)
      ..cubicTo(2, 12.276, 2.098, 12.512, 2.293, 12.707)
      ..cubicTo(2.488, 12.902, 2.724, 13, 3, 13)
      ..lineTo(10.293, 13)
      ..lineTo(6.207, 8.914)
      ..cubicTo(6.012, 8.719, 5.776, 8.621, 5.5, 8.621)
      ..cubicTo(5.224, 8.621, 4.988, 8.719, 4.793, 8.914)
      ..lineTo(2, 11.707)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_ImagesIconPainter old) => old.color != color;
}
