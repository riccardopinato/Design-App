// Original component: RXN-animated-gradient-text, Ruixen MIT.
// https://github.com/ruixenui/ruixen.com/blob/f6b20860623fa39122ac2b5f0e5bd29a9eb10941/registry/ruixenui/animated-gradient-text.tsx
// Independent Flutter adaptation; no React runtime or Material UI dependency.
import 'dart:math' as math;
import 'package:flutter/widgets.dart';

class RxnAnimatedGradientText extends StatefulWidget {
  const RxnAnimatedGradientText({
    super.key,
    required this.text,
    this.from = const Color(0xFFFFAA40),
    this.to = const Color(0xFF9C40FF),
    this.speed = 1,
    this.style,
  }) : assert(speed > 0);
  final String text;
  final Color from;
  final Color to;
  final double speed;
  final TextStyle? style;

  @override
  State<RxnAnimatedGradientText> createState() => _RxnAnimatedGradientTextState();
}

class _RxnAnimatedGradientTextState extends State<RxnAnimatedGradientText>
    with SingleTickerProviderStateMixin {
  late final AnimationController _animation;
  Duration get _duration => Duration(milliseconds: math.max(300, (3000 / widget.speed).round()));
  @override
  void initState() {
    super.initState();
    _animation = AnimationController(vsync: this, duration: _duration)..repeat();
  }
  @override
  void didUpdateWidget(covariant RxnAnimatedGradientText oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.speed != oldWidget.speed) {
      _animation.duration = _duration;
      _animation.repeat();
    }
  }
  @override
  Widget build(BuildContext context) {
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) {
        final phase = reduced ? 0.0 : _animation.value;
        return ShaderMask(
          blendMode: BlendMode.srcIn,
          shaderCallback: (bounds) => LinearGradient(
            begin: Alignment(-3 + 6 * phase, 0),
            end: Alignment(-1 + 6 * phase, 0),
            colors: [widget.from, widget.to, widget.from],
          ).createShader(bounds),
          child: child,
        );
      },
      child: Text(widget.text, style: widget.style),
    );
  }
  @override
  void dispose() {
    _animation.dispose();
    super.dispose();
  }
}
