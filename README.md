
# Spatial Data API - README

This is a **FastAPI-based backend** for storing, updating, and retrieving spatial data (**points** and **polygons**) using **PostgreSQL + PostGIS**.

---

## Features

-->Add, retrieve, and update **points** (latitude, longitude)  
-->Add, retrieve, and update **polygons** (multiple coordinates)  
-->Find points inside a specific polygon

---

## Tech Stack

- **Python (FastAPI)**
- **PostgreSQL with PostGIS**
- **SQLAlchemy + GeoAlchemy2**
- **Uvicorn** (ASGI server)

---

## Project Structure

```
spatial_data_api/
│── conf/
│ └── application.conf                # Configuration file for DB credentials, etc.
│── scripts/
│ ├── api_details/                    # API endpoint details
│ ├── handler/                        # Business logic for handling spatial data
│ ├── models/                         # Pydantic models for request validation
│ ├── postgres_db/                    # Database models and initialization
│ ├── service/                        # FastAPI router (API definitions)
│ ├── logging/                        # Logging configurations
│── main.py                           # FastAPI application entry point
│── requirements.txt                  # Dependencies
│── README.md                         # Project documentation
```

---

## Setup & Installation

### 1.Clone the Repository
```bash
git clone https://github.com/Jyothi-O/spatial_data_api.git
cd spatial_data_api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Database

Ensure **PostgreSQL** and **PostGIS** are installed and enabled.

Update the following values in `conf/application.conf`:
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_PORT`
- `DB_HOST`

---

## Running the API

```bash
python main.py
```

Server runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

| Method | Endpoint                          | Description                       |
|--------|-----------------------------------|-----------------------------------|
| POST   | `/add_points`                     | Add new point(s)                  |
| POST   | `/update_points`                  | Update existing point(s)          |
| GET    | `/get_points`                     | Retrieve all points               |
| POST   | `/add_polygons`                   | Add new polygon(s)                |
| POST   | `/update_polygons`                | Update existing polygon(s)        |
| GET    | `/get_polygons`                   | Retrieve all polygons             |
| GET    | `/find_points_in_polygon`         | Find points inside a polygon      |

---

## Example Requests

### Add Point(s)
**POST** `/add_points`

**Input:**
```json
[
  {
    "name": "Point Inside",
    "latitude": 15.0,
    "longitude": 35.0
  },
  {
    "name": "Point Outside",
    "latitude": 25.0,
    "longitude": 45.0
  }
]
```

**Output:**
```json
{
  "data": {
    "message": "2 points added successfully"
  }
}
```

---

###  Update Point(s)
**POST** `/update_points`

**Input:**
```json
[
  {
    "name": "Point A",
    "new_name": "Updated Point A",
    "latitude": 10.123,
    "longitude": 20.456
  },
  {
    "name": "Point B",
    "latitude": 11.111,
    "longitude": 22.222
  }
]
```

**Output:**
```json
{
  "data": {
    "message": "2 point(s) updated successfully"
  }
}
```

---

### Add Polygon(s)
**POST** `/add_polygons`

**Input:**
```json
[
  {
    "name": "Polygon X",
    "coordinates": [
      [30.0, 10.0],
      [40.0, 40.0],
      [20.0, 40.0],
      [10.0, 20.0],
      [30.0, 10.0]
    ]
  }
]
```

**Output:**
```json
{
  "data": {
    "message": "1 polygon added successfully"
  }
}
```

---

### Update Polygon(s)
**POST** `/update_polygons`

**Input:**
```json
[
  {
    "name": "Polygon X",
    "new_name": "Polygon Updated",
    "coordinates": [
      [35.0, 15.0],
      [45.0, 45.0],
      [25.0, 45.0],
      [15.0, 25.0],
      [35.0, 15.0]
    ]
  }
]
```

**Output:**
```json
{
  "data": {
    "message": "1 polygon updated successfully"
  }
}
```

---

### Get All Points
**GET** `/get_points`

---

### Get All Polygons
**GET** `/get_polygons`

---

### Find Points in a Polygon
**GET** `/find_points_in_polygon?polygon_name=Polygon X`

**Output:**
```json
{
  "data": [
    {
      "name": "Point Inside",
      "latitude": 15.0,
      "longitude": 35.0
    }
  ]
}
```

---

## Notes

- Ensure **PostGIS extension** is enabled in PostgreSQL:
  ```sql
  CREATE EXTENSION postgis;
  ```
- Use **pgAdmin** or `psql` to verify the tables: `points` and `polygons`.
- All coordinates should form a **closed polygon** (first and last coordinate must be the same).
