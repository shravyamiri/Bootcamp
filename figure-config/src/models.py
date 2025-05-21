from pydantic import BaseModel
from typing import List, Optional

class Entity(BaseModel):
    text: str
    type: str

class FigureCaption(BaseModel):
    figure_id: str
    caption: str
    url: Optional[str]
    entities: List[Entity]

class Paper(BaseModel):
    pmcid: str
    pmid: Optional[str]
    title: str
    abstract: str
    captions: List[FigureCaption]