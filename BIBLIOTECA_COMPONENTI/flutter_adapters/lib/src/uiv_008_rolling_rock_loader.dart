// Native Flutter port of Uiverse UIV-008 (Shoh2008), preserving HTML/CSS original.
import 'dart:math' as math;
import 'package:flutter/widgets.dart';

class Uiv008RollingRockLoader extends StatefulWidget {
  const Uiv008RollingRockLoader({
    super.key,
    this.size = 88,
    this.rockColor = const Color(0xFFFFA500),
    this.trackColor = const Color(0xFFFFFFFF),
  }) : assert(size > 0);
  final double size;
  final Color rockColor, trackColor;
  @override
  State<Uiv008RollingRockLoader> createState() => _Uiv008RollingRockLoaderState();
}

class _Uiv008RollingRockLoaderState extends State<Uiv008RollingRockLoader>
    with SingleTickerProviderStateMixin {
  static const poses = <({double t, double x, double y, double deg})>[
    (t:0, x:0, y:-1, deg:-45),
    (t:.05, x:0, y:-1, deg:-50),
    (t:.20, x:1, y:-2, deg:47),
    (t:.25, x:1, y:-2, deg:45),
    (t:.30, x:1, y:-2, deg:40),
    (t:.45, x:2, y:-3, deg:137),
    (t:.50, x:2, y:-3, deg:135),
    (t:.55, x:2, y:-3, deg:130),
    (t:.70, x:3, y:-4, deg:217),
    (t:.75, x:3, y:-4, deg:220),
    (t:1, x:0, y:-1, deg:-225),
  ];
  late final AnimationController _animation;
  @override
  void initState() {
    super.initState();
    _animation = AnimationController(vsync: this,
      duration: const Duration(milliseconds: 2500))..repeat();
  }
  ({double x, double y, double deg}) sample(double phase) {
    for (var i=1; i<poses.length; i++) {
      final a=poses[i-1], b=poses[i];
      if (phase<=b.t) {
        final p=Curves.easeInOutCubic.transform(((phase-a.t)/(b.t-a.t)).clamp(0.0,1.0));
        return (x:a.x+(b.x-a.x)*p, y:a.y+(b.y-a.y)*p, deg:a.deg+(b.deg-a.deg)*p);
      }
    }
    return (x:0, y:-1, deg:-225);
  }
  @override
  Widget build(BuildContext context) {
    final reduced=MediaQuery.maybeOf(context)?.disableAnimations??false;
    final em=widget.size/5.5;
    return Semantics(
      label:'Caricamento',
      liveRegion:true,
      child: ExcludeSemantics(
        child: SizedBox.square(
          dimension:widget.size,
          child: AnimatedBuilder(
            animation:_animation,
            builder:(_, __) {
              final p=sample(reduced?0:_animation.value);
              return Stack(
                clipBehavior:Clip.none,
                children:[
                  Positioned.fill(child:CustomPaint(painter:_RockTrack(widget.trackColor))),
                  Positioned(
                    left:em*.2,
                    bottom:em*.18,
                    child:Transform.translate(
                      offset:Offset(p.x*em,p.y*em),
                      child:Transform.rotate(
                        angle:p.deg*math.pi/180,
                        child:SizedBox.square(
                          dimension:em,
                          child:DecoratedBox(
                            decoration:BoxDecoration(
                              color:widget.rockColor,
                              borderRadius:BorderRadius.circular(em*.15),
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
              );
            },
          ),
        ),
      ),
    );
  }
  @override
  void dispose() { _animation.dispose(); super.dispose(); }
}

class _RockTrack extends CustomPainter {
  const _RockTrack(this.color);
  final Color color;
  @override
  void paint(Canvas canvas,Size size) {
    canvas.drawLine(
      Offset(size.width*.1,size.height*.91),
      Offset(size.width*.91,size.height*.09),
      Paint()..color=color..strokeWidth=size.width*4/88,
    );
  }
  @override
  bool shouldRepaint(covariant _RockTrack old)=>old.color!=color;
}
