from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        exclude = ('created', 'modified', 'deleted_at', 'is_deleted')
        lookup_field = 'slug'

class ProductSerializer(serializers.ModelSerializer):
    available = serializers.BooleanField(read_only=True)
    rating = serializers.FloatField(min_value=0, max_value=5, read_only=True)

    class Meta:
        model = models.Product
        exclude = ('created', 'modified', 'deleted_at', 'is_deleted')
        lookup_field = 'slug'
        depth = 1
