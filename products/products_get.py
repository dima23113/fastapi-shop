from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db import get_session

from .models import Category, Rubric, Product

router = APIRouter(
    prefix='/product',
    tags=['products']
)


@router.get('/{product}/')
def get_product(product: str):
    return {'message': 'ok'}
