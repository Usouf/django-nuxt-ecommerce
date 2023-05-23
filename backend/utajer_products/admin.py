from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name', 'created', 'modified']
    list_editable = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.ProductImage)
class ProductImageAdmin(ImportExportModelAdmin):
    list_display = ['id', 'image', 'created', 'modified']
    list_filter = ['id', 'created', 'modified']

@admin.register(models.Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'slug', 'price', 'available', 'created', 'modified']
    list_filter = ['name', 'created', 'modified']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.ProductReview)
class ProductReviewAdmin(ImportExportModelAdmin):
    list_display = ['id', 'product', 'rating', 'created', 'modified']
    list_filter = ['product', 'rating', 'created', 'modified']
    list_editable = ['rating']
