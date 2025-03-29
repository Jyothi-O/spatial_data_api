Spatial Data API 🌍
A FastAPI-based backend for storing, updating, and retrieving spatial data (points & polygons) using PostgreSQL + PostGIS.

🚀 Features
✅ Store, update, and retrieve multiple point data
✅ Store, update, and retrieve multiple polygon data
✅ Find points within a polygon
✅ Uses FastAPI for RESTful APIs
✅ PostGIS for spatial queries

📌 Tech Stack
FastAPI (Backend)
PostgreSQL + PostGIS (Database)
SQLAlchemy + GeoAlchemy2 (ORM)
Uvicorn (ASGI Server)

📂 Project Structure
📦 spatial-data-api
│── 📂 scripts
│   ├── 📂 api_details
│   │   ├── api.py  # API Endpoints
│   ├── 📂 handler
│   │   ├── spatial_data_handler.py  # Business Logic
│   ├── 📂 models
│   │   ├── base_models.py  # Pydantic Models
│   ├── 📂 service
│   │   ├── spatial_data_service.py  # API Route Handlers
│   ├── 📂 postgres_db
│   │   ├── db_models.py  # Database Models & Connection
│   │   ├── init_db.py  # Database Initialization
│── main.py  # Application Entry Point
│── requirements.txt  # Dependencies
│── README.md  # Project Documentation

🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone <your-repo-url>
cd spatial-data-api
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set Up PostgreSQL + PostGIS
Install PostgreSQL & PostGIS

Create Database:

CREATE DATABASE databasename;
Enable PostGIS Extension:
\c {your Database}
CREATE EXTENSION postgis;
Update db_models.py with your database credentials.

4️⃣ Run the Application
uvicorn main:app --reload

🔌 API Endpoints
Method	Endpoint	Description
POST	/add_point	Add a point
GET	/get_points	Get all points
POST	/add_polygon	Add a polygon
GET	/get_polygons	Get all polygons
GET	/find_points_in_polygon?polygon_name={name}	Find points inside a polygon


📩 Example API Request
➤ Add a Point
Request (POST /add_point)
{
    "name": "Point A",
    "latitude": 12.9716,
    "longitude": 77.5946
}
Response
{
    "message": "Point added successfully",
    "data": {}
}
