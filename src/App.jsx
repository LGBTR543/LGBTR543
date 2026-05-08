import GeneratorLab from './components/GeneratorLab';
import Footer from './components/layout/Footer';
import Navbar from './components/layout/Navbar';
import DropsSection from './components/sections/DropsSection';
import HeroSection from './components/sections/HeroSection';
import RitualsSection from './components/sections/RitualsSection';
import SectionHeading from './components/SectionHeading';
import { archive, drops, navItems, rituals } from './data/content';

export default function App() {
  return (
    <div className="min-h-screen bg-black">
      <Navbar items={navItems} />

      <main className="relative mx-auto max-w-6xl space-y-14 px-4 py-8 sm:space-y-16 sm:py-10 md:space-y-20 md:py-14">
        <div className="noise-overlay pointer-events-none absolute inset-0 -z-10" />

        <HeroSection />
        <DropsSection drops={drops} />
        <RitualsSection rituals={rituals} />

        <section id="archive" className="rounded-2xl border border-zinc-800 bg-zinc-950/50 p-5 sm:p-6">
          <SectionHeading eyebrow="Archive / What No Longer Exists" title="The archive preserves what no longer exists." />
          <ul className="space-y-3 text-sm text-zinc-400">{archive.map((item) => <li key={item}>• {item}</li>)}</ul>
        </section>

        <section id="editorial" className="grid gap-5 md:grid-cols-2 md:gap-6">
          <SectionHeading eyebrow="Signal / Editorial Transmissions" title="Not content. Transmission." subtitle="Encrypted dispatches on AI art, sound, and symbolic creator strategy." />
          <form className="rounded-2xl border border-zinc-800 bg-zinc-950/70 p-5">
            <label htmlFor="email" className="mb-2 block text-sm">Receive encrypted updates</label>
            <input id="email" type="email" placeholder="you@frequency.com" className="w-full rounded-lg border border-zinc-700 bg-black px-4 py-3 text-sm outline-none ring-violet focus:ring" />
            <button className="mt-4 w-full rounded-lg bg-violet px-4 py-3 text-sm font-semibold text-black">Join Signal List</button>
          </form>
        </section>

        <GeneratorLab />

        <section id="manifesto" className="rounded-2xl border border-violet/30 bg-gradient-to-b from-violet/10 to-black p-5 sm:p-6">
          <SectionHeading eyebrow="Manifesto / The Core Code" title="We turn sabotage into sacred design." />
          <p className="max-w-3xl text-sm leading-7 text-zinc-300 md:text-base">JuankoOS™ guides conscious artists through lyrics, symbols, and strategy. The mission: build emotional impact, spiritual clarity, and monetizable transmissions.</p>
        </section>
      </main>

      <Footer />
    </div>
  );
}
