// Gentleface "heart-pulse" (line-round), MIT. https://gentleface.com/icons/heart-pulse
import 'package:flutter/widgets.dart';

class HeartPulseIcon extends StatelessWidget {
  const HeartPulseIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _HeartPulseIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _HeartPulseIconPainter extends CustomPainter {
  _HeartPulseIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(8.653, 13.87)
      ..cubicTo(8.444, 13.957, 8.226, 14, 8, 14)
      ..cubicTo(7.774, 14, 7.556, 13.957, 7.347, 13.87)
      ..cubicTo(7.138, 13.783, 6.953, 13.66, 6.793, 13.5)
      ..lineTo(2.146, 8.854)
      ..cubicTo(1.83, 8.537, 1.566, 8.131, 1.353, 7.634)
      ..cubicTo(1.118, 7.085, 1, 6.541, 1, 6)
      ..cubicTo(1, 5.452, 1.097, 4.928, 1.292, 4.428)
      ..cubicTo(1.476, 3.956, 1.734, 3.535, 2.066, 3.166)
      ..cubicTo(2.393, 2.802, 2.764, 2.519, 3.179, 2.316)
      ..cubicTo(3.61, 2.105, 4.051, 2, 4.5, 2)
      ..cubicTo(4.913, 2, 5.331, 2.065, 5.755, 2.194)
      ..cubicTo(6.147, 2.313, 6.522, 2.48, 6.882, 2.696)
      ..cubicTo(7.23, 2.905, 7.538, 3.143, 7.807, 3.412)
      ..cubicTo(7.875, 3.48, 7.939, 3.549, 8, 3.619)
      ..cubicTo(8.061, 3.549, 8.125, 3.48, 8.193, 3.412)
      ..cubicTo(8.462, 3.143, 8.77, 2.905, 9.118, 2.696)
      ..cubicTo(9.478, 2.48, 9.853, 2.313, 10.245, 2.194)
      ..cubicTo(10.669, 2.065, 11.087, 2, 11.5, 2)
      ..cubicTo(11.949, 2, 12.39, 2.105, 12.821, 2.316)
      ..cubicTo(13.236, 2.519, 13.607, 2.802, 13.934, 3.166)
      ..cubicTo(14.266, 3.535, 14.524, 3.956, 14.708, 4.428)
      ..cubicTo(14.903, 4.928, 15, 5.452, 15, 6)
      ..cubicTo(15, 6.541, 14.882, 7.085, 14.647, 7.634)
      ..cubicTo(14.434, 8.131, 14.17, 8.537, 13.854, 8.854)
      ..lineTo(9.207, 13.5)
      ..cubicTo(9.047, 13.66, 8.862, 13.783, 8.653, 13.87)
      ..close()
      ..moveTo(13.728, 7.241)
      ..cubicTo(13.909, 6.817, 14, 6.404, 14, 6)
      ..cubicTo(14, 5.577, 13.925, 5.174, 13.776, 4.791)
      ..cubicTo(13.637, 4.432, 13.441, 4.113, 13.191, 3.834)
      ..cubicTo(12.951, 3.568, 12.681, 3.361, 12.382, 3.215)
      ..cubicTo(12.089, 3.072, 11.795, 3, 11.5, 3)
      ..cubicTo(11.187, 3, 10.865, 3.05, 10.536, 3.15)
      ..cubicTo(10.223, 3.245, 9.922, 3.38, 9.632, 3.554)
      ..cubicTo(9.355, 3.72, 9.111, 3.909, 8.9, 4.119)
      ..cubicTo(8.699, 4.321, 8.548, 4.522, 8.447, 4.724)
      ..cubicTo(8.398, 4.823, 8.323, 4.898, 8.224, 4.947)
      ..cubicTo(8.098, 5.01, 7.97, 5.02, 7.841, 4.977)
      ..cubicTo(7.712, 4.934, 7.616, 4.85, 7.553, 4.724)
      ..cubicTo(7.452, 4.522, 7.301, 4.321, 7.1, 4.119)
      ..cubicTo(6.889, 3.909, 6.645, 3.72, 6.368, 3.554)
      ..cubicTo(6.078, 3.38, 5.777, 3.245, 5.464, 3.15)
      ..cubicTo(5.135, 3.05, 4.813, 3, 4.5, 3)
      ..cubicTo(4.205, 3, 3.911, 3.072, 3.618, 3.215)
      ..cubicTo(3.319, 3.361, 3.049, 3.568, 2.809, 3.834)
      ..cubicTo(2.559, 4.113, 2.363, 4.432, 2.224, 4.791)
      ..cubicTo(2.075, 5.174, 2, 5.577, 2, 6)
      ..cubicTo(2, 6.404, 2.091, 6.817, 2.272, 7.241)
      ..cubicTo(2.401, 7.542, 2.551, 7.796, 2.72, 8)
      ..lineTo(4.573, 8)
      ..cubicTo(4.762, 8, 4.938, 7.95, 5.099, 7.851)
      ..cubicTo(5.26, 7.751, 5.383, 7.617, 5.467, 7.447)
      ..lineTo(6.053, 6.276)
      ..cubicTo(6.116, 6.15, 6.212, 6.066, 6.341, 6.023)
      ..cubicTo(6.47, 5.98, 6.598, 5.99, 6.724, 6.053)
      ..cubicTo(6.823, 6.102, 6.898, 6.177, 6.947, 6.276)
      ..lineTo(8.5, 9.382)
      ..lineTo(8.638, 9.106)
      ..cubicTo(8.808, 8.767, 9.053, 8.498, 9.376, 8.299)
      ..cubicTo(9.698, 8.1, 10.048, 8, 10.427, 8)
      ..lineTo(13.28, 8)
      ..cubicTo(13.449, 7.796, 13.599, 7.542, 13.728, 7.241)
      ..close()
      ..moveTo(10.427, 9)
      ..cubicTo(10.238, 9, 10.062, 9.05, 9.901, 9.149)
      ..cubicTo(9.74, 9.249, 9.617, 9.383, 9.533, 9.553)
      ..lineTo(8.947, 10.724)
      ..cubicTo(8.898, 10.823, 8.823, 10.898, 8.724, 10.947)
      ..cubicTo(8.6, 11.009, 8.473, 11.018, 8.342, 10.974)
      ..cubicTo(8.211, 10.931, 8.115, 10.847, 8.053, 10.724)
      ..lineTo(6.5, 7.618)
      ..lineTo(6.362, 7.894)
      ..cubicTo(6.192, 8.233, 5.947, 8.502, 5.624, 8.701)
      ..cubicTo(5.302, 8.9, 4.952, 9, 4.573, 9)
      ..lineTo(3.707, 9)
      ..lineTo(7.5, 12.793)
      ..cubicTo(7.638, 12.931, 7.805, 13, 8, 13)
      ..cubicTo(8.195, 13, 8.362, 12.931, 8.5, 12.793)
      ..lineTo(12.293, 9)
      ..lineTo(10.427, 9)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_HeartPulseIconPainter old) => old.color != color;
}
