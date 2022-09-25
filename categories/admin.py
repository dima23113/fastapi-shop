from sqladmin import ModelAdmin
from products.models import Category, Rubric


class CategoryAdmin(ModelAdmin, model=Category):
    column_list = [Category.id, Category.name, Category.rubrics]


class RubricAdmin(ModelAdmin, model=Rubric):
    column_list = [Rubric.id, Rubric.name, Rubric.category_id]
