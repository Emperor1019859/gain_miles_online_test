"""insert_default_products

Revision ID: 0412bb788ab2
Revises: 4d87711f60e1
Create Date: 2024-09-04 19:53:44.059775

"""

from typing import Sequence, Union
from alembic import op
from sqlmodel import Session, select
from itertools import product as iter_product

from orm.db import sync_engine
from orm.models import Product, ProductColor, ProductSize


# revision identifiers, used by Alembic.
revision: str = "0412bb788ab2"
down_revision: Union[str, None] = "4d87711f60e1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

ALLOWED_COLORS = ["Red", "Blue", "Green", "White", "Black"]
ALLOWED_SIZES = ["S", "M", "L"]
PRODUCTS = {
    "Star": {
        "code": "A-001",
        "category": "cloth",
        "unit_price": 200,
        "inventory": 20,
        "sizes": ["S", "M"],
        "colors": ["Red", "Blue"],
    },
    "Moon": {
        "code": "A-002",
        "category": "cloth",
        "unit_price": 300,
        "inventory": 10,
        "sizes": ["M", "L"],
        "colors": ["Red", "White"],
    },
    "Eagle": {
        "code": "B-001",
        "category": "pants",
        "unit_price": 100,
        "inventory": 23,
        "sizes": ["M", "L"],
        "colors": ["Green"],
    },
    "Bird": {
        "code": "B-002",
        "category": "pants",
        "unit_price": 50,
        "inventory": 12,
        "sizes": ["S", "M", "L"],
        "colors": ["Black"],
    },
}


def upgrade() -> None:
    with Session(sync_engine) as session:
        for color in ALLOWED_COLORS:
            session.add(ProductColor(name=color))
            session.flush()

        for size in ALLOWED_SIZES:
            session.add(ProductSize(name=size))
            session.flush()

        for name, info in PRODUCTS.items():
            for size, color in iter_product(info["sizes"], info["colors"]):
                # get size id
                size_query = select(ProductSize.id).where(ProductSize.name == size)
                size_id = session.exec(size_query).first()

                # get color id
                color_query = select(ProductColor.id).where(ProductColor.name == color)
                color_id = session.exec(color_query).first()

                product = Product(
                    name=name,
                    code=info["code"],
                    size_id=size_id,
                    color_id=color_id,
                    category=info["category"],
                    unit_price=info["unit_price"],
                    inventory=info["inventory"],
                )
                session.add(product)

        session.commit()


def downgrade() -> None:
    op.execute("DELETE FROM product")
    op.execute("DELETE FROM product_color")
    op.execute("DELETE FROM product_size")
