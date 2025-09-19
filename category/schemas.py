from pydantic import BaseModel

class CategoryCreateReq(BaseModel):
    code: str
    name: str

class CategoryUpdateReq(BaseModel):
    name: str

class PaginationReq(BaseModel):
    page: int
    limit: int