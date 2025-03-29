from fastapi import APIRouter, HTTPException, Query
from scripts.api_details.api import Endpoint
from scripts.handler.spatial_data_handler import SpatialDataHandler
from scripts.models.base_models import PointModel, PolygonModel, DefaultFailureResponse, DefaultResponse

handler_obj = SpatialDataHandler()
spatial_data_obj = APIRouter()

@spatial_data_obj.post(Endpoint.add_point)
def add_point(point: PointModel):
    try:
        response = handler_obj.add_data_point(point)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to add data", "error": str(e)}
        )

@spatial_data_obj.get(Endpoint.get_points)
def get_points():
    try:
        response = handler_obj.get_data_points()
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to get data", "error": str(e)}
        )

@spatial_data_obj.post(Endpoint.add_polygon)
def add_polygon(polygon: PolygonModel):
    try:
        response = handler_obj.add_polygon_data(polygon)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to add polygon data", "error": str(e)}
        )

@spatial_data_obj.get(Endpoint.get_polygons)
def get_polygons():
    try:
        response = handler_obj.get_polygons_data()
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to get polygons data", "error": str(e)}
        )

@spatial_data_obj.get(Endpoint.find_points_in_polygon)
def find_points_in_polygon(
    polygon_name: str = Query(..., description="Name of the polygon to search in")
):
    try:
        response = handler_obj.find_data_points_in_polygon(polygon_name)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to find data in polygon", "error": str(e)}
        )
