from typing import List, Optional
from pydantic import condecimal
from sqlmodel import SQLModel, Field, Relationship


class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, description='id категории')
    name: str = Field(description='Название категории')
    rubrics: List['Rubric'] = Relationship(back_populates='category')
    product_category: List['Product'] = Relationship(back_populates='products_category')


class Rubric(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, description='id рубрики')
    name: str = Field(description='Название рубрики')
    category_id: Optional[int] = Field(default=None, foreign_key='category.id')
    category: Optional[Category] = Relationship(back_populates='rubrics')
    product_rubric: List['Product'] = Relationship(back_populates='products_rubric')


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, description='id товара', title='id товара')
    name: str = Field(title='Название')
    description: str = Field(title='Описание')
    price: condecimal(max_digits=10, decimal_places=2) = Field(default=0)
    images: List['ImageProducts'] = Relationship(back_populates='product_images')
    available: bool = Field(title='В наличии')
    article: str = Field(title='Артикль')
    sale: bool = Field(title='Индикатор наличия скидки')
    sizes: List['ProductSize'] = Relationship(back_populates='product_sizes')
    category_id: Optional[int] = Field(default=None, foreign_key='category.id')
    products_category: Optional[Category] = Relationship(back_populates='product_category')
    rubric_id: Optional[int] = Field(default=None, foreign_key='rubric.id')
    products_rubric: Optional[Rubric] = Relationship(back_populates='product_rubric')


class ImageProducts(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, description='id изображения', title='id изображения')
    file_id: int = Field(title='id файла')
    name: str = Field(title='Название')
    tag: str = Field(title='Тэг')
    size: str = Field(title='Размер изображения')
    mime_type: str = Field(title='mime type изображения')
    modification_time: str = Field(title='Время изменения')
    product_id: Optional[int] = Field(default=None, foreign_key='product.id', title='Связь с товаром')
    product_images: Optional[Product] = Relationship(back_populates='images')


class ProductSize(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, description='id размера', title='id размера')
    size: str = Field(title='Размер')
    qty: int = Field(title='Количество')
    product_id: Optional[int] = Field(default=None, title='связь с товаром', foreign_key='product.id')
    product_sizes: Optional[Product] = Relationship(back_populates='sizes')
