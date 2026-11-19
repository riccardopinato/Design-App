// Gentleface "play" (line-round), MIT. https://gentleface.com/icons/play
import 'package:flutter/widgets.dart';

class PlayIcon extends StatelessWidget {
  const PlayIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _PlayIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _PlayIconPainter extends CustomPainter {
  _PlayIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(3.757, 13.929)
      ..cubicTo(3.636, 14.001, 3.51, 14.021, 3.378, 13.988)
      ..cubicTo(3.246, 13.955, 3.144, 13.878, 3.071, 13.757)
      ..cubicTo(3.024, 13.678, 3, 13.592, 3, 13.5)
      ..lineTo(3, 1.5)
      ..cubicTo(3, 1.359, 3.048, 1.241, 3.144, 1.144)
      ..cubicTo(3.241, 1.048, 3.359, 1, 3.5, 1)
      ..cubicTo(3.592, 1, 3.678, 1.024, 3.757, 1.071)
      ..lineTo(13.757, 7.071)
      ..cubicTo(13.876, 7.142, 13.952, 7.245, 13.985, 7.379)
      ..cubicTo(14.019, 7.513, 14, 7.639, 13.929, 7.757)
      ..cubicTo(13.886, 7.829, 13.829, 7.886, 13.757, 7.929)
      ..lineTo(3.757, 13.929)
      ..close()
      ..moveTo(12.528, 7.5)
      ..lineTo(4, 2.383)
      ..lineTo(4, 12.617)
      ..lineTo(12.528, 7.5)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_PlayIconPainter old) => old.color != color;
}
