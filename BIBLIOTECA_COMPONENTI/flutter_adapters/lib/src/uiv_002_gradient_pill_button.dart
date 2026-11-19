// Original UIV-002 by xueyuantan on Uiverse.io, HTML/CSS archived.
// Independent Flutter implementation, preserving source attribution.
// The original code remains at UI-UX/UIVERSE/CODICE_SORGENTE/UIV-002_original.html.
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

class Uiv002GradientPillButton extends StatefulWidget {
  const Uiv002GradientPillButton({
    super.key,
    required this.label,
    required this.onPressed,
    this.width = 135,
    this.height = 45,
  });
  final String label;
  final VoidCallback? onPressed;
  final double width;
  final double height;
  @override
  State<Uiv002GradientPillButton> createState() => _Uiv002GradientPillButtonState();
}

class _Uiv002GradientPillButtonState extends State<Uiv002GradientPillButton>
    with SingleTickerProviderStateMixin {
  late final AnimationController _fill;
  bool _focused = false, _hovered = false, _pressed = false;
  @override
  void initState() {
    super.initState();
    _fill = AnimationController(vsync: this, duration: const Duration(milliseconds: 500));
  }
  void _refresh() {
    if (widget.onPressed == null) return;
    if (_focused || _hovered || _pressed) {
      _fill.forward();
    } else {
      _fill.reverse();
    }
  }
  @override
  Widget build(BuildContext context) {
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    final border = BorderRadius.circular(widget.height / 2);
    return Semantics(
      button: true,
      enabled: widget.onPressed != null,
      label: widget.label,
      child: Focus(
        onFocusChange: (v) { _focused = v; _refresh(); },
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
          onEnter: (_) { _hovered = true; _refresh(); },
          onExit: (_) { _hovered = false; _refresh(); },
          child: GestureDetector(
            onTap: widget.onPressed,
            onTapDown: (_) { _pressed = true; _refresh(); },
            onTapUp: (_) { _pressed = false; _refresh(); },
            onTapCancel: () { _pressed = false; _refresh(); },
            child: SizedBox(
              width: widget.width,
              height: widget.height,
              child: DecoratedBox(
                decoration: BoxDecoration(
                  color: const Color(0xFFFAFAFA),
                  borderRadius: border,
                  boxShadow: const [
                    BoxShadow(offset: Offset(6, 6), blurRadius: 12, color: Color(0xFFC5C5C5)),
                    BoxShadow(offset: Offset(-6, -6), blurRadius: 12, color: Color(0xFFFFFFFF)),
                  ],
                ),
                child: ClipRRect(
                  borderRadius: border,
                  child: AnimatedBuilder(
                    animation: _fill,
                    builder: (_, __) => LayoutBuilder(
                      builder: (_, bounds) => Stack(
                        fit: StackFit.expand,
                        children: [
                          Align(
                            alignment: Alignment.centerLeft,
                            child: SizedBox(
                              width: bounds.maxWidth * (reduced ? (_focused || _hovered || _pressed ? 1 : 0) : _fill.value),
                              height: bounds.maxHeight,
                              child: const DecoratedBox(
                                decoration: BoxDecoration(
                                  gradient: LinearGradient(
                                    colors: [Color(0xFF0FD850), Color(0xFFF9F047)],
                                  ),
                                ),
                              ),
                            ),
                          ),
                          Center(
                            child: Text(widget.label,
                              style: const TextStyle(color: Color(0xFF20232A), fontSize: 15)),
                          ),
                        ],
                      ),
                    ),
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
  void dispose() { _fill.dispose(); super.dispose(); }
}
