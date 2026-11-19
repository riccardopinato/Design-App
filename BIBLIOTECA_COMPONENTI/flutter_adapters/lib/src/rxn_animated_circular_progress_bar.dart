// Original component: RXN-animated-circular-progress-bar, Ruixen MIT.
// https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/animated-circular-progress-bar.tsx
// Native Flutter canvas implementation; independent from React/CSS.
import 'dart:math' as math;
import 'package:flutter/widgets.dart';

class RxnAnimatedCircularProgressBar extends StatelessWidget {
  const RxnAnimatedCircularProgressBar({
    super.key,
    required this.value,
    this.min = 0,
    this.max = 100,
    this.size = 160,
    this.primary = const Color(0xFF7753FF),
    this.secondary = const Color(0xFFE9E7F2),
    this.duration = const Duration(milliseconds: 900),
  }) : assert(max > min), assert(size > 0);
  final double value;
  final double min;
  final double max;
  final double size;
  final Color primary;
  final Color secondary;
  final Duration duration;

  @override
  Widget build(BuildContext context) {
    final fraction = ((value - min) / (max - min)).clamp(0.0, 1.0);
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    return Semantics(
      label: 'Progresso',
      value: '${(fraction * 100).round()}%',
      child: TweenAnimationBuilder<double>(
        tween: Tween<double>(end: fraction),
        duration: reduced ? Duration.zero : duration,
        curve: Curves.easeInOutCubic,
        builder: (context, current, _) => SizedBox.square(
          dimension: size,
          child: Stack(
            alignment: Alignment.center,
            children: [
              CustomPaint(
                size: Size.square(size),
                painter: _RingPainter(current, primary, secondary),
              ),
              Text(
                '${(current * 100).round()}',
                style: TextStyle(fontSize: size * .17, fontWeight: FontWeight.w600),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _RingPainter extends CustomPainter {
  _RingPainter(this.fraction, this.primary, this.secondary);
  final double fraction;
  final Color primary;
  final Color secondary;
  @override
  void paint(Canvas canvas, Size size) {
    final width = size.shortestSide * .10;
    final rect = Rect.fromCircle(
      center: Offset(size.width / 2, size.height / 2),
      radius: (size.shortestSide - width) / 2,
    );
    final background = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = width
      ..strokeCap = StrokeCap.round
      ..color = secondary;
    final foreground = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = width
      ..strokeCap = StrokeCap.round
      ..color = primary;
    canvas.drawArc(rect, -math.pi / 2, 2 * math.pi, false, background);
    if (fraction > 0) {
      canvas.drawArc(rect, -math.pi / 2, 2 * math.pi * fraction, false, foreground);
    }
  }
  @override
  bool shouldRepaint(covariant _RingPainter old) =>
      old.fraction != fraction || old.primary != primary || old.secondary != secondary;
}
