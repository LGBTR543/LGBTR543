from pathlib import Path
from typing import Dict

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from juankoos import (
    BRAND_PALETTE,
    BRAND_SYMBOLS,
    JUANKO_TONE,
    JuankoOpenAI,
    craft_membership_tier,
    create_shop_item,
    design_ritual,
    generate_lyrics,
    generate_slogan,
)

app = FastAPI(title="JuankoOS™", version="0.1.0", description="Creative spiritual OS")

base_path = Path(__file__).parent
app.mount("/static", StaticFiles(directory=base_path / "static"), name="static")
templates = Jinja2Templates(directory=str(base_path / "templates"))


def build_context() -> Dict[str, str]:
    return {
        "palette": BRAND_PALETTE,
        "symbols": BRAND_SYMBOLS,
        "tone": JUANKO_TONE,
    }


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    context = {"request": request, **build_context()}
    return templates.TemplateResponse("index.html", context)


@app.post("/api/lyrics")
async def lyrics(payload: Dict[str, str]):
    theme = payload.get("theme")
    mood = payload.get("mood")
    if not theme or not mood:
        raise HTTPException(status_code=422, detail="theme and mood are required")
    return {"result": generate_lyrics(theme, mood, payload.get("language", "es"))}


@app.post("/api/slogan")
async def slogan(payload: Dict[str, str]):
    seed = payload.get("seed")
    if not seed:
        raise HTTPException(status_code=422, detail="seed is required")
    return {"result": generate_slogan(seed)}


@app.post("/api/ritual")
async def ritual(payload: Dict[str, str]):
    intention = payload.get("intention")
    if not intention:
        raise HTTPException(status_code=422, detail="intention is required")
    duration = int(payload.get("duration", 11))
    return {"result": design_ritual(intention, duration)}


@app.post("/api/membership")
async def membership(payload: Dict[str, str]):
    name = payload.get("name")
    price = payload.get("price")
    benefits_raw = payload.get("benefits", "")
    if not name or not price:
        raise HTTPException(status_code=422, detail="name and price are required")
    benefits = [b.strip() for b in benefits_raw.split(";") if b.strip()]
    return {"result": craft_membership_tier(name, benefits, price)}


@app.post("/api/shop")
async def shop(payload: Dict[str, str]):
    title = payload.get("title")
    format_hint = payload.get("format")
    value = payload.get("value")
    if not title or not format_hint or not value:
        raise HTTPException(status_code=422, detail="title, format, and value are required")
    return {"result": create_shop_item(title, format_hint, value)}


@app.post("/api/openai")
async def openai_generate(payload: Dict[str, str]):
    task = payload.get("task")
    if not task:
        raise HTTPException(status_code=422, detail="task is required")
    generator = JuankoOpenAI(model=payload.get("model", "gpt-4o-mini"))
    result = generator.generate(task, payload)
    return {"result": result}
