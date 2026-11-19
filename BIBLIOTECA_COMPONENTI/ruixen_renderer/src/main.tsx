import React from 'react';
import { createRoot } from 'react-dom/client';
import { GrainGradientBg } from '../../sorgenti/ruixen/grain-gradient-bg';
import { GridPattern } from '../../sorgenti/ruixen/grid-pattern';
import { PulsatingButton } from '../../sorgenti/ruixen/pulsating-button';
import { ShimmerButton } from '../../sorgenti/ruixen/shimmer-button';
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
};
const slug = new URLSearchParams(window.location.search).get('component') || '';
const root = document.getElementById('root');
if (!root) throw new Error('Fixture root missing');
if (!(slug in map)) throw new Error('Fixture component not allowlisted: '+slug);
createRoot(root).render(<main id="component-root" data-original-slug={slug}>{map[slug]}</main>);
