from slugify import slugify
from sqlalchemy import ForeignKey, String, Column, Boolean, Date, Integer, Text, Float, DateTime

from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    first_name = Column(String(120), nullable=True)
    second_name = Column(String(120), nullable=True)
    zip_code = Column(String(20), nullable=True)
    email_mailing = Column(Boolean, default=False)
    phone = Column(String(120), nullable=True)
    birthday = Column(Date, nullable=True)
    address = Column(String(120), nullable=True)
    city = Column(String(120), nullable=True)
    country = Column(String(120), nullable=True)
    amount_of_purchases = Column(Integer, default=0)

    def __repr__(self) -> str:
        return f'User id: {self.id}, email: {self.email}'

    def get_full_name(self):
        return f'{self.first_name} {self.second_name}'


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(55), nullable=False)
    slug = Column(String(55), unique=True)
    subcategories = relationship('Subcategory', backref='category')
    products = relationship('Product', backref='category_products')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Category id: {self.id}, category_name: {self.name}'


class Subcategory(Base):
    __tablename__ = 'subcategory'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(55), nullable=False)
    slug = Column(String(55), unique=True)
    category_slug = Column(String(55), ForeignKey('category.slug'))
    subcategories_type = relationship('Subcategory_type', backref='subcategorytype')
    products = relationship('Product', backref='subcategory_products')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Subcategory id: {self.id}, subcategory_name: {self.name}'


class Subcategory_type(Base):
    __tablename__ = 'subcategory_type'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(55), nullable=False)
    slug = Column(String(55), unique=True)
    subcategory_slug = Column(String(55), ForeignKey('subcategory.slug'))
    products = relationship('Product', backref='subcategory_type_products')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Subcategory_type id: {self.id}, subcategory_type_name: {self.name}'


class Brand(Base):
    __tablename__ = 'brand'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    slug = Column(String(256), unique=True)
    description = Column(Text)
    products = relationship('Product', backref='brand_products')
    img = Column(Text, unique=True, nullable=True)
    name_img = Column(Text, nullable=True)
    mimetype = Column(Text, nullable=True)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Brand id: {self.id}, brand_name: {self.name}'


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    category_slug = Column(String(256), ForeignKey('category.slug'))
    subcategory_slug = Column(String(256), ForeignKey('subcategory.slug'))
    subcategory_type_slug = Column(String(256), ForeignKey('subcategory_type.slug'))
    brand_slug = Column(String(256), ForeignKey('brand.slug'))
    name = Column(String(256))
    slug = Column(String(256))
    description = Column(Text)
    specifications = Column(Text)
    price = Column(Float(decimal_return_scale=2))
    available = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.utcnow())
    article = Column(String(256))
    img = Column(Text, unique=True, nullable=True, )
    name_img = Column(Text, nullable=True)
    mimetype = Column(Text, nullable=True)
    price_discount = Column(Float(decimal_return_scale=2))
    product_images = relationship('ImageProduct', backref='image_products')
    product_sizes = relationship('ProductSize', backref='prouduct_sizes')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        if not 'price_discount' in kwargs:
            kwargs['price_discount'] = self.price
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Product id: {self.id}, product_name: {self.name}'


class ImageProduct(Base):
    __tablename__ = 'image_product'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    img = Column(Text, unique=True, nullable=True)
    name = Column(Text, nullable=True)
    mimetype = Column(Text, nullable=True)
    product = Column(Integer, ForeignKey('product.id'))

    def __repr__(self) -> str:
        return f'Image id: {self.id}, : {self.name}'


class ProductSize(Base):
    __tablename__ = 'prouduct_size'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=True)
    qty = Column(Integer, nullable=True)
    product = Column(Integer, ForeignKey('product.id'))
