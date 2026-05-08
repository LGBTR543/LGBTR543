import CardGrid from '../CardGrid';
import SectionHeading from '../SectionHeading';
import PortalCard from '../ui/PortalCard';

export default function DropsSection({ drops }) {
  return (
    <section id="drops">
      <SectionHeading eyebrow="Drops / Limited Transmissions" title="Released in fragments. Never repeated." />
      <CardGrid items={drops} renderItem={(drop) => <PortalCard key={drop.title} title={drop.title} subtitle={drop.format} caption={drop.status} />} />
    </section>
  );
}
