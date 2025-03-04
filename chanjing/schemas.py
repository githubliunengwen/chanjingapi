from pydantic import BaseModel
from typing import List, Optional, Generic, TypeVar

T = TypeVar('T')

class Figure(BaseModel):
    """人物形象数据模型"""
    pic_path: str
    type: str
    cover: str
    width: int
    height: int
    preview_video_url: str

class Person(BaseModel):
    """人物信息数据模型"""
    id: str
    name: str
    figures: List[Figure]
    gender: str
    width: int
    height: int
    audio_name: str
    audio_man_id: str
    audio_preview: str

class PageInfo(BaseModel):
    """分页信息数据模型"""
    page: int
    size: int
    total_count: int
    total_page: int

class ResponseData(BaseModel):
    """响应数据模型"""
    list: List[Person]
    page_info: PageInfo

class APIResponse(BaseModel, Generic[T]):
    """API响应模型"""
    trace_id: str
    code: int
    msg: str
    data: T
