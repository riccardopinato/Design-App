// Adapter only for Ruixen's import alias. Original TSX remains unchanged.
export function cn(...values: Array<string | undefined | null | false | Record<string, unknown>>) {
  return values.flatMap(v => {
    if (!v) return [];
    if (typeof v === 'string') return [v];
    return Object.entries(v).filter(([,on])=>Boolean(on)).map(([name])=>name);
  }).join(' ');
}
