from uvicorn import run
from fastapi import FastAPI, Depends
from sqlmodel import select

from orm.db import get_session
from orm.models import Product


app = FastAPI()


@app.get("/")
async def root() -> str:
    return "Hello World"


@app.get("/api/product/{id}")
async def get_product(id: int, session=Depends(get_session)) -> Product | None:
    query = select(Product).where(Product.id == id)
    query_result = await session.exec(query)

    return query_result.first()


if __name__ == "__main__":
    run("main:app", host="localhost", port=8000, reload=True)
