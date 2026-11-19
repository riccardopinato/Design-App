// Gentleface "shield-check" (line-round), MIT. https://gentleface.com/icons/shield-check
import 'package:flutter/widgets.dart';

class ShieldCheckIcon extends StatelessWidget {
  const ShieldCheckIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _ShieldCheckIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _ShieldCheckIconPainter extends CustomPainter {
  _ShieldCheckIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(12.528, 10.763)
      ..cubicTo(12.243, 11.414, 11.835, 12.024, 11.302, 12.592)
      ..cubicTo(10.825, 13.101, 10.259, 13.565, 9.605, 13.984)
      ..cubicTo(9.015, 14.362, 8.375, 14.689, 7.686, 14.964)
      ..cubicTo(7.562, 15.014, 7.438, 15.014, 7.314, 14.964)
      ..cubicTo(6.625, 14.689, 5.985, 14.362, 5.395, 13.984)
      ..cubicTo(4.741, 13.565, 4.175, 13.101, 3.698, 12.592)
      ..cubicTo(3.165, 12.024, 2.757, 11.414, 2.472, 10.763)
      ..cubicTo(2.157, 10.044, 2, 9.29, 2, 8.5)
      ..lineTo(2, 3.5)
      ..cubicTo(2, 3.359, 2.048, 3.241, 2.144, 3.144)
      ..cubicTo(2.241, 3.048, 2.359, 3, 2.5, 3)
      ..cubicTo(3.471, 3, 4.307, 2.865, 5.008, 2.596)
      ..cubicTo(5.754, 2.309, 6.467, 1.826, 7.146, 1.146)
      ..cubicTo(7.244, 1.049, 7.362, 1, 7.5, 1)
      ..cubicTo(7.638, 1, 7.756, 1.049, 7.854, 1.146)
      ..cubicTo(8.533, 1.826, 9.246, 2.309, 9.992, 2.596)
      ..cubicTo(10.693, 2.865, 11.529, 3, 12.5, 3)
      ..cubicTo(12.641, 3, 12.759, 3.048, 12.856, 3.144)
      ..cubicTo(12.952, 3.241, 13, 3.359, 13, 3.5)
      ..lineTo(13, 8.5)
      ..cubicTo(13, 9.29, 12.843, 10.044, 12.528, 10.763)
      ..close()
      ..moveTo(4.427, 11.908)
      ..cubicTo(4.848, 12.357, 5.35, 12.768, 5.934, 13.141)
      ..cubicTo(6.418, 13.451, 6.94, 13.724, 7.5, 13.96)
      ..cubicTo(8.06, 13.724, 8.582, 13.451, 9.066, 13.141)
      ..cubicTo(9.65, 12.768, 10.152, 12.357, 10.573, 11.908)
      ..cubicTo(11.524, 10.893, 12, 9.757, 12, 8.5)
      ..lineTo(12, 3.989)
      ..cubicTo(11.111, 3.947, 10.322, 3.794, 9.633, 3.529)
      ..cubicTo(8.886, 3.242, 8.175, 2.795, 7.5, 2.189)
      ..cubicTo(6.825, 2.795, 6.114, 3.242, 5.367, 3.529)
      ..cubicTo(4.678, 3.794, 3.889, 3.947, 3, 3.989)
      ..lineTo(3, 8.5)
      ..cubicTo(3, 9.757, 3.476, 10.893, 4.427, 11.908)
      ..close()
      ..moveTo(10.146, 5.146)
      ..cubicTo(10.246, 5.047, 10.364, 4.997, 10.5, 4.997)
      ..cubicTo(10.636, 4.997, 10.754, 5.047, 10.854, 5.146)
      ..cubicTo(10.951, 5.244, 11, 5.362, 11, 5.5)
      ..cubicTo(11, 5.638, 10.951, 5.756, 10.854, 5.854)
      ..lineTo(6.854, 9.854)
      ..cubicTo(6.754, 9.953, 6.636, 10.003, 6.5, 10.003)
      ..cubicTo(6.364, 10.003, 6.246, 9.953, 6.146, 9.854)
      ..lineTo(4.146, 7.854)
      ..cubicTo(4.047, 7.754, 3.997, 7.636, 3.997, 7.5)
      ..cubicTo(3.997, 7.364, 4.047, 7.246, 4.146, 7.146)
      ..cubicTo(4.246, 7.047, 4.364, 6.997, 4.5, 6.997)
      ..cubicTo(4.636, 6.997, 4.754, 7.047, 4.854, 7.146)
      ..lineTo(6.5, 8.793)
      ..lineTo(10.146, 5.146)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_ShieldCheckIconPainter old) => old.color != color;
}
