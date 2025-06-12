from pydantic import BaseModel, Field
from typing import List, Optional

class PromptRequest(BaseModel):
    prompts: List[str]
    width: Optional[int] = 512
    height: Optional[int] = 512

class GenerationResponse(BaseModel):
    images: List[str]
