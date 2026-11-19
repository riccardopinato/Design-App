import React from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

// Lazy import each exact original TSX separately. No component can break another
// fixture's compilation. All sources remain untouched and source-pinned.
const views: Record<string, () => Promise<React.ReactNode>> = {
  'grain-gradient-bg': () => import('../../sorgenti/ruixen/grain-gradient-bg')
    .then(m => <m.GrainGradientBg className="h-full w-full"/>),
  'grid-pattern': () => import('../../sorgenti/ruixen/grid-pattern')
    .then(m => <div className="h-full w-full relative overflow-hidden bg-white rounded-xl">
      <m.GridPattern squares={[[0,0],[2,1],[5,3],[8,4],[12,6],[14,0]]} />
    </div>),
  'pulsating-button': () => import('../../sorgenti/ruixen/pulsating-button')
    .then(m => <div className="w-full h-full flex items-center justify-center"><m.PulsatingButton>Continua</m.PulsatingButton></div>),
  'shimmer-button': () => import('../../sorgenti/ruixen/shimmer-button')
    .then(m => <div className="w-full h-full flex items-center justify-center"><m.ShimmerButton>Scopri di più</m.ShimmerButton></div>),
  'interactive-hover-button': () => import('../../sorgenti/ruixen/interactive-hover-button')
    .then(m => <div className="w-full h-full flex justify-center items-center"><m.InteractiveHoverButton>Continua</m.InteractiveHoverButton></div>),
  'flip-text': () => import('../../sorgenti/ruixen/flip-text')
    .then(m => <div className="w-full h-full flex justify-center items-center text-4xl font-semibold text-slate-900"><m.FlipText duration={0.35} delayMultiple={0.035}>Design App</m.FlipText></div>),
  'orbiting-circles': () => import('../../sorgenti/ruixen/orbiting-circles')
    .then(m => <div className="w-full h-full flex justify-center items-center relative text-lg font-bold">
      <m.OrbitingCircles radius={100} duration={12} iconSize={42}>
        <div className="w-10 h-10 rounded-full bg-indigo-500 text-white grid place-items-center">A</div>
        <div className="w-10 h-10 rounded-full bg-pink-500 text-white grid place-items-center">B</div>
        <div className="w-10 h-10 rounded-full bg-emerald-500 text-white grid place-items-center">C</div>
      </m.OrbitingCircles>
    </div>),
  'rainbow-button': () => import('../../sorgenti/ruixen/rainbow-button')
    .then(m => <div className="w-full h-full flex justify-center items-center"><m.RainbowButton size="lg">Esplora</m.RainbowButton></div>),
  'ruixen-featured-message-card': () => import('../../sorgenti/ruixen/ruixen-featured-message-card')
    .then(m => <div className="w-full h-full flex justify-center items-center"><m.default /></div>),
  'spinning-text': () => import('../../sorgenti/ruixen/spinning-text')
    .then(m => <div className="w-full h-full flex justify-center items-center relative">
      <m.SpinningText className="absolute left-1/2 top-1/2 text-lg font-semibold text-slate-900" radius={11}>DESIGN APP •</m.SpinningText>
    </div>),
};
const slug = new URLSearchParams(window.location.search).get('component') || '';
const root = document.getElementById('root');
const fixture = views[slug];
if (!root || !fixture) throw new Error('Unregistered original source fixture: '+slug);
fixture()
  .then(view => createRoot(root).render(<main id="component-root" data-original-slug={slug}>{view}</main>))
  .catch(err => {
    console.error('PINNED_ORIGINAL_TSX_FIXTURE_ERROR', slug, String(err));
    root.textContent = 'SOURCE_MODULE_FAILED: '+slug+' '+String(err);
  });
