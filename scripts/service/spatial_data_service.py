from typing import List

from fastapi import APIRouter, HTTPException, Query, Depends
from scripts.api_details.api import Endpoint
from scripts.handler.spatial_data_handler import SpatialDataHandler
from sqlalchemy.orm import Session
from scripts.models.base_models import PointModel, PolygonModel, DefaultResponse, \
    PolygonUpdateModel, PointUpdateModel
from scripts.postgres_db.db_models import get_db

handler_obj = SpatialDataHandler()
spatial_data_obj = APIRouter()


@spatial_data_obj.post(Endpoint.add_points)
def add_points_bulk(points: List[PointModel], db: Session = Depends(get_db)):
    """
    Endpoint to add multiple points in bulk.

    Args:
        points (List[PointModel]): List of points to add.
        db (Session): Database session, injected by FastAPI Depends.

    Returns:
        DefaultResponse: Success message with count of points added.
    """
    try:
        response = handler_obj.add_data_points(points, db)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to add bulk points", "error": str(e)}
        )


@spatial_data_obj.post(Endpoint.update_points)
def update_bulk_points(points: List[PointUpdateModel], db: Session = Depends(get_db)):
    """
    Endpoint to update multiple points in bulk.

    Args:
        points (List[PointUpdateModel]): List of points with update details.
        db (Session): Database session.

    Returns:
        DefaultResponse: Success message with count of points updated.
    """
    try:
        response = handler_obj.update_bulk_points(points, db)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to update points", "error": str(e)}
        )


@spatial_data_obj.get(Endpoint.get_points)
def get_points(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all points from the database.

    Args:
        db (Session): Database session.

    Returns:
        DefaultResponse: List of points with name and location.
    """
    try:
        response = handler_obj.get_data_points(db)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to get data", "error": str(e)}
        )


@spatial_data_obj.post(Endpoint.add_polygons)
def add_polygons(polygons: List[PolygonModel], db: Session = Depends(get_db)):
    """
    Endpoint to add multiple polygons in bulk.

    Args:
        polygons (List[PolygonModel]): List of polygons to add.
        db (Session): Database session.

    Returns:
        DefaultResponse: Success message with count of polygons added.
    """
    try:
        response = handler_obj.add_polygons(polygons, db)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to add bulk polygons", "error": str(e)}
        )


@spatial_data_obj.post(Endpoint.update_polygons)
def update_bulk_polygons(polygons: List[PolygonUpdateModel], db: Session = Depends(get_db)):
    """
    Endpoint to update multiple polygons in bulk.

    Args:
        polygons (List[PolygonUpdateModel]): List of polygon updates.
        db (Session): Database session.

    Returns:
        DefaultResponse: Success message with count of polygons updated.
    """
    try:
        response = handler_obj.update_bulk_polygons(polygons, db)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to update polygons", "error": str(e)}
        )


@spatial_data_obj.get(Endpoint.get_polygons)
def get_polygons(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all polygons from the database.

    Args:
        db (Session): Database session.

    Returns:
        DefaultResponse: List of polygons with name and geometry.
    """
    try:
        response = handler_obj.get_polygons_data(db)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to get polygons data", "error": str(e)}
        )


@spatial_data_obj.get(Endpoint.find_points_in_polygon)
def find_points_in_polygon(
        polygon_name: str = Query(..., description="Name of the polygon to search in"),
        db: Session = Depends(get_db)
):
    """
    Endpoint to find all points contained within a given polygon.

    Args:
        polygon_name (str): Name of the polygon to search within.
        db (Session): Database session.

    Returns:
        DefaultResponse: Polygon name and list of points inside it.
    """
    try:
        response = handler_obj.find_data_points_in_polygon(polygon_name, db)
        return DefaultResponse(data=response)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"message": "Failed to find data in polygon", "error": str(e)}
        )
