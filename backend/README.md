# This_Document_Outlines_The_Technical_Specifications_For_The_Backend_Api_Of_An_E-Commerce_Website._The_Api_Will_Be_Built_Using_Fastapi_And_Sqlalchemy,_And_It_Will_Serve_As_The_Data_Provider_For_A_React-Based_Frontend._The_Api_Will_Handle_User_Authentication,_Product_Management,_Order_Processing,_And_Other_Core_E-Commerce_Functionalities. API

Generated from Impact Analysis specifications.

## Endpoints

- POST /api/auth/login
- POST /api/auth/register
- POST /api/payment/process
- GET /api/config/language
- GET /api/config/encoding
- GET /api/config/meta
- GET /api/config/script
- POST /api/auth/logout
- GET /api/auth/profile
- GET /api/hardcoded-values
- GET /api/hardcoded-values/:key
- POST /api/hardcoded-values
- PUT /api/hardcoded-values/:key
- DELETE /api/hardcoded-values/:key
- GET /api/mock-data
- GET /api/mock-data/:key
- POST /api/mock-data
- PUT /api/mock-data/:key
- DELETE /api/mock-data/:key

## Models

- Fields
- Dynamic_Hardcoded_Values
- Dynamic_Mock_Data
- Dynamic_Hardcoded_Values_With_Type
- Dynamic_Mock_Data_With_Type
- Data
- Database
- Create
- Design

## Setup

```bash
pip install -r requirements.txt
python main.py
```

API runs on http://localhost:8000
Docs available at http://localhost:8000/docs
