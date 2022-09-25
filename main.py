from fastapi import FastAPI
from sqladmin import Admin, ModelAdmin
from categories import categories_get
from products import products_get
from db import get_session, engine
from categories.admin import CategoryAdmin, RubricAdmin

app = FastAPI()
app.include_router(categories_get.router)
app.include_router(products_get.router)
admin = Admin(app, engine)

admin.add_view(CategoryAdmin)
admin.add_view(RubricAdmin)
