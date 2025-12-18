# JuankoOS™ · plataforma creativa y espiritual

Base mínima para JuankoOS™, inspirada en Juanko Tara y optimizada para crear experiencias simbólicas, contenido y monetización consciente.

## Características
- 🎤 Generadores determinísticos para lyrics, slogans y rituales (`juankoos/content.py`).
- 🔮 Identidad de marca centralizada (paleta, símbolos, tono) en `juankoos/config.py`.
- 🤖 Bridge listo para la API de OpenAI con prompts alineados a la voz de Juanko (`juankoos/openai_bridge.py`).
- 🕸️ Interfaz web FastAPI + Jinja con estilos místicos responsivos (`app.py`, `templates/index.html`, `static/styles.css`).
- 💰 Endpoints para membresías y tienda digital que ayudan a preparar landing pages.

## Cómo correr
1. Crea y activa un entorno virtual.
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. (Opcional) Exporta tu clave:
   ```bash
   export OPENAI_API_KEY="tu_clave"
   ```
4. Levanta el servidor:
   ```bash
   uvicorn app:app --reload --port 8000
   ```
5. Abre http://localhost:8000 para ver la experiencia mística.

## Endpoints útiles
- `POST /api/lyrics` → `{ "theme": "", "mood": "", "language": "es|en" }`
- `POST /api/slogan` → `{ "seed": "" }`
- `POST /api/ritual` → `{ "intention": "", "duration": 11 }`
- `POST /api/membership` → `{ "name": "", "price": "", "benefits": "benef1;benef2" }`
- `POST /api/shop` → `{ "title": "", "format": "PDF", "value": "curso express" }`
- `POST /api/openai` → `{ "task": "describe un lanzamiento", ... }` (requiere `OPENAI_API_KEY`)

## Notas de diseño
- Paleta dorado/negro/púrpura con acentos glow para transmitir misterio.
- Accesibilidad: esquema oscuro declarado y respeto a `prefers-reduced-motion`.
- Texto bilingüe para amplificar alcance y resonancia.
