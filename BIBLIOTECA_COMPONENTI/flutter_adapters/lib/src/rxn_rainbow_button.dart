// Native Flutter port of the pinned Ruixen MIT rainbow-button.tsx.
// Original TSX, API variants and license remain in the source archive.
// No Material, CSS, React or third-party runtime dependencies.
import 'dart:math' as math;
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

enum RxnRainbowVariant { filled, outline }

class RxnRainbowButton extends StatefulWidget {
  const RxnRainbowButton({
    super.key,
    required this.label,
    required this.onPressed,
    this.variant = RxnRainbowVariant.filled,
    this.width = 158,
    this.height = 44,
    this.duration = const Duration(seconds: 3),
  }) : assert(width > 0 && height > 0);

  final String label;
  final VoidCallback? onPressed;
  final RxnRainbowVariant variant;
  final double width, height;
  final Duration duration;

  @override
  State<RxnRainbowButton> createState() => _RxnRainbowButtonState();
}

class _RxnRainbowButtonState extends State<RxnRainbowButton>
    with SingleTickerProviderStateMixin {
  late final AnimationController _animation;

  @override
  void initState() {
    super.initState();
    _animation = AnimationController(vsync: this, duration: widget.duration)..repeat();
  }

  @override
  void didUpdateWidget(covariant RxnRainbowButton old) {
    super.didUpdateWidget(old);
    if (old.duration != widget.duration) {
      _animation.duration = widget.duration;
      _animation.repeat();
    }
  }

  @override
  Widget build(BuildContext context) {
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    final outline = widget.variant == RxnRainbowVariant.outline;
    final enabled = widget.onPressed != null;
    final radius = BorderRadius.circular(widget.height / 3);
    const colors = <Color>[
      Color(0xFFFC5353), Color(0xFFF9AF44), Color(0xFFEEDB59),
      Color(0xFF4CD5A9), Color(0xFF588BF6), Color(0xFFD468DF),
      Color(0xFFFC5353),
    ];
    return Semantics(
      button: true,
      enabled: enabled,
      label: widget.label,
      child: Focus(
        onKeyEvent: (_, event) {
          if (enabled && event is KeyDownEvent &&
              (event.logicalKey == LogicalKeyboardKey.enter ||
               event.logicalKey == LogicalKeyboardKey.space)) {
            widget.onPressed?.call();
            return KeyEventResult.handled;
          }
          return KeyEventResult.ignored;
        },
        child: MouseRegion(
          cursor: enabled ? SystemMouseCursors.click : SystemMouseCursors.basic,
          child: GestureDetector(
            onTap: widget.onPressed,
            child: AnimatedBuilder(
              animation: _animation,
              builder: (_, child) {
                final rotation = reduced ? 0.0 : _animation.value * math.pi * 2;
                return Opacity(
                  opacity: enabled ? 1 : .5,
                  child: Container(
                    width: widget.width,
                    height: widget.height,
                    decoration: BoxDecoration(
                      borderRadius: radius,
                      gradient: SweepGradient(
                        colors: colors,
                        transform: GradientRotation(rotation),
                      ),
                    ),
                    padding: const EdgeInsets.all(2),
                    child: DecoratedBox(
                      decoration: BoxDecoration(
                        color: outline ? const Color(0xFFFFFFFF) : const Color(0xFF121213),
                        borderRadius: radius,
                      ),
                      child: child,
                    ),
                  ),
                );
              },
              child: Center(
                child: Text(widget.label,
                    style: TextStyle(
                      color: outline ? const Color(0xFF25252B) : const Color(0xFFFFFFFF),
                      fontSize: 14,
                      fontWeight: FontWeight.w600,
                    )),
              ),
            ),
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _animation.dispose();
    super.dispose();
  }
}
