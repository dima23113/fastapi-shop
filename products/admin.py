from sqladmin import ModelAdmin
from .models import Product, ProductSize, ImageProducts


class ProductAdmin(ModelAdmin, model=Product):
    column_list = [Product.id, Product.name, Product.category_id, Product.rubric_id]


class ProductSizeAdmin(ModelAdmin, model=ProductSize):
    column_list = [ProductSize.id, ProductSize.size, ProductSize.product_id]


class ImageProductsAdmin(ModelAdmin, model=ImageProducts):
    column_list = [ImageProducts.id, ImageProducts.name, ImageProducts.mime_type, ImageProducts.product_id]
