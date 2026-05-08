export default function PortalCard({ title, subtitle, caption }) {
  return (
    <article className="rounded-2xl border border-zinc-800 bg-zinc-950/70 p-5">
      <p className="text-xs uppercase tracking-[0.22em] text-zinc-500">{subtitle}</p>
      <h3 className="mt-2 text-lg font-semibold sm:text-xl">{title}</h3>
      <p className="mt-3 text-sm text-violet">{caption}</p>
    </article>
  );
}
