// Gentleface "eye" (line-round), MIT. https://gentleface.com/icons/eye
import 'package:flutter/widgets.dart';

class EyeIcon extends StatelessWidget {
  const EyeIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _EyeIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _EyeIconPainter extends CustomPainter {
  _EyeIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(8, 3)
      ..cubicTo(9.51, 3, 10.882, 3.472, 12.116, 4.415)
      ..cubicTo(13.122, 5.184, 14.059, 6.293, 14.929, 7.743)
      ..cubicTo(14.977, 7.823, 15.001, 7.908, 15.001, 8)
      ..cubicTo(15.001, 8.092, 14.977, 8.177, 14.929, 8.257)
      ..cubicTo(14.059, 9.707, 13.122, 10.816, 12.116, 11.585)
      ..cubicTo(10.882, 12.528, 9.51, 13, 8, 13)
      ..cubicTo(6.49, 13, 5.118, 12.528, 3.884, 11.585)
      ..cubicTo(2.878, 10.816, 1.941, 9.707, 1.071, 8.257)
      ..cubicTo(1.023, 8.177, 0.999, 8.092, 0.999, 8)
      ..cubicTo(0.999, 7.908, 1.023, 7.823, 1.071, 7.743)
      ..cubicTo(1.941, 6.293, 2.878, 5.184, 3.884, 4.415)
      ..cubicTo(5.118, 3.472, 6.49, 3, 8, 3)
      ..close()
      ..moveTo(8, 12)
      ..cubicTo(9.285, 12, 10.454, 11.597, 11.509, 10.79)
      ..cubicTo(12.354, 10.144, 13.156, 9.214, 13.914, 8)
      ..cubicTo(13.156, 6.786, 12.354, 5.856, 11.509, 5.21)
      ..cubicTo(10.454, 4.403, 9.285, 4, 8, 4)
      ..cubicTo(6.715, 4, 5.546, 4.403, 4.491, 5.21)
      ..cubicTo(3.646, 5.856, 2.844, 6.786, 2.086, 8)
      ..cubicTo(2.844, 9.214, 3.646, 10.144, 4.491, 10.79)
      ..cubicTo(5.546, 11.597, 6.715, 12, 8, 12)
      ..close()
      ..moveTo(5.211, 6.896)
      ..cubicTo(5.363, 6.511, 5.586, 6.172, 5.879, 5.879)
      ..cubicTo(6.172, 5.586, 6.511, 5.363, 6.896, 5.211)
      ..cubicTo(7.25, 5.07, 7.619, 5, 8, 5)
      ..cubicTo(8.381, 5, 8.75, 5.07, 9.104, 5.211)
      ..cubicTo(9.489, 5.363, 9.828, 5.586, 10.121, 5.879)
      ..cubicTo(10.414, 6.172, 10.637, 6.511, 10.789, 6.896)
      ..cubicTo(10.93, 7.25, 11, 7.619, 11, 8)
      ..cubicTo(11, 8.381, 10.93, 8.75, 10.789, 9.104)
      ..cubicTo(10.637, 9.489, 10.414, 9.828, 10.121, 10.121)
      ..cubicTo(9.828, 10.414, 9.489, 10.637, 9.104, 10.789)
      ..cubicTo(8.75, 10.93, 8.381, 11, 8, 11)
      ..cubicTo(7.619, 11, 7.25, 10.93, 6.896, 10.789)
      ..cubicTo(6.511, 10.637, 6.172, 10.414, 5.879, 10.121)
      ..cubicTo(5.586, 9.828, 5.363, 9.489, 5.211, 9.104)
      ..cubicTo(5.07, 8.75, 5, 8.381, 5, 8)
      ..cubicTo(5, 7.619, 5.07, 7.25, 5.211, 6.896)
      ..close()
      ..moveTo(6.14, 8.736)
      ..cubicTo(6.242, 8.993, 6.391, 9.219, 6.586, 9.414)
      ..cubicTo(6.781, 9.609, 7.007, 9.758, 7.264, 9.86)
      ..cubicTo(7.5, 9.953, 7.746, 10, 8, 10)
      ..cubicTo(8.254, 10, 8.5, 9.953, 8.736, 9.86)
      ..cubicTo(8.993, 9.758, 9.219, 9.609, 9.414, 9.414)
      ..cubicTo(9.609, 9.219, 9.758, 8.993, 9.86, 8.736)
      ..cubicTo(9.953, 8.5, 10, 8.254, 10, 8)
      ..cubicTo(10, 7.746, 9.953, 7.5, 9.86, 7.264)
      ..cubicTo(9.758, 7.007, 9.609, 6.781, 9.414, 6.586)
      ..cubicTo(9.219, 6.391, 8.993, 6.242, 8.736, 6.14)
      ..cubicTo(8.5, 6.047, 8.254, 6, 8, 6)
      ..cubicTo(7.746, 6, 7.5, 6.047, 7.264, 6.14)
      ..cubicTo(7.007, 6.242, 6.781, 6.391, 6.586, 6.586)
      ..cubicTo(6.391, 6.781, 6.242, 7.007, 6.14, 7.264)
      ..cubicTo(6.047, 7.5, 6, 7.746, 6, 8)
      ..cubicTo(6, 8.254, 6.047, 8.5, 6.14, 8.736)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_EyeIconPainter old) => old.color != color;
}
