from pydantic import BaseModel, Field


class NewsRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=10,
        max_length=5000,
        description="Tigrigna news text",
    )
