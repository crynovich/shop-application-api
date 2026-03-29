from pydantic import BaseModel


class Feature(BaseModel):
    id: int
    name: str
