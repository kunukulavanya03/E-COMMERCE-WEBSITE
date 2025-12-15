# The_Backend_Api_For_The_E-Commerce-Website_Is_Designed_To_Handle_All_Business_Logic_And_Data_Operations_For_An_E-Commerce_Platform._It_Will_Be_Built_Using_Fastapi,_A_Modern,_Fast_(High-Performance),_Web_Framework_For_Building_Apis_With_Python_3.7+_Based_On_Standard_Python_Type_Hints._Sqlalchemy_Will_Be_Used_As_The_Orm_To_Interact_With_The_Database. Backend API

Complete FastAPI backend with authentication, database models, and API endpoints.

## Features

- FastAPI framework with automatic OpenAPI documentation
- JWT authentication with user registration/login
- SQLAlchemy ORM with database models
- Pydantic schemas for request/response validation
- CORS middleware for frontend integration
- Comprehensive error handling
- Database migrations with Alembic

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Run the application:
```bash
python main.py
```

Or with uvicorn:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- POST `/auth/register` - Register new user
- POST `/auth/login` - Login user

### Core Endpoints
- GET `/api/items` - Get all items
- POST `/api/items` - Create new item
- PUT `/api/items/<built-in function id>` - Update item
- DELETE `/api/items/<built-in function id>` - Delete item

## Database

The application uses SQLite by default. To use PostgreSQL:

1. Install PostgreSQL
2. Update DATABASE_URL in .env:
```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Testing

Run tests with:
```bash
pytest
```
