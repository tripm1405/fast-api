from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from category.repository import CategoryRepository
from category.schemas import CategoryCreateReq, CategoryUpdateReq, PaginationReq
from db import get_db

CategoryRouter = APIRouter(prefix='/api/categories')


@CategoryRouter.get("/{id}")
def detail(id: int, db: Session = Depends(get_db)):
    try:
        repo = CategoryRepository(db)

        return repo.detail(id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Category not found")


@CategoryRouter.put("/{id}")
def update(id: str, body: CategoryUpdateReq, db: Session = Depends(get_db)):
    try:
        repo = CategoryRepository(db)

        return repo.update(id, body)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Category not found")


@CategoryRouter.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    try:
        repo = CategoryRepository(db)

        return repo.delete(id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Category not found")


@CategoryRouter.get("")
def list(page: int, limit: int, db: Session = Depends(get_db)):
    repo = CategoryRepository(db)

    return repo.paginate(page=page, limit=limit)


@CategoryRouter.post("")
def create(body: CategoryCreateReq, db: Session = Depends(get_db)):
    repo = CategoryRepository(db)

    return repo.create(body)
