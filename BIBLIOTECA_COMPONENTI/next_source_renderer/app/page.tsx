"use client";
// Import the archived, Git-blob-pinned original TSX as-is. The Next runtime
// resolves next/font/google via its real loader; no stub and no rewritten UI.
import GlowingSendInput from '../../sorgenti/ruixen/glowing-send-input';
export default function Page() {
  return <main><div id="component-root" data-source="RXN-glowing-send-input">
    <GlowingSendInput placeholder="Type your message..." className="max-w-md" />
  </div></main>;
}
