from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from category.model import Category
from category.schemas import CategoryCreateReq, CategoryUpdateReq


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def detail(self, id: int):
        model = self.db.get(Category, id)
        if model is None:
            raise NoResultFound()

        return

    def list(self):
        return self.db.query(Category).all()

    def create(self, dto: CategoryCreateReq):
        model = Category(code=dto.code, name=dto.name)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model.id

    def update(self, id: str, dto: CategoryUpdateReq):
        model = self.db.get(Category, id)
        if model is None:
            raise NoResultFound()

        model.name = dto.name

        self.db.commit()
        self.db.refresh(model)
        return model

    def delete(self, id: int):
        model = self.db.get(Category, id)
        if model is None:
            raise NoResultFound()

        self.db.delete(model)
        self.db.commit()

    def paginate(self, page: int, limit: int):
        page = 1 if page < 1 else page
        limit = 5 if limit < 5 else limit

        items = self.db.query(Category).offset((page - 1) * limit).limit(limit).all()
        total = self.db.query(Category).count()
        return (items, total)
