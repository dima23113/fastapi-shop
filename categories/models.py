from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, description='id категории')
    name: str = Field(description='Название категории')
    rubrics: List['Rubric'] = Relationship(back_populates='category')


class Rubric(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, description='id рубрики')
    name: str = Field(description='Название рубрики')
    category_id: Optional[int] = Field(default=None, foreign_key='category.id')
    category: Optional[Category] = Relationship(back_populates='rubrics')
