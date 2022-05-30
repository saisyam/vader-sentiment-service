from pydantic import BaseModel, Field

class Input(BaseModel):
    sentence: str = Field(..., title="Sentence")


class Output(BaseModel):
    sentence: str = Field(..., title="Sentence")
    sentiment: str = Field(..., title="Sentiment")