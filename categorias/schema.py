from graphene_django import DjangoObjectType
from .models import Category


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category
        fields = '__all__'
