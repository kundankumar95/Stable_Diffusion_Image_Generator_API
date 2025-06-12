from diffusers import StableDiffusionPipeline
import torch
from app.config import MODEL_ID
import uuid
from pathlib import Path

device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
pipe.to(device)

async def generate_image(prompt: str, size: tuple = (512, 512)) -> str:
    image = pipe(prompt, height=size[1], width=size[0]).images[0]
    filename = f"{uuid.uuid4().hex}.png"
    filepath = Path("generated") / filename
    image.save(filepath)
    return str(filepath)
