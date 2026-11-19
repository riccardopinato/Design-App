// Native Flutter rewrite of the pinned Ruixen MIT grid-pattern.tsx original.
// Original source preserved in BIBLIOTECA_COMPONENTI/sorgenti/ruixen/grid-pattern.tsx.
import 'package:flutter/widgets.dart';

class RxnGridPattern extends StatelessWidget {
  const RxnGridPattern({
    super.key,
    this.cellWidth = 40,
    this.cellHeight = 40,
    this.offsetX = -1,
    this.offsetY = -1,
    this.squares = const [],
    this.strokeColor = const Color(0x4D9CA3AF),
    this.fillColor = const Color(0x4D9CA3AF),
    this.child,
  }) : assert(cellWidth > 0), assert(cellHeight > 0);

  final double cellWidth, cellHeight, offsetX, offsetY;
  final List<Offset> squares;
  final Color strokeColor, fillColor;
  final Widget? child;

  @override
  Widget build(BuildContext context) => ExcludeSemantics(
        excluding: child == null,
        child: Stack(
          fit: StackFit.expand,
          children: [
            CustomPaint(
              painter: _GridPainter(
                cellWidth: cellWidth,
                cellHeight: cellHeight,
                offsetX: offsetX,
                offsetY: offsetY,
                squares: squares,
                strokeColor: strokeColor,
                fillColor: fillColor,
              ),
            ),
            if (child != null) child!,
          ],
        ),
      );
}

class _GridPainter extends CustomPainter {
  const _GridPainter({
    required this.cellWidth,
    required this.cellHeight,
    required this.offsetX,
    required this.offsetY,
    required this.squares,
    required this.strokeColor,
    required this.fillColor,
  });
  final double cellWidth, cellHeight, offsetX, offsetY;
  final List<Offset> squares;
  final Color strokeColor, fillColor;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save();
    canvas.clipRect(Offset.zero & size);
    final line = Paint()
      ..color = strokeColor
      ..strokeWidth = 1
      ..style = PaintingStyle.stroke;
    final firstX = offsetX % cellWidth;
    final firstY = offsetY % cellHeight;
    for (double x = firstX; x <= size.width; x += cellWidth) {
      canvas.drawLine(Offset(x + 0.5, 0), Offset(x + 0.5, size.height), line);
    }
    for (double y = firstY; y <= size.height; y += cellHeight) {
      canvas.drawLine(Offset(0, y + 0.5), Offset(size.width, y + 0.5), line);
    }
    final fill = Paint()..color = fillColor;
    for (final square in squares) {
      canvas.drawRect(
        Rect.fromLTWH(
          firstX + square.dx * cellWidth + 1,
          firstY + square.dy * cellHeight + 1,
          cellWidth - 1,
          cellHeight - 1,
        ),
        fill,
      );
    }
    canvas.restore();
  }
  @override
  bool shouldRepaint(covariant _GridPainter old) =>
      old.cellWidth != cellWidth ||
      old.cellHeight != cellHeight ||
      old.offsetX != offsetX ||
      old.offsetY != offsetY ||
      old.strokeColor != strokeColor ||
      old.fillColor != fillColor ||
      old.squares != squares;
}
