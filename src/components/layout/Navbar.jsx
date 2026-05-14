import { useState } from 'react';

export default function Navbar({ items }) {
  const [open, setOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-40 border-b border-zinc-800 bg-black/90 backdrop-blur">
      <div className="mx-auto flex h-14 max-w-6xl items-center justify-between px-4">
        <a href="#signal" className="text-xs font-bold tracking-[0.3em] text-violet">ALTO SABOTAJE™</a>
        <button aria-expanded={open} aria-label="Toggle menu" onClick={() => setOpen((v) => !v)} className="text-sm text-zinc-300 md:hidden">Menu</button>
        <ul className="hidden items-center gap-5 text-sm md:flex">
          {items.map((item) => (
            <li key={item.id}><a href={`#${item.id}`} className="text-zinc-300 transition hover:text-violet">{item.label}</a></li>
          ))}
        </ul>
      </div>
      {open && (
        <ul className="space-y-3 border-t border-zinc-800 px-4 py-4 md:hidden">
          {items.map((item) => (
            <li key={item.id}><a href={`#${item.id}`} className="block text-sm text-zinc-300" onClick={() => setOpen(false)}>{item.label}</a></li>
          ))}
        </ul>
      )}
    </nav>
  );
}
