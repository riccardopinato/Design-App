// RXN-accordion-editorial — independent Flutter port of original Ruixen MIT TSX.
// Source: registry/ruixenui/accordion-editorial.tsx @ f6b20860623fa39122ac2b5f0e5bd29a9eb10941.
// Deliberately does not import Material, shadcn or an alternate navigation stack.
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

class RxnEditorialAccordionItem {
  const RxnEditorialAccordionItem({required this.id,required this.title,required this.content});
  final String id, title, content;
}

class RxnEditorialAccordion extends StatefulWidget {
  const RxnEditorialAccordion({
    super.key,
    required this.items,
    this.defaultValue,
    this.value,
    this.collapsible = true,
    this.onValueChange,
  });
  final List<RxnEditorialAccordionItem> items;
  final String? defaultValue;
  final String? value;
  final bool collapsible;
  final ValueChanged<String?>? onValueChange;
  @override
  State<RxnEditorialAccordion> createState() => _RxnEditorialAccordionState();
}

class _RxnEditorialAccordionState extends State<RxnEditorialAccordion> {
  String? _expanded;
  @override
  void initState() {
    super.initState();
    _expanded = widget.value ?? widget.defaultValue;
  }
  @override
  void didUpdateWidget(covariant RxnEditorialAccordion oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.value != oldWidget.value && widget.value != null) _expanded = widget.value;
  }
  void _toggle(String id) {
    final active = widget.value ?? _expanded;
    final next = active == id && widget.collapsible ? null : id;
    if (widget.value == null) setState(() => _expanded = next);
    widget.onValueChange?.call(next);
  }
  @override
  Widget build(BuildContext context) {
    final reduce = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    final active = widget.value ?? _expanded;
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: widget.items.map((item) {
        final open = active == item.id;
        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Semantics(
              button: true,
              expanded: open,
              label: item.title,
              child: Focus(
                onKeyEvent: (_, event) {
                  if (event is KeyDownEvent &&
                      (event.logicalKey == LogicalKeyboardKey.enter ||
                       event.logicalKey == LogicalKeyboardKey.space)) {
                    _toggle(item.id);
                    return KeyEventResult.handled;
                  }
                  return KeyEventResult.ignored;
                },
                child: MouseRegion(
                  cursor: SystemMouseCursors.click,
                  child: GestureDetector(
                    onTap: () => _toggle(item.id),
                    child: Padding(
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      child: AnimatedDefaultTextStyle(
                        duration: reduce ? Duration.zero : const Duration(milliseconds: 300),
                        style: TextStyle(
                          fontSize: 20,
                          letterSpacing: -.4,
                          color: open ? const Color(0xE623252D) : const Color(0x5523252D),
                        ),
                        child: Text(item.title),
                      ),
                    ),
                  ),
                ),
              ),
            ),
            ClipRect(
              child: AnimatedSize(
                alignment: Alignment.topCenter,
                duration: reduce ? Duration.zero : const Duration(milliseconds: 300),
                curve: Curves.easeOutCubic,
                child: open
                    ? Padding(
                        padding: const EdgeInsets.only(left: 15, bottom: 8),
                        child: DecoratedBox(
                          decoration: const BoxDecoration(
                            border: Border(left: BorderSide(color: Color(0x2423252D))),
                          ),
                          child: Padding(
                            padding: const EdgeInsets.only(left: 14),
                            child: Text(item.content,
                              style: const TextStyle(height: 1.8,fontSize: 14,color: Color(0x8823252D))),
                          ),
                        ),
                      )
                    : const SizedBox(width: double.infinity),
              ),
            ),
          ],
        );
      }).toList(),
    );
  }
}
