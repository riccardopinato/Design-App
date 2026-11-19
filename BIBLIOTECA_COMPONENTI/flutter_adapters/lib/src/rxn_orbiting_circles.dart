// Original MIT TSX: Ruixen orbiting-circles.tsx @
// f6b20860623fa39122ac2b5f0e5bd29a9eb10941.
// Native Flutter orbit animation with exact source-driven radius, period,
// direction and optional circular path, not a static illustration.
import 'dart:math' as math;
import 'package:flutter/widgets.dart';

class RxnOrbitingCircles extends StatefulWidget {
  const RxnOrbitingCircles({
    super.key,
    required this.children,
    this.radius = 160,
    this.iconSize = 30,
    this.duration = const Duration(seconds: 20),
    this.speed = 1,
    this.reverse = false,
    this.showPath = true,
    this.pathColor = const Color(0x1A000000),
  }) : assert(radius > 0), assert(iconSize > 0), assert(speed > 0);

  final List<Widget> children;
  final double radius, iconSize, speed;
  final Duration duration;
  final bool reverse, showPath;
  final Color pathColor;

  @override
  State<RxnOrbitingCircles> createState() => _RxnOrbitingCirclesState();
}

class _RxnOrbitingCirclesState extends State<RxnOrbitingCircles>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;

  Duration get _effectiveDuration =>
      Duration(microseconds: (widget.duration.inMicroseconds / widget.speed).round());

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: _effectiveDuration)
      ..repeat();
  }

  @override
  void didUpdateWidget(covariant RxnOrbitingCircles old) {
    super.didUpdateWidget(old);
    if (old.duration != widget.duration || old.speed != widget.speed) {
      _controller.duration = _effectiveDuration;
      _controller.repeat();
    }
  }

  @override
  Widget build(BuildContext context) {
    final reduce = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    final dimension = widget.radius * 2 + widget.iconSize;
    return SizedBox.square(
      dimension: dimension,
      child: AnimatedBuilder(
        animation: _controller,
        builder: (_, __) => Stack(
          clipBehavior: Clip.none,
          alignment: Alignment.center,
          children: [
            if (widget.showPath)
              Positioned.fill(
                child: ExcludeSemantics(
                  child: CustomPaint(
                    painter: _OrbitPathPainter(
                      radius: widget.radius,
                      color: widget.pathColor,
                    ),
                  ),
                ),
              ),
            for (var i = 0; i < widget.children.length; i++)
              Transform.translate(
                offset: Offset(
                  widget.radius * math.cos(
                    2 * math.pi * (i / widget.children.length +
                        (widget.reverse ? -1 : 1) * (reduce ? 0 : _controller.value)),
                  ),
                  widget.radius * math.sin(
                    2 * math.pi * (i / widget.children.length +
                        (widget.reverse ? -1 : 1) * (reduce ? 0 : _controller.value)),
                  ),
                ),
                child: SizedBox.square(
                  dimension: widget.iconSize,
                  child: widget.children[i],
                ),
              ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}

class _OrbitPathPainter extends CustomPainter {
  const _OrbitPathPainter({required this.radius, required this.color});
  final double radius;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.drawCircle(
      size.center(Offset.zero),
      radius,
      Paint()..color = color..strokeWidth = 1..style = PaintingStyle.stroke,
    );
  }

  @override
  bool shouldRepaint(covariant _OrbitPathPainter old) =>
      old.radius != radius || old.color != color;
}
