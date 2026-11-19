// Flutter adaptation of Ruixen MIT interactive-hover-button.tsx,
// source pin f6b20860623fa39122ac2b5f0e5bd29a9eb10941.
// Original React TSX preserved in BIBLIOTECA_COMPONENTI/sorgenti/ruixen.
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

class RxnInteractiveHoverButton extends StatefulWidget {
  const RxnInteractiveHoverButton({
    super.key,
    required this.label,
    required this.onPressed,
    this.accent = const Color(0xFF4A55B2),
    this.background = const Color(0xFFFDFDFD),
    this.foreground = const Color(0xFF22242D),
    this.width = 172,
    this.height = 48,
  }) : assert(width > 0 && height > 0);

  final String label;
  final VoidCallback? onPressed;
  final Color accent, background, foreground;
  final double width, height;

  @override
  State<RxnInteractiveHoverButton> createState() =>
      _RxnInteractiveHoverButtonState();
}

class _RxnInteractiveHoverButtonState
    extends State<RxnInteractiveHoverButton> {
  bool _hover = false, _focus = false, _pressed = false;
  bool get _active => _hover || _focus || _pressed;

  @override
  Widget build(BuildContext context) {
    final enabled = widget.onPressed != null;
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    return Semantics(
      button: true,
      enabled: enabled,
      label: widget.label,
      child: Focus(
        onFocusChange: (v) => setState(() => _focus = v),
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
          onEnter: (_) { if (enabled) setState(() => _hover = true); },
          onExit: (_) => setState(() => _hover = false),
          child: GestureDetector(
            onTap: widget.onPressed,
            onTapDown: (_) { if (enabled) setState(() => _pressed = true); },
            onTapUp: (_) => setState(() => _pressed = false),
            onTapCancel: () => setState(() => _pressed = false),
            child: TweenAnimationBuilder<double>(
              tween: Tween<double>(end: enabled && _active ? 1.0 : 0.0),
              duration: reduced ? Duration.zero : const Duration(milliseconds: 300),
              curve: Curves.easeInOut,
              builder: (_, p, __) => Container(
                width: widget.width,
                height: widget.height,
                decoration: BoxDecoration(
                  color: widget.background,
                  borderRadius: BorderRadius.circular(widget.height / 2),
                  border: Border.all(color: widget.accent.withValues(alpha: .25)),
                ),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(widget.height / 2),
                  child: Stack(
                    fit: StackFit.expand,
                    children: [
                      Positioned(
                        left: 24 - (widget.width - 8) * p / 2,
                        top: widget.height / 2 - 4 - (widget.height - 8) * p / 2,
                        child: Container(
                          width: 8 + (widget.width - 8) * p,
                          height: 8 + (widget.height - 8) * p,
                          decoration: BoxDecoration(
                            color: widget.accent,
                            borderRadius: BorderRadius.circular(widget.height / 2),
                          ),
                        ),
                      ),
                      Center(
                        child: Opacity(
                          opacity: 1 - p,
                          child: Transform.translate(
                            offset: Offset(24 * p, 0),
                            child: Text(
                              widget.label,
                              style: TextStyle(
                                color: enabled ? widget.foreground : widget.foreground.withValues(alpha: .45),
                                fontSize: 14,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ),
                        ),
                      ),
                      Center(
                        child: Opacity(
                          opacity: p,
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Text(widget.label, style: const TextStyle(
                                color: Color(0xFFFFFFFF), fontSize: 14, fontWeight: FontWeight.w600,
                              )),
                              const SizedBox(width: 8),
                              const Text('→', style: TextStyle(
                                color: Color(0xFFFFFFFF), fontSize: 18,
                              )),
                            ],
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
