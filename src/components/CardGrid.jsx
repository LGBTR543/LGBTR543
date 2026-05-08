export default function CardGrid({ items, renderItem }) {
  return <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">{items.map(renderItem)}</div>;
}
