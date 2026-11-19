import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import path from 'node:path';
import { createRequire } from 'node:module';

const requireFromRenderer = createRequire(import.meta.url);
// The archived TSX sits in a sibling directory, outside renderer/node_modules.
// Resolve third-party imports through THIS isolated runtime. Never modify TSX.
const originalDeps = [
  'react', 'react-dom', 'react/jsx-runtime', 'lucide-react',
  'motion/react', 'framer-motion', 'class-variance-authority',
].map((name) => ({
  find: new RegExp('^' + name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$'),
  replacement: requireFromRenderer.resolve(name),
}));

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: [{ find: '@', replacement: path.resolve(__dirname, 'src') }, ...originalDeps],
    dedupe: ['react', 'react-dom'],
  },
  server: {
    host: '127.0.0.1', port: 5181, strictPort: true, hmr: false,
    fs: { allow: ['..'] },
  },
});
