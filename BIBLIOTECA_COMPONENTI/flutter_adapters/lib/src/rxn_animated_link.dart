// RXN-animated-link — Flutter rewrite of Ruixen MIT original at
// registry/ruixenui/animated-link.tsx @ f6b20860623fa39122ac2b5f0e5bd29a9eb10941.
// Preserves hover/focus underline-wipe direction and accessible activation.
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

enum RxnUnderlineVariant { left, right, center }

class RxnAnimatedLink extends StatefulWidget {
  const RxnAnimatedLink({
    super.key,
    required this.label,
    required this.onTap,
    this.variant = RxnUnderlineVariant.left,
    this.showArrow = true,
    this.color = const Color(0xFF23252D),
  });
  final String label;
  final VoidCallback? onTap;
  final RxnUnderlineVariant variant;
  final bool showArrow;
  final Color color;
  @override
  State<RxnAnimatedLink> createState() => _RxnAnimatedLinkState();
}

class _RxnAnimatedLinkState extends State<RxnAnimatedLink>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  bool _hovered = false, _focused = false;
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this,
      duration: const Duration(milliseconds: 300));
  }
  void _animate() {
    if (_hovered || _focused) {
      _controller.forward();
    } else {
      _controller.reverse();
    }
  }
  @override
  Widget build(BuildContext context) {
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    return Semantics(
      link: true,
      enabled: widget.onTap != null,
      label: widget.label,
      child: Focus(
        onFocusChange: (active) { _focused = active; _animate(); },
        onKeyEvent: (_, event) {
          if (widget.onTap != null && event is KeyDownEvent &&
              (event.logicalKey == LogicalKeyboardKey.enter ||
               event.logicalKey == LogicalKeyboardKey.space)) {
            widget.onTap!();
            return KeyEventResult.handled;
          }
          return KeyEventResult.ignored;
        },
        child: MouseRegion(
          cursor: widget.onTap == null ? SystemMouseCursors.basic : SystemMouseCursors.click,
          onEnter: (_) { _hovered = true; _animate(); },
          onExit: (_) { _hovered = false; _animate(); },
          child: GestureDetector(
            onTap: widget.onTap,
            child: AnimatedBuilder(
              animation: _controller,
              builder: (_, __) => CustomPaint(
                foregroundPainter: _LinkUnderlinePainter(
                  variant: widget.variant,
                  progress: reduced ? (_hovered || _focused ? 1 : 0) : _controller.value,
                  color: widget.color,
                ),
                child: Padding(
                  padding: const EdgeInsets.only(bottom: 5),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(widget.label, style: TextStyle(color: widget.color, fontSize: 16)),
                      if (widget.showArrow) ...[
                        const SizedBox(width: 5),
                        Text('↗', style: TextStyle(color: widget.color, fontSize: 12)),
                      ],
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
  @override
  void dispose() { _controller.dispose(); super.dispose(); }
}

class _LinkUnderlinePainter extends CustomPainter {
  const _LinkUnderlinePainter({required this.variant,required this.progress,required this.color});
  final RxnUnderlineVariant variant;
  final double progress;
  final Color color;
  @override
  void paint(Canvas canvas, Size size) {
    final width = size.width * progress.clamp(0.0, 1.0);
    if (width <= 0) return;
    final start = switch (variant) {
      RxnUnderlineVariant.left => 0.0,
      RxnUnderlineVariant.right => size.width - width,
      RxnUnderlineVariant.center => (size.width - width) / 2,
    };
    canvas.drawRect(
      Rect.fromLTWH(start, size.height - 1.5, width, 1),
      Paint()..color = color,
    );
  }
  @override
  bool shouldRepaint(covariant _LinkUnderlinePainter old) =>
      old.variant != variant || old.progress != progress || old.color != color;
}
