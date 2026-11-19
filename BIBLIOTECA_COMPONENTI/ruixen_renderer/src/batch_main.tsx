import React from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

const modules = import.meta.glob('../../sorgenti/**/*.tsx');
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
  const variants = [
    '../../sorgenti/ruixen/'+cid.slice(4)+'.tsx',
    '../../sorgenti/amicro/'+cid.toLowerCase()+'.tsx',
    '../../sorgenti/watermelon/'+cid.toLowerCase()+'.tsx',
    '../../sorgenti/easeui/'+cid.toLowerCase()+'.tsx',
  ];
  const path=variants.find(v=>modules[v]);
  if (!path) throw Error('NO_ARCHIVED_MODULE_FOR_UID '+cid);
  const m=await modules[path]() as Record<string, unknown>;
  const component = meaningfulExport(m,cid);
  if (!component) throw Error('NO_REACT_COMPONENT_EXPORT; exports='+Object.keys(m).join(','));
  const fixtureProps = {
    className:'relative w-full h-full',
    children:React.createElement('span', {className:'font-semibold'}, 'Design App'),
    text:'Design App',
    title:'Design App',
    label:'Continua',
    value:64,
    progress:64,
    size:120,
    duration:2,
    color:'#4f46e5',
    items: [
      {id:'1',title:'Design App',description:'Preview component',content:'Design App'},
      {id:'2',title:'Second',description:'UI preview',content:'Other item'},
      {id:'3',title:'Third',description:'UI preview',content:'Third item'},
    ],
  };
  // Fixture props only; never inject, rewrite or transpile alternate TSX code.
  const node=React.createElement(component as React.ElementType,fixtureProps);
  createRoot(target).render(node);
  target.dataset.captureStatus='ready';
  target.dataset.sourcePath=path;
}
mount(slug).catch(e=>{
  target.dataset.captureStatus='failed';
  target.dataset.sourceError=String(e).slice(0,500);
  console.error('ARCHIVED_TSX_BATCH_FAILED',slug,e);
});
