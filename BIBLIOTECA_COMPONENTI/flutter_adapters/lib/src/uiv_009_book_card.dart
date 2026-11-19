// Flutter adaptation of UIV-009 by eslam-hany on Uiverse.io.
// Original HTML/CSS preserved at UI-UX/UIVERSE/CODICE_SORGENTE/UIV-009_original.html.
// Full widget, hover and touch interaction; consumer validation is separate.
import 'dart:math' as math;
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

class Uiv009BookCard extends StatefulWidget {
  const Uiv009BookCard({
    super.key,
    this.coverText = 'Hover Me',
    this.insideText = 'Hello',
    this.width = 220,
    this.height = 300,
    this.onOpenChanged,
  }) : assert(width > 0 && height > 0);

  final String coverText;
  final String insideText;
  final double width;
  final double height;
  final ValueChanged<bool>? onOpenChanged;

  @override
  State<Uiv009BookCard> createState() => _Uiv009BookCardState();
}

class _Uiv009BookCardState extends State<Uiv009BookCard> {
  bool _hovered = false;
  bool _toggled = false;
  bool get _opened => _hovered || _toggled;

  void _setHover(bool hovered) {
    final before = _opened;
    setState(() => _hovered = hovered);
    if (before != _opened) widget.onOpenChanged?.call(_opened);
  }

  void _toggle() {
    final before = _opened;
    setState(() => _toggled = !_toggled);
    if (before != _opened) widget.onOpenChanged?.call(_opened);
  }

  @override
  Widget build(BuildContext context) {
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    final radius = BorderRadius.circular(10);
    const shadow = [
      BoxShadow(color: Color(0x77000000), blurRadius: 12, offset: Offset(1, 1)),
    ];
    return Semantics(
      button: true,
      label: widget.coverText,
      value: _opened ? 'Aperto' : 'Chiuso',
      child: Focus(
        onKeyEvent: (_, event) {
          if (event is KeyDownEvent &&
              (event.logicalKey == LogicalKeyboardKey.enter ||
               event.logicalKey == LogicalKeyboardKey.space)) {
            _toggle();
            return KeyEventResult.handled;
          }
          return KeyEventResult.ignored;
        },
        child: MouseRegion(
          cursor: SystemMouseCursors.click,
          onEnter: (_) => _setHover(true),
          onExit: (_) => _setHover(false),
          child: GestureDetector(
            onTap: _toggle,
            child: SizedBox(
              width: widget.width,
              height: widget.height,
              child: Stack(
                clipBehavior: Clip.none,
                children: [
                  DecoratedBox(
                    decoration: BoxDecoration(
                      color: const Color(0xFFF5F5F5),
                      borderRadius: radius,
                      boxShadow: shadow,
                    ),
                    child: SizedBox(
                      width: widget.width,
                      height: widget.height,
                      child: Center(
                        child: Text(widget.insideText,
                            style: const TextStyle(
                                color: Color(0xFF000000),
                                fontWeight: FontWeight.bold,
                                fontSize: 20)),
                      ),
                    ),
                  ),
                  TweenAnimationBuilder<double>(
                    tween: Tween<double>(
                      end: _opened ? -80 * math.pi / 180 : 0,
                    ),
                    curve: Curves.easeInOut,
                    duration: reduced
                        ? Duration.zero
                        : const Duration(milliseconds: 500),
                    builder: (_, angle, child) => Transform(
                      alignment: Alignment.centerLeft,
                      transform: Matrix4.identity()
                        ..setEntry(3, 2, 0.001)
                        ..rotateY(angle),
                      child: child,
                    ),
                    child: DecoratedBox(
                      decoration: BoxDecoration(
                        color: const Color(0xFFD3D3D3),
                        borderRadius: radius,
                        boxShadow: shadow,
                      ),
                      child: SizedBox(
                        width: widget.width,
                        height: widget.height,
                        child: Center(
                          child: Text(widget.coverText,
                              style: const TextStyle(
                                  color: Color(0xFF000000),
                                  fontWeight: FontWeight.bold,
                                  fontSize: 20)),
                        ),
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
}
