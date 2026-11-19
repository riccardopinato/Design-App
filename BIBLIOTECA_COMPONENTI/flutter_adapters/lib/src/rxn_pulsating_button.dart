// Native Flutter rewrite of pinned Ruixen MIT pulsating-button.tsx.
// Original TSX preserved, Flutter replaces CSS pulse with an AnimationController.
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

class RxnPulsatingButton extends StatefulWidget {
  const RxnPulsatingButton({
    super.key,
    required this.label,
    required this.onPressed,
    this.pulseColor = const Color(0xFF808080),
    this.background = const Color(0xFF5266D2),
    this.textColor = const Color(0xFFFFFFFF),
    this.pulseDuration = const Duration(milliseconds: 1500),
    this.width = 160,
    this.height = 48,
  }) : assert(width > 0), assert(height > 0);

  final String label;
  final VoidCallback? onPressed;
  final Color pulseColor, background, textColor;
  final Duration pulseDuration;
  final double width, height;

  @override
  State<RxnPulsatingButton> createState() => _RxnPulsatingButtonState();
}

class _RxnPulsatingButtonState extends State<RxnPulsatingButton>
    with SingleTickerProviderStateMixin {
  late final AnimationController _pulse;
  @override
  void initState() {
    super.initState();
    _pulse = AnimationController(vsync: this, duration: widget.pulseDuration)..repeat();
  }
  @override
  void didUpdateWidget(covariant RxnPulsatingButton oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.pulseDuration != widget.pulseDuration) {
      _pulse.duration = widget.pulseDuration;
      _pulse.repeat();
    }
  }
  @override
  Widget build(BuildContext context) {
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    final radius = BorderRadius.circular(9);
    return Semantics(
      button: true,
      enabled: widget.onPressed != null,
      label: widget.label,
      child: Focus(
        onKeyEvent: (_, event) {
          if (widget.onPressed != null && event is KeyDownEvent &&
              (event.logicalKey == LogicalKeyboardKey.enter ||
               event.logicalKey == LogicalKeyboardKey.space)) {
            widget.onPressed!();
            return KeyEventResult.handled;
          }
          return KeyEventResult.ignored;
        },
        child: MouseRegion(
          cursor: widget.onPressed == null ? SystemMouseCursors.basic : SystemMouseCursors.click,
          child: GestureDetector(
            onTap: widget.onPressed,
            child: SizedBox(
              width: widget.width,
              height: widget.height,
              child: Stack(
                clipBehavior: Clip.none,
                children: [
                  if (widget.onPressed != null)
                    Positioned.fill(
                      child: AnimatedBuilder(
                        animation: _pulse,
                        builder: (_, __) {
                          final progress = reduced ? 0.0 : _pulse.value;
                          return Transform.scale(
                            scale: 1 + 0.22 * progress,
                            child: DecoratedBox(
                              decoration: BoxDecoration(
                                color: widget.pulseColor.withValues(
                                  alpha: reduced ? 0.12 : (0.32 * (1 - progress)),
                                ),
                                borderRadius: radius,
                              ),
                            ),
                          );
                        },
                      ),
                    ),
                  Positioned.fill(
                    child: DecoratedBox(
                      decoration: BoxDecoration(
                        color: widget.onPressed == null
                            ? widget.background.withValues(alpha: 0.48)
                            : widget.background,
                        borderRadius: radius,
                      ),
                      child: Center(
                        child: Text(widget.label,
                            style: TextStyle(
                              color: widget.textColor,
                              fontSize: 15,
                              fontWeight: FontWeight.w600,
                            )),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
  @override
  void dispose() {
    _pulse.dispose();
    super.dispose();
  }
}
