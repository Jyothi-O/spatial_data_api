from sqlalchemy.orm import Session
from sqlalchemy import func
from scripts.postgres_db.db_models import get_db, Point, Polygon

class SpatialDataHandler:
    def __init__(self):
        pass

    def add_data_point(self, point, db: Session):
        try:
            wkt_point = f"POINT({point.longitude} {point.latitude})"
            db_point = Point(name=point.name, location=wkt_point)
            db.add(db_point)
            db.commit()
            return {"message": "Point added successfully"}
        except Exception as e:
            return {"message": f"Failed to add spatial data due to {str(e)}"}

    def get_data_points(self, db: Session):
        try:
            points = db.query(Point).all()
            return [{"name": p.name, "location": p.location} for p in points]
        except Exception as e:
            return {"message": f"Failed to get spatial data due to {str(e)}"}

    def add_polygon_data(self, polygon, db: Session):
        try:
            coords = polygon.coordinates
            if coords[0] != coords[-1]:  # Ensure the polygon closes the loop
                coords.append(coords[0])

            wkt_polygon = f"POLYGON(({', '.join([f'{lng} {lat}' for lat, lng in coords])}))"
            db_polygon = Polygon(name=polygon.name, geometry=wkt_polygon)
            db.add(db_polygon)
            db.commit()
            return {"message": "Polygon added successfully"}
        except Exception as e:
            return {"message": f"Failed to add polygon due to {str(e)}"}

    def get_polygons_data(self, db: Session):
        try:
            polygons = db.query(Polygon).all()
            return [{"name": p.name, "geometry": p.geometry} for p in polygons]
        except Exception as e:
            return {"message": f"Failed to get polygons data due to {str(e)}"}

    def find_data_points_in_polygon(self, polygon_name: str, db: Session):
        try:
            polygon = db.query(Polygon).filter(Polygon.name == polygon_name).first()
            if not polygon:
                raise ValueError("Polygon not found")

            points = db.query(Point).filter(
                func.ST_Within(Point.location, polygon.geometry)
            ).all()

            return {"polygon": polygon_name,
                    "points_inside": [{"name": p.name, "location": p.location} for p in points]}
        except Exception as e:
            return {"message": f"Failed to find polygons data due to {str(e)}"}
