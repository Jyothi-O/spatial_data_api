from typing import List, Optional, Any
from pydantic import BaseModel


class PointModel(BaseModel):
    name: str
    latitude: float
    longitude: float


class PolygonUpdateModel(BaseModel):
    name: str
    new_name: Optional[str] = None
    coordinates: Optional[List[List[float]]] = None


class PointUpdateModel(BaseModel):
    name: str
    new_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class PolygonModel(BaseModel):
    name: str
    coordinates: List[List[float]]


class DefaultResponse(BaseModel):
    data: Optional[Any] = None


class DefaultFailureResponse(DefaultResponse):
    status: str = "Failed"
    error: Any
