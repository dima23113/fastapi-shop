from fastapi import APIRouter

router = APIRouter(
    prefix='/category',
    tags=['categories'],
)


@router.get('/{category}/')
def get_products_by_category(category: str):
    return {'message': 'ok'}


@router.get('/{category}/{rubric}/')
def get_products_by_rubric(category: str, rubric: str):
    return {'message': 'ok'}
