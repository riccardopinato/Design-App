import 'package:flutter/material.dart';

import 'motion_policy.dart';

/// Supported, intentionally restrained state transition variants.
enum FactoryMotionEffect { fade, fadeScale, fadeSlide }

/// Replaces a keyed child with a short, functional transition.
///
/// Change [motionKey] when the *logical* content changes. During transitions,
/// outgoing and incoming content may coexist briefly. Do not use this widget
/// around sensitive duplicated controls or focus owners; prefer [MotionExpand].
class MotionSwap extends StatelessWidget {
  const MotionSwap({
    super.key,
    required this.motionKey,
    required this.child,
    this.effect = FactoryMotionEffect.fade,
    this.duration = FactoryMotionTokens.standard,
  });

  final Object motionKey;
  final Widget child;
  final FactoryMotionEffect effect;
  final Duration duration;

  @override
  Widget build(BuildContext context) {
    final keyedChild = KeyedSubtree(
      key: ValueKey<Object>(motionKey),
      child: child,
    );

    if (FactoryMotionPolicy.reduceMotion(context)) {
      return keyedChild;
    }

    return AnimatedSwitcher(
      duration: duration,
      reverseDuration: duration,
      switchInCurve: FactoryMotionTokens.enter,
      switchOutCurve: FactoryMotionTokens.exit,
      transitionBuilder: (widget, animation) {
        final fade = FadeTransition(opacity: animation, child: widget);
        return switch (effect) {
          FactoryMotionEffect.fade => fade,
          FactoryMotionEffect.fadeScale => ScaleTransition(
              scale: Tween<double>(begin: 0.96, end: 1.0).animate(animation),
              child: fade,
            ),
          FactoryMotionEffect.fadeSlide => SlideTransition(
              position: Tween<Offset>(
                begin: const Offset(0, 0.06),
                end: Offset.zero,
              ).animate(animation),
              child: fade,
            ),
        };
      },
      child: keyedChild,
    );
  }
}

/// Expands and collapses without leaving hidden descendants focusable/tappable.
///
/// Reduced-motion mode swaps immediately, with no animated intermediate state.
class MotionExpand extends StatelessWidget {
  const MotionExpand({
    super.key,
    required this.expanded,
    required this.child,
    this.duration = FactoryMotionTokens.standard,
  });

  final bool expanded;
  final Widget child;
  final Duration duration;

  @override
  Widget build(BuildContext context) {
    if (FactoryMotionPolicy.reduceMotion(context)) {
      return expanded ? child : const SizedBox.shrink();
    }

    return AnimatedSize(
      alignment: Alignment.topCenter,
      duration: duration,
      reverseDuration: duration,
      curve: FactoryMotionTokens.enter,
      clipBehavior: Clip.hardEdge,
      child: expanded ? child : const SizedBox.shrink(),
    );
  }
}

/// A short success/completion indicator with explicit accessibility wording.
///
/// The caller must provide a localized [semanticLabel]; no text is hardcoded.
class MotionCompletionBadge extends StatelessWidget {
  const MotionCompletionBadge({
    super.key,
    required this.completed,
    required this.semanticLabel,
    this.icon = Icons.check_rounded,
    this.duration = FactoryMotionTokens.feedback,
  });

  final bool completed;
  final String semanticLabel;
  final IconData icon;
  final Duration duration;

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;

    return MotionSwap(
      motionKey: completed,
      effect: FactoryMotionEffect.fadeScale,
      duration: duration,
      child: completed
          ? Semantics(
              label: semanticLabel,
              liveRegion: true,
              child: ExcludeSemantics(
                child: DecoratedBox(
                  decoration: BoxDecoration(
                    color: scheme.primaryContainer,
                    shape: BoxShape.circle,
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(8),
                    child: Icon(icon, color: scheme.onPrimaryContainer),
                  ),
                ),
              ),
            )
          : const SizedBox.shrink(),
    );
  }
}

/// Selectable Material surface with a 48dp minimum target and state feedback.
///
/// The caller controls selection and provides localized, meaningful child UI.
class MotionSelectionTile extends StatelessWidget {
  const MotionSelectionTile({
    super.key,
    required this.selected,
    required this.child,
    this.onTap,
    this.duration = FactoryMotionTokens.feedback,
  });

  final bool selected;
  final Widget child;
  final VoidCallback? onTap;
  final Duration duration;

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;

    return Semantics(
      button: true,
      selected: selected,
      enabled: onTap != null,
      child: AnimatedContainer(
        duration: FactoryMotionPolicy.duration(context, duration),
        curve: FactoryMotionTokens.enter,
        constraints: const BoxConstraints(minWidth: 48, minHeight: 48),
        decoration: BoxDecoration(
          color: selected ? scheme.secondaryContainer : scheme.surfaceContainerLow,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: selected ? scheme.secondary : scheme.outlineVariant,
          ),
        ),
        child: Material(
          type: MaterialType.transparency,
          child: InkWell(
            onTap: onTap,
            borderRadius: BorderRadius.circular(16),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              child: child,
            ),
          ),
        ),
      ),
    );
  }
}

/// A static skeleton, matching the geometry of the eventual content.
///
/// Avoids perpetual shimmer/battery costs. Usually exclude individual skeleton
/// shapes from semantics and let the screen announce loading once.
class MotionSkeleton extends StatelessWidget {
  const MotionSkeleton({
    super.key,
    required this.width,
    required this.height,
    this.radius = 16,
    this.semanticLabel,
  });

  final double width;
  final double height;
  final double radius;
  final String? semanticLabel;

  @override
  Widget build(BuildContext context) {
    final placeholder = SizedBox(
      width: width,
      height: height,
      child: DecoratedBox(
        decoration: BoxDecoration(
          color: Theme.of(context).colorScheme.surfaceContainerHighest,
          borderRadius: BorderRadius.circular(radius),
        ),
      ),
    );
    if (semanticLabel == null) {
      return ExcludeSemantics(child: placeholder);
    }
    return Semantics(
      label: semanticLabel,
      child: ExcludeSemantics(child: placeholder),
    );
  }
}

/// Hero continuity that disables its own flight when reduced motion is requested.
///
/// Route transitions remain the responsibility of the owning navigator.
class MotionHero extends StatelessWidget {
  const MotionHero({
    super.key,
    required this.tag,
    required this.child,
  });

  final Object tag;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    return HeroMode(
      enabled: !FactoryMotionPolicy.reduceMotion(context),
      child: Hero(tag: tag, child: child),
    );
  }
}
