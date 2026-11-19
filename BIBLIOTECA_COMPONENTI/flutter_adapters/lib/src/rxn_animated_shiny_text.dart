// Flutter adaptation of Ruixen MIT original animated-shiny-text.tsx.
// Original pinned TSX stays in BIBLIOTECA_COMPONENTI/sorgenti/ruixen.
// Native color-mask shimmer without React, Tailwind, or external packages.
import 'dart:math' as math;
import 'package:flutter/widgets.dart';

class RxnAnimatedShinyText extends StatefulWidget {
  const RxnAnimatedShinyText({
    super.key,
    required this.text,
    this.shimmerWidth = 100,
    this.duration = const Duration(milliseconds: 1600),
    this.baseColor = const Color(0xFF777777),
    this.shineColor = const Color(0xFFF6F6F6),
    this.style,
  }) : assert(shimmerWidth > 0), assert(duration > Duration.zero);

  final String text;
  final double shimmerWidth;
  final Duration duration;
  final Color baseColor;
  final Color shineColor;
  final TextStyle? style;

  @override
  State<RxnAnimatedShinyText> createState() => _RxnAnimatedShinyTextState();
}

class _RxnAnimatedShinyTextState extends State<RxnAnimatedShinyText>
    with SingleTickerProviderStateMixin {
  late final AnimationController _animation;

  @override
  void initState() {
    super.initState();
    _animation = AnimationController(vsync: this, duration: widget.duration)
      ..repeat();
  }

  @override
  void didUpdateWidget(covariant RxnAnimatedShinyText oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.duration != oldWidget.duration) {
      _animation.duration = widget.duration;
      _animation.repeat();
    }
  }

  @override
  Widget build(BuildContext context) {
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    return AnimatedBuilder(
      animation: _animation,
      builder: (_, child) => ShaderMask(
        blendMode: BlendMode.srcIn,
        shaderCallback: (bounds) {
          final frac = (widget.shimmerWidth / math.max(1, bounds.width))
              .clamp(0.05, 1.0);
          final progress = reduced ? 0.5 : _animation.value;
          final center = -1.0 - frac + (2 + 2 * frac) * progress;
          return LinearGradient(
            begin: Alignment(center - frac, 0),
            end: Alignment(center + frac, 0),
            colors: [widget.baseColor, widget.shineColor, widget.baseColor],
            stops: const [0.0, 0.5, 1.0],
          ).createShader(bounds);
        },
        child: child,
      ),
      child: Text(widget.text, style: widget.style),
    );
  }

  @override
  void dispose() {
    _animation.dispose();
    super.dispose();
  }
}
