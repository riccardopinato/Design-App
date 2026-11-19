// Gentleface "gauge" (line-round), MIT. https://gentleface.com/icons/gauge
import 'package:flutter/widgets.dart';

class GaugeIcon extends StatelessWidget {
  const GaugeIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _GaugeIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _GaugeIconPainter extends CustomPainter {
  _GaugeIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(1.112, 10.699)
      ..cubicTo(0.966, 9.924, 0.962, 9.148, 1.099, 8.371)
      ..cubicTo(1.236, 7.595, 1.505, 6.867, 1.907, 6.188)
      ..cubicTo(2.284, 5.552, 2.755, 4.996, 3.322, 4.521)
      ..cubicTo(3.888, 4.045, 4.518, 3.677, 5.21, 3.417)
      ..cubicTo(5.948, 3.139, 6.711, 3, 7.5, 3)
      ..cubicTo(8.289, 3, 9.052, 3.139, 9.79, 3.417)
      ..cubicTo(10.482, 3.677, 11.112, 4.045, 11.678, 4.521)
      ..cubicTo(12.245, 4.996, 12.716, 5.552, 13.093, 6.188)
      ..cubicTo(13.495, 6.867, 13.764, 7.595, 13.901, 8.371)
      ..cubicTo(14.038, 9.148, 14.034, 9.924, 13.888, 10.699)
      ..cubicTo(13.752, 11.426, 13.499, 12.109, 13.129, 12.75)
      ..cubicTo(13.06, 12.87, 12.959, 12.947, 12.826, 12.983)
      ..cubicTo(12.692, 13.019, 12.566, 13.002, 12.446, 12.933)
      ..cubicTo(12.327, 12.864, 12.249, 12.763, 12.213, 12.629)
      ..cubicTo(12.177, 12.496, 12.194, 12.37, 12.263, 12.25)
      ..cubicTo(12.576, 11.708, 12.79, 11.129, 12.906, 10.514)
      ..cubicTo(13.029, 9.859, 13.032, 9.202, 12.916, 8.545)
      ..cubicTo(12.801, 7.888, 12.573, 7.272, 12.233, 6.698)
      ..cubicTo(11.914, 6.159, 11.515, 5.689, 11.035, 5.287)
      ..cubicTo(10.556, 4.884, 10.023, 4.573, 9.438, 4.353)
      ..cubicTo(8.813, 4.118, 8.167, 4, 7.5, 4)
      ..cubicTo(6.833, 4, 6.187, 4.118, 5.562, 4.353)
      ..cubicTo(4.977, 4.573, 4.444, 4.884, 3.965, 5.287)
      ..cubicTo(3.485, 5.689, 3.086, 6.159, 2.767, 6.698)
      ..cubicTo(2.427, 7.272, 2.199, 7.888, 2.084, 8.545)
      ..cubicTo(1.968, 9.202, 1.971, 9.859, 2.094, 10.514)
      ..cubicTo(2.21, 11.129, 2.424, 11.708, 2.737, 12.25)
      ..cubicTo(2.806, 12.37, 2.823, 12.496, 2.787, 12.629)
      ..cubicTo(2.751, 12.763, 2.673, 12.864, 2.554, 12.933)
      ..cubicTo(2.434, 13.002, 2.308, 13.019, 2.174, 12.983)
      ..cubicTo(2.041, 12.947, 1.94, 12.87, 1.871, 12.75)
      ..cubicTo(1.501, 12.109, 1.248, 11.426, 1.112, 10.699)
      ..close()
      ..moveTo(10.146, 6.146)
      ..cubicTo(10.246, 6.047, 10.364, 5.997, 10.5, 5.997)
      ..cubicTo(10.636, 5.997, 10.754, 6.047, 10.854, 6.146)
      ..cubicTo(10.951, 6.244, 11, 6.362, 11, 6.5)
      ..cubicTo(11, 6.638, 10.951, 6.756, 10.854, 6.854)
      ..lineTo(8.854, 8.854)
      ..cubicTo(8.951, 9.058, 9, 9.273, 9, 9.5)
      ..cubicTo(9, 9.914, 8.854, 10.268, 8.561, 10.561)
      ..cubicTo(8.268, 10.854, 7.914, 11, 7.5, 11)
      ..cubicTo(7.086, 11, 6.732, 10.854, 6.439, 10.561)
      ..cubicTo(6.146, 10.268, 6, 9.914, 6, 9.5)
      ..cubicTo(6, 9.086, 6.146, 8.732, 6.439, 8.439)
      ..cubicTo(6.732, 8.146, 7.086, 8, 7.5, 8)
      ..cubicTo(7.727, 8, 7.942, 8.049, 8.146, 8.146)
      ..lineTo(10.146, 6.146)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_GaugeIconPainter old) => old.color != color;
}
