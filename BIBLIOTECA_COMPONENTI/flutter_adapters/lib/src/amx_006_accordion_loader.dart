// Native Flutter port of Amicro MIT original amx-006.tsx, retained separately.
import 'package:flutter/widgets.dart';

class Amx006AccordionLoader extends StatefulWidget {
  const Amx006AccordionLoader({
    super.key,
    this.size = 40,
    this.duration = const Duration(milliseconds: 1500),
    this.color = const Color(0xFF27272A),
  }) : assert(size > 0);
  final double size;
  final Duration duration;
  final Color color;
  @override
  State<Amx006AccordionLoader> createState() => _Amx006AccordionLoaderState();
}

class _Amx006AccordionLoaderState extends State<Amx006AccordionLoader>
    with SingleTickerProviderStateMixin {
  late final AnimationController _progress;
  @override
  void initState() {
    super.initState();
    _progress = AnimationController(vsync: this, duration: widget.duration)
      ..repeat();
  }
  @override
  void didUpdateWidget(covariant Amx006AccordionLoader old) {
    super.didUpdateWidget(old);
    if (old.duration != widget.duration) {
      _progress.duration = widget.duration;
      _progress.repeat();
    }
  }
  @override
  Widget build(BuildContext context) {
    final reduced = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    return Semantics(
      label: 'Caricamento',
      liveRegion: true,
      child: ExcludeSemantics(
        child: SizedBox.square(
          dimension: widget.size,
          child: AnimatedBuilder(
            animation: _progress,
            builder: (_, __) => Column(
              mainAxisAlignment: MainAxisAlignment.center,
              mainAxisSize: MainAxisSize.min,
              children: List.generate(4, (index) {
                final t = ((_progress.value - index * .10) % 1 + 1) % 1;
                final triangle = t < .5 ? 2 * t : 2 * (1 - t);
                final fraction = reduced
                    ? 1.0
                    : 1 - .8 * Curves.easeInOut.transform(triangle);
                return Padding(
                  padding: EdgeInsets.only(bottom: index == 3 ? 0 : widget.size * .15),
                  child: Transform.scale(
                    scaleX: fraction,
                    alignment: Alignment.centerLeft,
                    child: SizedBox(
                      height: widget.size * .10,
                      width: widget.size,
                      child: DecoratedBox(
                        decoration: BoxDecoration(
                          color: widget.color,
                          borderRadius: BorderRadius.circular(widget.size * .05),
                        ),
                      ),
                    ),
                  ),
                );
              }),
            ),
          ),
        ),
      ),
    );
  }
  @override
  void dispose() { _progress.dispose(); super.dispose(); }
}
