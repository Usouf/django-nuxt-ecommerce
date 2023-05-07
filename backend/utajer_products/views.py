from rest_framework import viewsets, status, response
from rest_framework.decorators import action

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    @action(methods=['GET'], detail=True, url_path='products', url_name='products')
    def get_products_by_category(self, request, slug):
        category = self.get_object()
        products = category.products
        serializer = ProductSerializer(products, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
