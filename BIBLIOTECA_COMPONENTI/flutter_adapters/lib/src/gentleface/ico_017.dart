// Gentleface "cloud" (line-round), MIT. https://gentleface.com/icons/cloud
import 'package:flutter/widgets.dart';

class CloudIcon extends StatelessWidget {
  const CloudIcon({super.key, this.size = 16, this.color});
  final double size;
  final Color? color;

  @override
  Widget build(BuildContext context) => CustomPaint(
        size: Size.square(size),
        painter: _CloudIconPainter(color ?? IconTheme.of(context).color ?? const Color(0xFF000000)),
      );
}

class _CloudIconPainter extends CustomPainter {
  _CloudIconPainter(this.color);
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 16, size.height / 16);
    final p = Path()
      ..moveTo(4.16, 12.649)
      ..cubicTo(3.518, 12.395, 2.953, 12.024, 2.464, 11.536)
      ..cubicTo(1.976, 11.047, 1.605, 10.482, 1.351, 9.84)
      ..cubicTo(1.117, 9.249, 1, 8.636, 1, 8)
      ..cubicTo(1, 7.364, 1.117, 6.751, 1.351, 6.16)
      ..cubicTo(1.605, 5.518, 1.976, 4.953, 2.464, 4.464)
      ..cubicTo(2.953, 3.976, 3.518, 3.605, 4.16, 3.351)
      ..cubicTo(4.751, 3.117, 5.364, 3, 6, 3)
      ..cubicTo(6.636, 3, 7.249, 3.117, 7.84, 3.351)
      ..cubicTo(8.482, 3.605, 9.047, 3.976, 9.536, 4.464)
      ..cubicTo(10.024, 4.953, 10.395, 5.518, 10.649, 6.16)
      ..cubicTo(10.783, 6.497, 10.878, 6.842, 10.935, 7.194)
      ..cubicTo(11.088, 7.137, 11.245, 7.092, 11.409, 7.059)
      ..cubicTo(11.911, 6.958, 12.406, 6.984, 12.895, 7.136)
      ..cubicTo(13.383, 7.289, 13.805, 7.55, 14.16, 7.918)
      ..cubicTo(14.474, 8.244, 14.703, 8.622, 14.846, 9.051)
      ..cubicTo(14.989, 9.481, 15.033, 9.92, 14.977, 10.369)
      ..cubicTo(14.914, 10.877, 14.733, 11.339, 14.434, 11.754)
      ..cubicTo(14.134, 12.169, 13.754, 12.487, 13.292, 12.708)
      ..cubicTo(12.883, 12.903, 12.453, 13, 12, 13)
      ..lineTo(6, 13)
      ..cubicTo(5.364, 13, 4.751, 12.883, 4.16, 12.649)
      ..close()
      ..moveTo(12.861, 11.805)
      ..cubicTo(13.169, 11.658, 13.423, 11.446, 13.622, 11.169)
      ..cubicTo(13.822, 10.893, 13.943, 10.585, 13.985, 10.246)
      ..cubicTo(14.022, 9.947, 13.993, 9.654, 13.897, 9.368)
      ..cubicTo(13.802, 9.081, 13.65, 8.83, 13.44, 8.612)
      ..cubicTo(13.203, 8.366, 12.922, 8.193, 12.596, 8.091)
      ..cubicTo(12.271, 7.989, 11.94, 7.972, 11.606, 8.039)
      ..cubicTo(11.31, 8.099, 11.041, 8.219, 10.8, 8.4)
      ..cubicTo(10.711, 8.467, 10.611, 8.5, 10.5, 8.5)
      ..cubicTo(10.359, 8.5, 10.241, 8.452, 10.144, 8.356)
      ..cubicTo(10.048, 8.259, 10, 8.141, 10, 8)
      ..cubicTo(10, 7.491, 9.906, 7.001, 9.719, 6.528)
      ..cubicTo(9.516, 6.014, 9.219, 5.562, 8.828, 5.172)
      ..cubicTo(8.438, 4.781, 7.986, 4.484, 7.472, 4.281)
      ..cubicTo(6.999, 4.094, 6.509, 4, 6, 4)
      ..cubicTo(5.491, 4, 5.001, 4.094, 4.528, 4.281)
      ..cubicTo(4.014, 4.484, 3.562, 4.781, 3.172, 5.172)
      ..cubicTo(2.781, 5.562, 2.484, 6.014, 2.281, 6.528)
      ..cubicTo(2.094, 7.001, 2, 7.491, 2, 8)
      ..cubicTo(2, 8.509, 2.094, 8.999, 2.281, 9.472)
      ..cubicTo(2.484, 9.986, 2.781, 10.438, 3.172, 10.828)
      ..cubicTo(3.562, 11.219, 4.014, 11.516, 4.528, 11.719)
      ..cubicTo(5.001, 11.906, 5.491, 12, 6, 12)
      ..lineTo(12, 12)
      ..cubicTo(12.302, 12, 12.589, 11.935, 12.861, 11.805)
      ..close();
    canvas.drawPath(p, Paint()..color = color);
  }

  @override
  bool shouldRepaint(_CloudIconPainter old) => old.color != color;
}
