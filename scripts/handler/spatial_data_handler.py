from scripts.logging.log_module import logger as log
from typing import List, Optional
from sqlalchemy import func
from geoalchemy2 import WKTElement
from geoalchemy2.shape import to_shape
from shapely.geometry import mapping

from scripts.models.base_models import PointModel, PolygonModel, PointUpdateModel, PolygonUpdateModel
from scripts.postgres_db.db_models import Point, Polygon


class SpatialDataHandler:
    def __init__(self):
        """Initialize the SpatialDataHandler class."""
        log.info("SpatialDataHandler initialized")

    def add_data_points(self, points: List[PointModel], db):
        """Add multiple points to the database."""
        try:
            log.info(f"Adding {len(points)} points to the database")
            db_points = []
            for point in points:
                wkt_point = WKTElement(f"POINT({point.longitude} {point.latitude})", srid=4326)
                db_points.append(Point(name=point.name, location=wkt_point))
            db.bulk_save_objects(db_points)
            db.commit()
            log.info(f"Successfully added {len(db_points)} points")
            return {"message": f"{len(db_points)} points added successfully"}
        except Exception as e:
            db.rollback()
            log.error(f"Failed to add data points due to: {str(e)}")
            return {"message": f"Failed to add data points due to {str(e)}"}

    def update_bulk_points(self, updates: List[PointUpdateModel], db):
        """Update multiple points in the database in bulk."""
        try:
            log.info(f"Updating {len(updates)} points in bulk")
            updated = 0
            for point in updates:
                existing = db.query(Point).filter(Point.name == point.name).first()
                if existing:
                    if point.new_name:
                        existing.name = point.new_name
                    if point.latitude is not None and point.longitude is not None:
                        existing.location = WKTElement(f"POINT({point.longitude} {point.latitude})", srid=4326)
                    updated += 1
            db.commit()
            log.info(f"Successfully updated {updated} points")
            return {"message": f"{updated} point(s) updated successfully"}
        except Exception as e:
            db.rollback()
            log.error(f"Failed to update points due to: {str(e)}")
            return {"message": f"Failed to update points due to {str(e)}"}

    def get_data_points(self, db):
        """Retrieve all points from the database."""
        try:
            log.info("Fetching all points from database")
            points = db.query(Point).all()
            result = [
                {
                    "name": p.name,
                    "location": mapping(to_shape(p.location))
                }
                for p in points
            ]
            log.info(f"Retrieved {len(result)} points")
            return result
        except Exception as e:
            log.error(f"Failed to get spatial data due to: {str(e)}")
            return {"message": f"Failed to get spatial data due to {str(e)}"}

    def add_polygons(self, polygons: List[PolygonModel], db):
        """Add multiple polygons to the database."""
        try:
            log.info(f"Adding {len(polygons)} polygons to the database")
            db_polygons = []
            for polygon in polygons:
                coords = polygon.coordinates.copy()
                if coords[0] != coords[-1]:
                    coords.append(coords[0])
                # Correct order is longitude latitude for WKT
                wkt_polygon_str = f"POLYGON(({', '.join([f'{lng} {lat}' for lat, lng in coords])}))"
                wkt_polygon = WKTElement(wkt_polygon_str, srid=4326)
                db_polygons.append(Polygon(name=polygon.name, geometry=wkt_polygon))
            db.bulk_save_objects(db_polygons)
            db.commit()
            log.info(f"Successfully added {len(db_polygons)} polygons")
            return {"message": f"{len(db_polygons)} polygons added successfully"}
        except Exception as e:
            db.rollback()
            log.error(f"Failed to add polygons due to: {str(e)}")
            return {"message": f"Failed to add polygons due to {str(e)}"}

    def update_bulk_polygons(self, updates: List[PolygonUpdateModel], db):
        """Update multiple polygons in the database in bulk."""
        try:
            log.info(f"Updating {len(updates)} polygons in bulk")
            updated = 0
            for polygon in updates:
                existing = db.query(Polygon).filter(Polygon.name == polygon.name).first()
                if existing:
                    if polygon.new_name:
                        existing.name = polygon.new_name
                    if polygon.coordinates:
                        coords = polygon.coordinates.copy()
                        if coords[0] != coords[-1]:
                            coords.append(coords[0])
                        wkt_polygon_str = f"POLYGON(({', '.join([f'{lng} {lat}' for lat, lng in coords])}))"
                        existing.geometry = WKTElement(wkt_polygon_str, srid=4326)
                    updated += 1
            db.commit()
            log.info(f"Successfully updated {updated} polygons")
            return {"message": f"{updated} polygon(s) updated successfully"}
        except Exception as e:
            db.rollback()
            log.error(f"Failed to update polygons due to: {str(e)}")
            return {"message": f"Failed to update polygons due to {str(e)}"}

    def get_polygons_data(self, db):
        """Retrieve all polygons from the database."""
        try:
            log.info("Fetching all polygons from database")
            polygons = db.query(Polygon).all()
            result = [
                {
                    "name": p.name,
                    "geometry": mapping(to_shape(p.geometry))
                }
                for p in polygons
            ]
            log.info(f"Retrieved {len(result)} polygons")
            return result
        except Exception as e:
            log.error(f"Failed to get polygons data due to: {str(e)}")
            return {"message": f"Failed to get polygons data due to {str(e)}"}

    def find_data_points_in_polygon(self, polygon_name: str, db):
        """Find all points that lie within a specified polygon."""
        try:
            log.info(f"Finding points inside polygon: {polygon_name}")
            polygon = db.query(Polygon).filter(Polygon.name == polygon_name).first()
            if not polygon:
                log.error(f"Polygon '{polygon_name}' not found")
                raise ValueError("Polygon not found")
            points = db.query(Point).filter(
                func.ST_Contains(polygon.geometry, Point.location)
            ).all()

            points_inside = [
                {
                    "name": p.name,
                    "location": mapping(to_shape(p.location))
                }
                for p in points
            ]
            log.info(f"Found {len(points_inside)} points inside polygon '{polygon_name}'")
            return {
                "polygon": polygon_name,
                "points_inside": points_inside
            }
        except Exception as e:
            log.error(f"Failed to find polygons data due to: {str(e)}")
            return {
                "message": f"Failed to find polygons data due to {str(e)}"
            }
