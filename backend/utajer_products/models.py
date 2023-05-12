from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from utajer_accounts.models import User

from helpers.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='category_images', default='category_images/default.jpg')
    icon = models.ImageField(null=True, blank=True, upload_to='category_icons', default='category_icons/default.jpg')

    slug = models.SlugField(default="", null=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'

    def __str__(self):
        return self.name

class ProductImage(BaseModel):
    image = models.ImageField(upload_to='product_images', default='product_images/default.jpg')
    preview_image = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        db_table = 'product_image'

    def __str__(self):
        return self.image.name

class Product(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name="products")
    images = models.ManyToManyField(ProductImage, blank=True, related_name="products")

    slug = models.SlugField(default="", null=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'product'

    @property
    def available(self):
        return self.stock > 0

    @property
    def rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        return sum([review.rating for review in reviews]) / len(reviews)

    def __str__(self):
        return self.name

class ProductReview(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    comment = models.TextField()

    class Meta:
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'
        db_table = 'product_review'

    def __str__(self):
        return self.product.name
