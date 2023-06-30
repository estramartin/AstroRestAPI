from rest_framework.serializers import ModelSerializer
from products.models import Product
from categorias.Api.serializers import CategorySerializer


class ProductSerliazer(ModelSerializer):
    category_data = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        fields = ['prod_id', 'title', 'image', 'price',
                  'active', 'category', 'category_data']
