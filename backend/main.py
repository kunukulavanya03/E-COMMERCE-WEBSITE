from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="This_Document_Outlines_The_Technical_Specifications_For_The_Backend_Api_Of_An_E-Commerce_Website._The_Api_Will_Be_Built_Using_Fastapi_And_Sqlalchemy,_And_It_Will_Serve_As_The_Data_Provider_For_A_React-Based_Frontend._The_Api_Will_Handle_User_Authentication,_Product_Management,_Order_Processing,_And_Other_Core_E-Commerce_Functionalities. API",
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
        "endpoints": 19,
        "models": 9
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "this_document_outlines_the_technical_specifications_for_the_backend_api_of_an_e-commerce_website._the_api_will_be_built_using_fastapi_and_sqlalchemy,_and_it_will_serve_as_the_data_provider_for_a_react-based_frontend._the_api_will_handle_user_authentication,_product_management,_order_processing,_and_other_core_e-commerce_functionalities."}

# Generated API endpoints
@app.post("/api/auth/login")
def api_auth_login(item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Fields(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.post("/api/auth/register")
def api_auth_register(item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Fields(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.post("/api/payment/process")
def api_payment_process(item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Fields(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/api/config/language")
def api_config_language(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.get("/api/config/encoding")
def api_config_encoding(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.get("/api/config/meta")
def api_config_meta(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.get("/api/config/script")
def api_config_script(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.post("/api/auth/logout")
def api_auth_logout(item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Fields(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/api/auth/profile")
def api_auth_profile(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.get("/api/hardcoded-values")
def api_hardcoded-values(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.get("/api/hardcoded-values/:key")
def api_hardcoded-values_:key(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.post("/api/hardcoded-values")
def api_hardcoded-values(item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Fields(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.put("/api/hardcoded-values/:key")
def api_hardcoded-values_:key(id: int, item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Fields).filter(models.Fields.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/api/hardcoded-values/:key")
def api_hardcoded-values_:key(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Fields).filter(models.Fields.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.get("/api/mock-data")
def api_mock-data(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.get("/api/mock-data/:key")
def api_mock-data_:key(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Fields).all()
    return {"items": items, "total": len(items)}

@app.post("/api/mock-data")
def api_mock-data(item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Fields(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.put("/api/mock-data/:key")
def api_mock-data_:key(id: int, item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Fields).filter(models.Fields.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/api/mock-data/:key")
def api_mock-data_:key(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Fields).filter(models.Fields.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
