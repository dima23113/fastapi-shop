from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db import get_session
from products.models import Category, Rubric, Product

router = APIRouter(
    prefix='/category',
    tags=['categories'],
)


@router.get('/{category}/', response_model=list[Category])
async def get_products_by_category(category: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Category, Product).where(Category.product_category == Product.products_category))
    products = result.scalars().all()
    return [Product(name=product.name) for product in products]


@router.get('/{category}/{rubric}/')
def get_products_by_rubric(category: str, rubric: str):
    return {'message': 'ok'}
