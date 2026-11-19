/** Isolated original-source Next renderer. Never publish as an application. */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const runtimeDirectory = path.dirname(fileURLToPath(import.meta.url));
const nextConfig = {
  reactStrictMode: true,
  experimental: { externalDir: true },
  // The immutable original TSX is in ../sorgenti/ruixen, outside this Next
  // package. Webpack normally walks ancestor node_modules and misses our
  // installed real Motion/React/icons dependencies. Add the *actual* runtime
  // node_modules to the resolver; no source edits, mocks, or font aliases.
  webpack(config) {
    const realModules = path.join(runtimeDirectory, 'node_modules');
    config.resolve.modules = [realModules, ...(config.resolve.modules || [])];
    return config;
  },
};
export default nextConfig;
