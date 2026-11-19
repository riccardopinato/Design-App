// Gentleface "search" (line-round), MIT. https://gentleface.com/icons/search
import 'package:flutter/widgets.dart';

class SearchIcon extends StatelessWidget {
  const SearchIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _SearchIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _SearchIconPainter extends CustomPainter {
  _SearchIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(15.003, 14.5)
      ..cubicTo(15.003, 14.636, 14.953, 14.754, 14.854, 14.854)
      ..cubicTo(14.754, 14.953, 14.636, 15.003, 14.5, 15.003)
      ..cubicTo(14.364, 15.003, 14.246, 14.953, 14.146, 14.854)
      ..lineTo(10.02, 10.727)
      ..cubicTo(9.573, 11.101, 9.074, 11.396, 8.525, 11.614)
      ..cubicTo(7.874, 11.871, 7.199, 12, 6.5, 12)
      ..cubicTo(5.801, 12, 5.126, 11.871, 4.475, 11.614)
      ..cubicTo(3.769, 11.334, 3.148, 10.926, 2.611, 10.389)
      ..cubicTo(2.074, 9.852, 1.666, 9.231, 1.386, 8.525)
      ..cubicTo(1.129, 7.874, 1, 7.199, 1, 6.5)
      ..cubicTo(1, 5.801, 1.129, 5.126, 1.386, 4.475)
      ..cubicTo(1.666, 3.769, 2.074, 3.148, 2.611, 2.611)
      ..cubicTo(3.148, 2.074, 3.769, 1.666, 4.475, 1.386)
      ..cubicTo(5.126, 1.129, 5.801, 1, 6.5, 1)
      ..cubicTo(7.199, 1, 7.874, 1.129, 8.525, 1.386)
      ..cubicTo(9.231, 1.666, 9.852, 2.074, 10.389, 2.611)
      ..cubicTo(10.926, 3.148, 11.334, 3.769, 11.614, 4.475)
      ..cubicTo(11.871, 5.126, 12, 5.801, 12, 6.5)
      ..cubicTo(12, 7.199, 11.871, 7.874, 11.614, 8.525)
      ..cubicTo(11.396, 9.074, 11.101, 9.573, 10.727, 10.02)
      ..lineTo(14.854, 14.146)
      ..cubicTo(14.953, 14.246, 15.003, 14.364, 15.003, 14.5)
      ..close()
      ..moveTo(9.98, 9.273)
      ..lineTo(10.016, 9.309)
      ..cubicTo(10.295, 8.962, 10.517, 8.577, 10.684, 8.156)
      ..cubicTo(10.895, 7.624, 11, 7.072, 11, 6.5)
      ..cubicTo(11, 5.928, 10.895, 5.376, 10.684, 4.844)
      ..cubicTo(10.455, 4.266, 10.121, 3.757, 9.682, 3.318)
      ..cubicTo(9.243, 2.879, 8.734, 2.545, 8.156, 2.316)
      ..cubicTo(7.624, 2.105, 7.072, 2, 6.5, 2)
      ..cubicTo(5.928, 2, 5.376, 2.105, 4.844, 2.316)
      ..cubicTo(4.266, 2.545, 3.757, 2.879, 3.318, 3.318)
      ..cubicTo(2.879, 3.757, 2.545, 4.266, 2.316, 4.844)
      ..cubicTo(2.105, 5.376, 2, 5.928, 2, 6.5)
      ..cubicTo(2, 7.072, 2.105, 7.624, 2.316, 8.156)
      ..cubicTo(2.545, 8.734, 2.879, 9.243, 3.318, 9.682)
      ..cubicTo(3.757, 10.121, 4.266, 10.455, 4.844, 10.684)
      ..cubicTo(5.376, 10.895, 5.928, 11, 6.5, 11)
      ..cubicTo(7.072, 11, 7.624, 10.895, 8.156, 10.684)
      ..cubicTo(8.577, 10.517, 8.962, 10.295, 9.309, 10.016)
      ..lineTo(9.273, 9.98)
      ..cubicTo(9.535, 9.772, 9.772, 9.535, 9.98, 9.273)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_SearchIconPainter old) => old.color != color;
}
