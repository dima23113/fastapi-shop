from fastapi import APIRouter

router = APIRouter(
    prefix='/product',
    tags=['products']
)


@router.get('/{product}/')
def get_product(product: str):
    return {'message': 'ok'}
