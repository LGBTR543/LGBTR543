export default function SectionHeading({ eyebrow, title, subtitle }) {
  return (
    <header className="mb-6 space-y-2">
      <p className="text-xs uppercase tracking-[0.3em] text-violet/80">{eyebrow}</p>
      <h2 className="text-2xl font-semibold md:text-4xl">{title}</h2>
      {subtitle && <p className="max-w-2xl text-sm text-zinc-400 md:text-base">{subtitle}</p>}
    </header>
  );
}
