from fastapi import FastAPI, Request
from app.models import PromptRequest, GenerationResponse
from app.generator import generate_image
from app.rate_limiter import check_rate_limit
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Stable Diffusion API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/generate", response_model=GenerationResponse)
async def generate(request: Request, body: PromptRequest):
    ip = request.client.host
    check_rate_limit(ip)

    prompts = [p.strip() for p in body.prompts if len(p.strip()) > 5]
    if not prompts:
        return {"images": []}

    results = []
    for prompt in prompts:
        path = await generate_image(prompt, size=(body.width, body.height))
        results.append(path)

    return {"images": results}
