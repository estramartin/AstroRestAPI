from graphene_django import DjangoObjectType
import graphene
from .models import Table


class TableType(DjangoObjectType):

    class Meta:
        model = Table
        fields = '__all__'

    
class CreateTableMutation(graphene.Mutation):
    table = graphene.Field(TableType)

    class Arguments:        
        number = graphene.Int(required=True)

    def mutate(self, info, number):
        table = Table.objects.create(number=number)
        # Asigna los valores de los campos adicionales del modelo aquí
        # Ejemplo: table.field3 = field3
        table.save()
        return CreateTableMutation(table=table)