import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const requireFromRenderer = createRequire(import.meta.url);
// The archived TSX sits in a sibling directory, outside renderer/node_modules.
// Resolve third-party imports through THIS isolated runtime. Never modify TSX.
const originalDeps = [
  // React is resolved through Vite's root dedupe, not absolute CJS aliases.
  // Keep one dispatcher shared by source TSX, Radix and Framer Motion.
  'lucide-react', 'react-icons/fa6', 'react-icons/fa', 'clsx', 'tailwind-merge',
  'motion/react', 'framer-motion', 'class-variance-authority',
  // Dependency-licensed runtime imports for pinned original TSX; keep originals immutable.
  'next-themes', '@hugeicons/react', '@hugeicons/core-free-icons',
  '@shikijs/transformers', 'shiki',
].map((name) => ({
  find: new RegExp('^' + name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$'),
  // Motion/Framer must use the ESM import-condition entrypoint.
  // createRequire() selects CJS and can create a second React hook runtime
  // when a TSX lives outside this isolated Vite project.
  replacement: (name === 'framer-motion' || name === 'motion/react')
    ? fileURLToPath(import.meta.resolve(name))
    : requireFromRenderer.resolve(name),
}));

// Historical renderer package manifests are retained in package_history;
// PNG provenance hashes are never rewritten when a new runtime dependency is added.
// Resolve only the exact MIT upstream helper used by archived Amicro sources.
// The original TSX is never changed or silently stubbed.
const pinnedAmicroHook = {
  name: 'source-pinned-amicro-hook',
  enforce: 'pre' as const,
  resolveId(id: string, importer?: string) {
    if (/(?:^|\/)hooks\/useLoopFlg(?:\.[jt]sx?)?$/.test(id) &&
        importer?.replaceAll('\\', '/').includes('/sorgenti/amicro/')) {
      return path.resolve(__dirname, 'vendor/amicro/useLoopFlg.ts');
    }
    return null;
  },
};

export default defineConfig({
  define: {
    __DESIGN_APP_SOURCE_ROOT__: JSON.stringify(path.resolve(__dirname, '../sorgenti')),
  },
  plugins: [pinnedAmicroHook, react(), tailwindcss()],
  resolve: {
    alias: [{ find: '@', replacement: path.resolve(__dirname, 'src') }, ...originalDeps],
    dedupe: ['react', 'react-dom', 'react/jsx-runtime', 'react/jsx-dev-runtime'],
  },
  server: {
    host: '127.0.0.1', port: 5181, strictPort: true,
    // Vite overlay events are shared by the dev server: one bad import must
    // never contaminate another UID's valid screenshot.
    // Disabling only the overlay still broadcast unrelated transform errors
    // to every open page through Vite's websocket. Disable HMR entirely in
    // this one-shot capture harness; each page loads its own exact source.
    hmr: false,
    fs: { allow: ['..'] },
  },
});
