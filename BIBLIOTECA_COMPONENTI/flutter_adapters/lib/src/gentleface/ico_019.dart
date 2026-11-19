// Gentleface "star" (line-round), MIT. https://gentleface.com/icons/star
import 'package:flutter/widgets.dart';

class StarIcon extends StatelessWidget {
  const StarIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _StarIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _StarIconPainter extends CustomPainter {
  _StarIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(13.856, 6.144)
      ..cubicTo(13.952, 6.241, 14, 6.359, 14, 6.5)
      ..cubicTo(14, 6.653, 13.942, 6.78, 13.825, 6.88)
      ..lineTo(10.56, 9.679)
      ..lineTo(11.485, 13.379)
      ..cubicTo(11.519, 13.513, 11.5, 13.639, 11.429, 13.757)
      ..cubicTo(11.358, 13.876, 11.255, 13.952, 11.121, 13.985)
      ..cubicTo(10.972, 14.022, 10.835, 13.996, 10.709, 13.907)
      ..lineTo(7.5, 11.614)
      ..lineTo(4.291, 13.907)
      ..cubicTo(4.178, 13.987, 4.054, 14.016, 3.918, 13.993)
      ..cubicTo(3.782, 13.97, 3.673, 13.903, 3.593, 13.791)
      ..cubicTo(3.504, 13.665, 3.478, 13.528, 3.515, 13.379)
      ..lineTo(4.44, 9.679)
      ..lineTo(1.175, 6.88)
      ..cubicTo(1.07, 6.79, 1.012, 6.676, 1.001, 6.538)
      ..cubicTo(0.991, 6.401, 1.031, 6.279, 1.12, 6.175)
      ..cubicTo(1.22, 6.058, 1.347, 6, 1.5, 6)
      ..lineTo(5.653, 6)
      ..lineTo(7.032, 2.324)
      ..cubicTo(7.08, 2.195, 7.167, 2.102, 7.293, 2.045)
      ..cubicTo(7.419, 1.988, 7.546, 1.983, 7.676, 2.032)
      ..cubicTo(7.817, 2.085, 7.915, 2.183, 7.968, 2.324)
      ..lineTo(9.347, 6)
      ..lineTo(13.5, 6)
      ..cubicTo(13.641, 6, 13.759, 6.048, 13.856, 6.144)
      ..close()
      ..moveTo(6.59, 6.351)
      ..cubicTo(6.517, 6.546, 6.394, 6.703, 6.223, 6.822)
      ..cubicTo(6.052, 6.941, 5.862, 7, 5.653, 7)
      ..lineTo(2.852, 7)
      ..lineTo(5.091, 8.919)
      ..cubicTo(5.235, 9.043, 5.335, 9.194, 5.393, 9.375)
      ..cubicTo(5.45, 9.555, 5.456, 9.737, 5.41, 9.921)
      ..lineTo(4.814, 12.304)
      ..lineTo(6.919, 10.801)
      ..cubicTo(7.093, 10.677, 7.286, 10.614, 7.5, 10.614)
      ..cubicTo(7.714, 10.614, 7.907, 10.677, 8.081, 10.801)
      ..lineTo(10.186, 12.304)
      ..lineTo(9.59, 9.921)
      ..cubicTo(9.544, 9.737, 9.55, 9.555, 9.607, 9.375)
      ..cubicTo(9.665, 9.194, 9.765, 9.043, 9.909, 8.919)
      ..lineTo(12.148, 7)
      ..lineTo(9.347, 7)
      ..cubicTo(9.138, 7, 8.948, 6.941, 8.777, 6.822)
      ..cubicTo(8.606, 6.703, 8.483, 6.546, 8.41, 6.351)
      ..lineTo(7.5, 3.924)
      ..lineTo(6.59, 6.351)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_StarIconPainter old) => old.color != color;
}
