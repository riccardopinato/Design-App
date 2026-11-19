import React from 'react';
import { createRoot } from 'react-dom/client';
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
  const specialProps = {
    ...fixtureProps,
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
  const node=React.createElement(component as React.ElementType,specialProps);
  const isSmallLoading=cid.startsWith('DBM-')||cid==='AMX-006';
  const framed=isSmallLoading
    ? React.createElement('div',{style:{transform:'scale(3)',transformOrigin:'center'}},node)
    : node;
  createRoot(target).render(framed);
  target.dataset.captureStatus='ready';
  target.dataset.sourcePath=path;
}
mount(slug).catch(e=>{
  target.dataset.captureStatus='failed';
  target.dataset.sourceError=String(e).slice(0,500);
  console.error('ARCHIVED_TSX_BATCH_FAILED',slug,e);
});
