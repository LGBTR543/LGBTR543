# ALTO SABOTAJE™ + JuankoOS™ Portal (v1.3)

Premium portal experience built with React + Tailwind. Modular sections, mobile-first layout, and OpenAI-ready creative generation.

## Quick start (important)

Run commands **inside the project folder** (where `package.json` exists):

```bash
cd /workspace/LGBTR543
npm install
npm run dev
```

If you run `npm install` from `~` (home), you'll get `ENOENT` because no `package.json` is there.

## Production

```bash
cd /workspace/LGBTR543
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

## Troubleshooting

- `ENOENT ... /home/<user>/package.json`: you are in the wrong directory. `cd` into the repo root first.
- `403 Forbidden` when installing: your environment is blocking npm registry access; retry from a network/environment with npm access.
