from datetime import datetime
from sqlmodel import SQLModel, Field, String


class ProductSize(SQLModel, table=True):
    __tablename__ = "product_size"

    id: int = Field(default=None, primary_key=True, index=True)  # autoincrement
    name: str = Field(sa_type=String(100), nullable=False)  # S, M, L, XL
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})


class ProductColor(SQLModel, table=True):
    __tablename__ = "product_color"

    id: int = Field(default=None, primary_key=True, index=True)  # autoincrement
    name: str = Field(sa_type=String(120), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})


class Product(SQLModel, table=True):
    __tablename__ = "product"

    id: int = Field(default=None, primary_key=True, index=True)  # autoincrement
    name: str = Field(sa_type=String(200), nullable=False)
    code: str = Field(sa_type=String(100), nullable=False)
    category: str = Field(sa_type=String(200), nullable=False)
    unit_price: int
    inventory: int
    size_id: int = Field(foreign_key="product_size.id", nullable=False)
    color_id: int = Field(foreign_key="product_color.id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})
