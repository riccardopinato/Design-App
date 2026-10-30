import 'package:flutter/material.dart';
import 'generated_factory_icon_keys.dart';

/// Presentation-only semantic icon, using the active Material theme.
///
/// If [semanticLabel] is null the icon is decorative. The owning interactive
/// control must then supply an accessible, localized description.
class FactoryIcon extends StatelessWidget {
  const FactoryIcon({
    super.key,
    required this.icon,
    this.size = 24,
    this.color,
    this.semanticLabel,
  });

  final FactoryIconKey icon;
  final double size;
  final Color? color;
  final String? semanticLabel;

  @override
  Widget build(BuildContext context) => Icon(
        icon.materialIcon,
        size: size,
        color: color,
        semanticLabel: semanticLabel,
      );
}

/// Interactive icon with at least a 48x48 logical pixel hit target.
///
/// A nonempty localized [tooltip] is required so that icon-only actions
/// remain accessible; the inner icon has no duplicate semantic label.
class FactoryIconButton extends StatelessWidget {
  const FactoryIconButton({
    super.key,
    required this.icon,
    required this.tooltip,
    required this.onPressed,
    this.color,
  }) : assert(tooltip != '');

  final FactoryIconKey icon;
  final String tooltip;
  final VoidCallback? onPressed;
  final Color? color;

  @override
  Widget build(BuildContext context) => IconButton(
        tooltip: tooltip,
        onPressed: onPressed,
        color: color,
        constraints: const BoxConstraints(minWidth: 48, minHeight: 48),
        icon: FactoryIcon(icon: icon),
      );
}
