import React from 'react';
import { createRoot } from 'react-dom/client';
import { GrainGradientBg } from '../../sorgenti/ruixen/grain-gradient-bg';
import { GridPattern } from '../../sorgenti/ruixen/grid-pattern';
import { PulsatingButton } from '../../sorgenti/ruixen/pulsating-button';
import { ShimmerButton } from '../../sorgenti/ruixen/shimmer-button';
import { InteractiveHoverButton } from '../../sorgenti/ruixen/interactive-hover-button';
import { FlipText } from '../../sorgenti/ruixen/flip-text';
import { OrbitingCircles } from '../../sorgenti/ruixen/orbiting-circles';
import { RainbowButton } from '../../sorgenti/ruixen/rainbow-button';
import RuixenFeaturedMessageCard from '../../sorgenti/ruixen/ruixen-featured-message-card';
import { SpinningText } from '../../sorgenti/ruixen/spinning-text';
import './style.css';

// The four components above are imported straight from the pinned MIT TSX originals.
// Only the demo fixture is ours: it does NOT replace or rewrite the component.
const map: Record<string, React.ReactNode> = {
  'grain-gradient-bg': <GrainGradientBg className="h-full w-full"/>,
  'grid-pattern': <div className="h-full w-full relative overflow-hidden bg-white rounded-xl">
    <GridPattern squares={[[0,0],[2,1],[5,3],[8,4],[12,6],[14,0]]} />
  </div>,
  'pulsating-button': <div className="w-full h-full flex items-center justify-center">
    <PulsatingButton>Continua</PulsatingButton>
  </div>,
  'shimmer-button': <div className="w-full h-full flex items-center justify-center">
    <ShimmerButton>Scopri di più</ShimmerButton>
  </div>,
  'interactive-hover-button': <div className="w-full h-full flex justify-center items-center">
    <InteractiveHoverButton>Continua</InteractiveHoverButton>
  </div>,
  'flip-text': <div className="w-full h-full flex justify-center items-center text-4xl font-semibold text-slate-900">
    <FlipText duration={0.35} delayMultiple={0.035}>Design App</FlipText>
  </div>,
  'orbiting-circles': <div className="w-full h-full flex justify-center items-center relative text-lg font-bold">
    <OrbitingCircles radius={100} duration={12} iconSize={42}>
      <div className="w-10 h-10 rounded-full bg-indigo-500 text-white grid place-items-center">A</div>
      <div className="w-10 h-10 rounded-full bg-pink-500 text-white grid place-items-center">B</div>
      <div className="w-10 h-10 rounded-full bg-emerald-500 text-white grid place-items-center">C</div>
    </OrbitingCircles>
  </div>,
  'rainbow-button': <div className="w-full h-full flex justify-center items-center">
    <RainbowButton size="lg">Esplora</RainbowButton>
  </div>,
  'ruixen-featured-message-card': <div className="w-full h-full flex justify-center items-center">
    <RuixenFeaturedMessageCard />
  </div>,
  'spinning-text': <div className="w-full h-full flex justify-center items-center relative">
    <SpinningText className="absolute left-1/2 top-1/2 text-lg font-semibold text-slate-900" radius={11}>
      DESIGN APP •
    </SpinningText>
  </div>,
};
const slug = new URLSearchParams(window.location.search).get('component') || '';
const root = document.getElementById('root');
if (!root) throw new Error('Fixture root missing');
if (!(slug in map)) throw new Error('Fixture component not allowlisted: '+slug);
createRoot(root).render(<main id="component-root" data-original-slug={slug}>{map[slug]}</main>);
