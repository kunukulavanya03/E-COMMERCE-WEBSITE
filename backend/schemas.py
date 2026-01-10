from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class FieldsBase(BaseModel):
    name: str
    description: Optional[str] = None

class FieldsCreate(FieldsBase):
    pass

class FieldsResponse(FieldsBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class Dynamic_Hardcoded_ValuesBase(BaseModel):
    name: str
    description: Optional[str] = None

class Dynamic_Hardcoded_ValuesCreate(Dynamic_Hardcoded_ValuesBase):
    pass

class Dynamic_Hardcoded_ValuesResponse(Dynamic_Hardcoded_ValuesBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class Dynamic_Mock_DataBase(BaseModel):
    name: str
    description: Optional[str] = None

class Dynamic_Mock_DataCreate(Dynamic_Mock_DataBase):
    pass

class Dynamic_Mock_DataResponse(Dynamic_Mock_DataBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class Dynamic_Hardcoded_Values_With_TypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class Dynamic_Hardcoded_Values_With_TypeCreate(Dynamic_Hardcoded_Values_With_TypeBase):
    pass

class Dynamic_Hardcoded_Values_With_TypeResponse(Dynamic_Hardcoded_Values_With_TypeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class Dynamic_Mock_Data_With_TypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class Dynamic_Mock_Data_With_TypeCreate(Dynamic_Mock_Data_With_TypeBase):
    pass

class Dynamic_Mock_Data_With_TypeResponse(Dynamic_Mock_Data_With_TypeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DataBase(BaseModel):
    name: str
    description: Optional[str] = None

class DataCreate(DataBase):
    pass

class DataResponse(DataBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DatabaseBase(BaseModel):
    name: str
    description: Optional[str] = None

class DatabaseCreate(DatabaseBase):
    pass

class DatabaseResponse(DatabaseBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class CreateBase(BaseModel):
    name: str
    description: Optional[str] = None

class CreateCreate(CreateBase):
    pass

class CreateResponse(CreateBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DesignBase(BaseModel):
    name: str
    description: Optional[str] = None

class DesignCreate(DesignBase):
    pass

class DesignResponse(DesignBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

