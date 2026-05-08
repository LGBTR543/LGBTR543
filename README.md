# ALTO SABOTAJE™ + JuankoOS™ Portal (v1.2)

Premium portal experience built with React + Tailwind. Modular sections, mobile-first layout, and OpenAI-ready creative generation.

## Run locally

```bash
npm install
npm run dev
```

## Production

```bash
npm run build
npm run preview
```

## Architecture

- `src/components/layout/Navbar.jsx` - responsive navigation.
- `src/components/sections/HeroSection.jsx` - portal introduction.
- `src/components/sections/DropsSection.jsx` - limited transmission cards.
- `src/components/sections/RitualsSection.jsx` - activated object cards.
- `src/components/GeneratorLab.jsx` - lyrics/slogans/ritual generation + OpenAI API integration.
- `src/components/layout/Footer.jsx` - branded footer watermark.
- `src/App.jsx` - clean section composition.

## OpenAI

Create `.env`:

```bash
VITE_OPENAI_API_KEY=your_key_here
```

Generator API endpoint: `POST https://api.openai.com/v1/responses`.
