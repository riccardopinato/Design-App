// Gentleface "video" (line-round), MIT. https://gentleface.com/icons/video
import 'package:flutter/widgets.dart';

class VideoIcon extends StatelessWidget {
  const VideoIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _VideoIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _VideoIconPainter extends CustomPainter {
  _VideoIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(13.553, 4.415)
      ..cubicTo(13.697, 4.343, 13.849, 4.307, 14.01, 4.309)
      ..cubicTo(14.196, 4.311, 14.368, 4.361, 14.526, 4.458)
      ..cubicTo(14.684, 4.556, 14.805, 4.688, 14.89, 4.853)
      ..cubicTo(14.963, 4.996, 15, 5.148, 15, 5.309)
      ..lineTo(15, 10.691)
      ..cubicTo(15, 10.852, 14.963, 11.004, 14.89, 11.147)
      ..cubicTo(14.805, 11.312, 14.684, 11.444, 14.526, 11.542)
      ..cubicTo(14.368, 11.639, 14.196, 11.689, 14.01, 11.691)
      ..cubicTo(13.849, 11.693, 13.697, 11.657, 13.553, 11.585)
      ..lineTo(11, 10.309)
      ..lineTo(11, 11)
      ..cubicTo(11, 11.254, 10.953, 11.5, 10.86, 11.736)
      ..cubicTo(10.758, 11.993, 10.609, 12.219, 10.414, 12.414)
      ..cubicTo(10.219, 12.609, 9.993, 12.758, 9.736, 12.86)
      ..cubicTo(9.5, 12.953, 9.254, 13, 9, 13)
      ..lineTo(3, 13)
      ..cubicTo(2.746, 13, 2.5, 12.953, 2.264, 12.86)
      ..cubicTo(2.007, 12.758, 1.781, 12.609, 1.586, 12.414)
      ..cubicTo(1.391, 12.219, 1.242, 11.993, 1.14, 11.736)
      ..cubicTo(1.047, 11.5, 1, 11.254, 1, 11)
      ..lineTo(1, 5)
      ..cubicTo(1, 4.746, 1.047, 4.5, 1.14, 4.264)
      ..cubicTo(1.242, 4.007, 1.391, 3.781, 1.586, 3.586)
      ..cubicTo(1.781, 3.391, 2.007, 3.242, 2.264, 3.14)
      ..cubicTo(2.5, 3.047, 2.746, 3, 3, 3)
      ..lineTo(9, 3)
      ..cubicTo(9.254, 3, 9.5, 3.047, 9.736, 3.14)
      ..cubicTo(9.993, 3.242, 10.219, 3.391, 10.414, 3.586)
      ..cubicTo(10.609, 3.781, 10.758, 4.007, 10.86, 4.264)
      ..cubicTo(10.953, 4.5, 11, 4.746, 11, 5)
      ..lineTo(11, 5.691)
      ..lineTo(13.553, 4.415)
      ..close()
      ..moveTo(2.293, 11.707)
      ..cubicTo(2.488, 11.902, 2.724, 12, 3, 12)
      ..lineTo(9, 12)
      ..cubicTo(9.276, 12, 9.512, 11.902, 9.707, 11.707)
      ..cubicTo(9.902, 11.512, 10, 11.276, 10, 11)
      ..lineTo(10, 5)
      ..cubicTo(10, 4.724, 9.902, 4.488, 9.707, 4.293)
      ..cubicTo(9.512, 4.098, 9.276, 4, 9, 4)
      ..lineTo(3, 4)
      ..cubicTo(2.724, 4, 2.488, 4.098, 2.293, 4.293)
      ..cubicTo(2.098, 4.488, 2, 4.724, 2, 5)
      ..lineTo(2, 11)
      ..cubicTo(2, 11.276, 2.098, 11.512, 2.293, 11.707)
      ..close()
      ..moveTo(14, 10.691)
      ..lineTo(14, 5.309)
      ..lineTo(11, 6.809)
      ..lineTo(11, 9.191)
      ..lineTo(14, 10.691)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_VideoIconPainter old) => old.color != color;
}
