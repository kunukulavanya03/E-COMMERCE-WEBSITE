from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="This_Project_Outlines_The_Backend_Api_Specification_For_An_E-Commerce_Website._The_Backend_Will_Be_Built_Using_Fastapi_And_Sqlalchemy,_Providing_A_Restful_Api_For_The_React-Based_Frontend._The_Api_Will_Handle_User_Authentication,_Product_Management,_Cart_Operations,_Order_Processing,_And_Other_Essential_E-Commerce_Functionalities. API",
    description="Generated from Impact Analysis specifications",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "API is running",
        "endpoints": 1,
        "models": 7
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "this_project_outlines_the_backend_api_specification_for_an_e-commerce_website._the_backend_will_be_built_using_fastapi_and_sqlalchemy,_providing_a_restful_api_for_the_react-based_frontend._the_api_will_handle_user_authentication,_product_management,_cart_operations,_order_processing,_and_other_essential_e-commerce_functionalities."}

# Generated API endpoints
@app.put("/30")
def 30(id: int, item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Fields).filter(models.Fields.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
