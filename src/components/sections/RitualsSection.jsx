import CardGrid from '../CardGrid';
import SectionHeading from '../SectionHeading';

export default function RitualsSection({ rituals }) {
  return (
    <section id="rituals">
      <SectionHeading eyebrow="Rituals / Activated Objects" title="Objects that trigger symbolic movement." />
      <CardGrid
        items={rituals}
        renderItem={(ritual) => (
          <article key={ritual.title} className="rounded-2xl border border-violet/20 bg-black/70 p-5">
            <h3 className="text-lg font-semibold sm:text-xl">{ritual.title}</h3>
            <p className="mt-3 text-sm text-zinc-400">{ritual.detail}</p>
          </article>
        )}
      />
    </section>
  );
}
