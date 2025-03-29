📌 Spatial Data API - README
This is a FastAPI-based backend for storing, updating, and retrieving spatial data (points and polygons) using PostgreSQL + PostGIS.

🚀 Features
✅ Add, retrieve, and store points (latitude, longitude).
✅ Add, retrieve, and store polygons (multiple coordinates).
✅ Find points inside a polygon.

🛠️ Tech Stack
Python (FastAPI)
PostgreSQL with PostGIS
SQLAlchemy + GeoAlchemy2
Uvicorn (ASGI server)

📂 Project Structure
spatial_data_api/
│── scripts/
│   ├── api_details/       # API endpoint details  
│   ├── handler/           # Business logic for handling spatial data  
│   ├── models/            # Pydantic models for request validation  
│   ├── postgres_db/       # Database models and initialization  
│   ├── service/           # FastAPI router (API definitions)  
│── main.py                # FastAPI application entry point  
│── requirements.txt       # Dependencies  
│── README.md              # Project documentation 

🛠️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/Jyothi-O/spatial_data_api.git
cd spatial_data_api
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Configure Database
Ensure PostgreSQL and PostGIS are installed.

Update DB_NAME, DB_USER, DB_PASSWORD, and DB_HOST in scripts/postgres_db/db_models.py.

🚀 Running the API
python main.py

The server will start at: http://127.0.0.1:8000

📌 API Endpoints
Method	Endpoint	Description
POST	/add_point	Add a new point
GET	/get_points	Get all points
POST	/add_polygon	Add a polygon
GET	/get_polygons	Get all polygons
GET	/find_points_in_polygon?polygon_name=name	Find points inside a polygon


📄 Example Requests
📍 Add a Point
POST /add_point
{
  "name": "Point A",
  "latitude": 12.9716,
  "longitude": 77.5946
}
🟦 Add a Polygon
POST /add_polygon
{
  "name": "Polygon X",
  "coordinates": [[12.96, 77.58], [12.98, 77.60], [12.99, 77.61], [12.96, 77.58]]
}
🔍 Find Points in a Polygon
GET /find_points_in_polygon?polygon_name=Polygon X

📌 Notes
Ensure PostGIS extension is enabled in PostgreSQL.
Use pgAdmin or psql to verify tables (points and polygons).

