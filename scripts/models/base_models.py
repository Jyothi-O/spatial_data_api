from typing import List, Optional, Any
from pydantic import BaseModel

class PointModel(BaseModel):
    name: str
    latitude: float
    longitude: float

class PolygonModel(BaseModel):
    name: str
    coordinates: List[List[float]]  

class DefaultResponse(BaseModel):
    message: Optional[str] = None 
    data: Optional[Any] = None

class DefaultFailureResponse(DefaultResponse):
    status: str = "Failed"
    error: Any
