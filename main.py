from fastapi import FastAPI
from sqladmin import Admin, ModelAdmin
from categories import categories_get
from products import products_get
from db import get_session, engine
from categories.admin import CategoryAdmin, RubricAdmin
from products.admin import ProductAdmin, ProductSizeAdmin, ImageProductsAdmin

app = FastAPI()
app.include_router(categories_get.router)
app.include_router(products_get.router)
admin = Admin(app, engine)

admin.add_view(CategoryAdmin)
admin.add_view(RubricAdmin)
admin.add_view(ProductAdmin)
admin.add_view(ProductSizeAdmin)
admin.add_view(ImageProductsAdmin)
