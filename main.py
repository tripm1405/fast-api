from fastapi import FastAPI

from category.api import CategoryRouter

app = FastAPI()

app.include_router(CategoryRouter)
