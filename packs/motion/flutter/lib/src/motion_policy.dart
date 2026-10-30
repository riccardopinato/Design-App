import 'package:flutter/material.dart';

/// Standard timing shared by reusable App Factory motion primitives.
abstract final class FactoryMotionTokens {
  static const feedback = Duration(milliseconds: 160);
  static const standard = Duration(milliseconds: 220);
  static const emphasized = Duration(milliseconds: 260);
  static const Curve enter = Curves.easeOutCubic;
  static const Curve exit = Curves.easeInCubic;
}

/// Accessibility policy for all motion primitives in this package.
///
/// The current screen can further opt out via an enclosing MediaQuery.
abstract final class FactoryMotionPolicy {
  static bool reduceMotion(BuildContext context) {
    final media = MediaQuery.maybeOf(context);
    return media?.disableAnimations == true ||
        media?.accessibleNavigation == true;
  }

  static Duration duration(BuildContext context, Duration requested) {
    return reduceMotion(context) ? Duration.zero : requested;
  }
}
