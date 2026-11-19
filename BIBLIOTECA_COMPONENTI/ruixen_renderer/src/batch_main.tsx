import React from 'react';
import { createRoot } from 'react-dom/client';
import { flushSync } from 'react-dom';
import { ThemeProvider } from 'next-themes';
import './style.css';

// Compile ONE requested archived source per page. A broad glob caused Vite to
// transform unrelated files and show their error overlays over valid components.
declare const __DESIGN_APP_SOURCE_ROOT__: string;
const sourceRoots: Record<string, string> = {
  RXN: 'ruixen',
  AMX: 'amicro',
  DBM: 'amicro',
  DSP: 'amicro',
  WML: 'watermelon',
};
const slug = new URLSearchParams(location.search).get('cid') || '';
const target = document.getElementById('component-root');
if (!target) throw new Error('Missing original source renderer root');

function pascal(text: string) {
  return text.replace(/(^|[-_\/])([a-zA-Z])/g, (_,__,char: string)=> char.toUpperCase())
    .replace(/[^a-zA-Z0-9]/g,'');
}
function meaningfulExport(m: Record<string, unknown>, cid: string) {
  const fileId = cid.toLowerCase();
  const name = fileId.startsWith('rxn-') ? fileId.slice(4) : fileId;
  const candidates = [
    pascal(name),
    pascal(name.replace(/^(dbm|amx|dsp)-\d+-?/,'')),
    'default',
  ];
  for (const key of candidates) {
    const c=m[key];
    if (typeof c === 'function' || (c && typeof c==='object' && '$$typeof' in c)) return c;
  }
  for (const [key,exp] of Object.entries(m)) {
    if (key.startsWith('use') || /^(cn|variants|style|schema|metadata)$/i.test(key))continue;
    if (typeof exp === 'function' && /^[A-Z]/.test(key))return exp;
  }
  return null;
}
function BeamSourceFixture({component: Component}:{component: React.ElementType}) {
  const containerRef=React.useRef<HTMLDivElement>(null);
  const fromRef=React.useRef<HTMLDivElement>(null);
  const toRef=React.useRef<HTMLDivElement>(null);
  const dot={width:92,height:92,borderRadius:'50%',border:'2px solid #818cf8',background:'#e0e7ff'};
  return React.createElement('div',{ref:containerRef,
    style:{position:'relative',width:620,height:320,display:'flex',alignItems:'center',justifyContent:'space-around'}},
    React.createElement('div',{ref:fromRef,style:dot}),
    React.createElement('div',{ref:toRef,style:{...dot,background:'#fde68a'}}),
    React.createElement(Component,{containerRef,fromRef,toRef,duration:2,delay:0}));
}

async function mount(cid: string) {
  if (!/^(RXN-[a-z0-9-]+|(?:AMX|DBM|DSP|WML)-[0-9]{3})$/.test(cid)) {
    throw Error('INVALID_CANONICAL_COMPONENT_ID');
  }
  const prefix=cid.split('-')[0];
  const moduleName=cid.startsWith('RXN-')?cid.slice(4):cid.toLowerCase();
  const sourceDir=(prefix==='DSP' && cid==='DSP-001')?'easeui':
    (prefix==='DBM' && cid==='DBM-024')?'watermelon':
    sourceRoots[prefix];
  if (!sourceDir) throw Error('NO_ORIGINAL_SOURCE_PROVIDER '+cid);
  const path=sourceDir+'/'+moduleName+'.tsx';
  const sourceUrl='/@fs'+__DESIGN_APP_SOURCE_ROOT__+'/'+path;
  // This source path must map to the SHA-pinned original verified by Python.
  // Vite does not pre-transform any other repo file.
  const m=await import(/* @vite-ignore */ sourceUrl) as Record<string, unknown>;
  const component = meaningfulExport(m,cid);
  if (!component) throw Error('NO_REACT_COMPONENT_EXPORT; exports='+Object.keys(m).join(','));
  const fixtureProps = {
    className:'relative w-full h-full',
    children:'Design App',
    text:'Design App',
    title:'Design App',
    label:'Continua',
    value:64,
    progress:64,
    size:120,
    duration:2,
    color:'#4f46e5',
    avatarUrls: [],
    numPeople: 3,
    words: ['Design', 'App'],
    texts: ['Design', 'App'],
    defaultValue: new Date('2026-11-19T12:00:00'),
    sound: false,
    items: [
      {id:'1',title:'Design App',description:'Preview component',content:'Design App'},
      {id:'2',title:'Second',description:'UI preview',content:'Other item'},
      {id:'3',title:'Third',description:'UI preview',content:'Third item'},
    ],
  };
  // Fixture props only; never inject, rewrite or transpile alternate TSX code.
  const textComponents = new Set([
    'RXN-animated-gradient-text','RXN-number-ticker','RXN-line-shadow-text',
    'RXN-typing-animation','RXN-comic-text','RXN-animated-shiny-text',
    'RXN-text-reveal','RXN-blur-fade','RXN-linear-mask',
  ]);
  const specialProps = {
    ...fixtureProps,
    className: textComponents.has(cid)
      ? 'relative text-7xl font-semibold text-slate-900'
      : fixtureProps.className,
    // Data is required by the original ArcTimeline API; omitting it caused a
    // source exception, not a defect in the archived component.
    ...(cid==='RXN-arc-timeline'
      ? {arcConfig:{circleWidth:720},data:[
          {time:'2024',steps:[{icon:'●',content:'Progettazione'},{icon:'◆',content:'Ricerca'}]},
          {time:'2025',steps:[{icon:'●',content:'Sviluppo'},{icon:'◆',content:'Test'}]},
          {time:'2026',steps:[{icon:'★',content:'Rilascio'}]},
        ]}
      : {}),
    // The upstream IconCloud paints supplied icons onto its canvas. The
    // 12 small SVG symbols are explicit local fixture inputs, not claimed
    // as official images or reusable assets.
    ...(cid==='RXN-code-comparison'
      ? {beforeCode:'const count = 1;',afterCode:'const count = 2;',
          language:'typescript',filename:'counter.ts',lightTheme:'github-light',darkTheme:'github-dark'}
      : {}),
    ...(cid==='RXN-icon-cloud'
      ? {icons:Array.from({length:12},(_,i)=>
          React.createElement('svg',{xmlns:'http://www.w3.org/2000/svg',width:40,height:40,viewBox:'0 0 40 40'},
            React.createElement('circle',{cx:20,cy:20,r:16,fill:['#6366f1','#10b981','#f59e0b'][i%3]}),
            React.createElement('path',{d:'M12 20h16M20 12v16',stroke:'white',strokeWidth:3})
          )
        )}
      : {}),
    ...(cid==='RXN-animated-subscribe-button'
      ? {children:[
          React.createElement('span',{key:'before'},'Iscriviti'),
          React.createElement('span',{key:'after'},'Iscritto'),
        ]}
      : {}),
    ...(cid==='RXN-scrub-datetime'
      ? {value:new Date('2026-11-19T12:00:00'),sound:false}
      : {}),
  };
  // Compound source APIs need their real children; a generic div or text
  // would not exercise the component they are meant to preview.
  let node: React.ReactNode=React.createElement(component as React.ElementType,specialProps);
  if (cid==='RXN-scroll-based-velocity' &&
      typeof m.ScrollVelocityContainer==='function' &&
      typeof m.ScrollVelocityRow==='function') {
    node=React.createElement(m.ScrollVelocityContainer as React.ElementType,{className:'w-full'},
      React.createElement(m.ScrollVelocityRow as React.ElementType,
        {baseVelocity:2,className:'text-6xl text-slate-900'},'Design App • Componenti'));
  }
  if (cid==='RXN-animated-beam') {
    node=React.createElement(BeamSourceFixture,{component:component as React.ElementType});
  }
  const isSmallLoading=cid.startsWith('DBM-')||cid==='AMX-006';
  const framed=isSmallLoading
    ? React.createElement('div',{style:{transform:'scale(3)',transformOrigin:'center'}},node)
    : node;
  // The ready flag is a render barrier: React 19's normal createRoot.render
  // is asynchronous. Never declare a page ready before its DOM is committed.
  // Some archived components explicitly use next-themes context. Supply
  // the real upstream provider rather than faking useTheme or theme state.
  const themed = ['DSP-001','RXN-code-comparison','RXN-mode-toggle','RXN-script-copy-btn'];
  const preview = themed.includes(cid)
    ? React.createElement(ThemeProvider,{attribute:'class',defaultTheme:'light',enableSystem:false},framed)
    : framed;
  flushSync(()=>createRoot(target).render(preview));
  target.dataset.captureStatus='ready';
  target.dataset.sourcePath=path;
}
mount(slug).catch(e=>{
  target.dataset.captureStatus='failed';
  target.dataset.sourceError=String(e).slice(0,500);
  console.error('ARCHIVED_TSX_BATCH_FAILED',slug,e);
});
