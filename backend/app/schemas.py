from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime


class MemeUpdate(BaseModel):
    caption: Optional[str] = None
    url: Optional[str] = None

    @validator('caption')
    def caption_validation(cls, v, values, **kwargs):
        if (v == "") and ('url' in values and values['url'] == ""):
            raise ValueError("caption and url both must not be null")
        if not type(v) == str:
            raise TypeError("Caption must be a string")
        return v

    @validator('url')
    def url_validation(cls, v, values, **kwargs):
        if (v == "") and ('caption' in values and values['caption'] == ""):
            raise ValueError("caption and url both must not be null")
        if not type(v) == str:
            raise TypeError("URL must be of a string")
        return v


class MemeBase(BaseModel):
    name: str
    caption: str
    url: str


class MemeCreate(MemeBase):

    @validator('name')
    def name_validation(cls, v):
        if v == "":
            raise ValueError("Name must not be null")
        if not type(v) == str:
            raise TypeError("Name must be a string")
        return v

    @validator('caption')
    def caption_validation(cls, v):
        if v == "":
            raise ValueError("Caption must not be null")
        if not type(v) == str:
            raise TypeError("Caption must be a string")
        return v

    @validator('url')
    def url_validation(cls, v):
        if v == "":
            raise ValueError("URL must not be null")
        if not type(v) == str:
            raise TypeError("URL must be of a string")
        return v


class Meme(MemeBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
