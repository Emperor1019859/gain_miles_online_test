from uvicorn import run
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select

from orm.db import get_session
from orm.models import Product
from orm.pydantic_models import ProductPayload


app = FastAPI()


@app.get("/")
async def root() -> str:
    return "Hello World"


@app.get("/api/product/{id}")
async def get_product(id: int, session=Depends(get_session)) -> Product | None:
    query = select(Product).where(Product.id == id)
    query_result = await session.exec(query)

    return query_result.first()


@app.get("/api/product")
async def get_products(session=Depends(get_session)) -> list[Product]:
    query = select(Product)
    query_result = await session.exec(query)

    return query_result.all()


@app.delete("/api/product/{id}")
async def delete_product(id: int, session=Depends(get_session)) -> dict:
    query = select(Product).where(Product.id == id)
    query_result = await session.exec(query)
    product_obj = query_result.first()

    if product_obj:
        await session.delete(product_obj)
        await session.commit()

        return {
            "status": "ok",
            "message": f"Product {id = } had been deleted",
        }

    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/api/product")
async def create_product(payload: ProductPayload, session=Depends(get_session)) -> Product:
    product_obj = Product(**payload)
    session.add(product_obj)
    await session.commit()

    return product_obj


if __name__ == "__main__":
    run("main:app", host="localhost", port=8000, reload=True)
