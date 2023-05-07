from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name', 'created', 'modified']
    list_editable = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'created', 'modified']
    list_filter = ['id', 'created', 'modified']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'price', 'available', 'created', 'modified']
    list_filter = ['name', 'created', 'modified']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'rating', 'created', 'modified']
    list_filter = ['product', 'rating', 'created', 'modified']
