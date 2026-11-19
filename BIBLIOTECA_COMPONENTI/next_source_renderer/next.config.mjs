/** Isolated original-source Next renderer. Never publish as an application. */
const nextConfig = {
  reactStrictMode: true,
  // The archived, blob-verified upstream TSX lives in the sibling sources tree.
  experimental: { externalDir: true },
};
export default nextConfig;
