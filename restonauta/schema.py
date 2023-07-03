import graphene
import graphql_jwt
from products import schema as products_schema
from categorias import schema as categorias_schema
from tables import schema as tables_schema
from products.models import Product
from categorias.models import Category
from tables.models import Table




class Query(graphene.ObjectType):
    all_products = graphene.List(products_schema.ProductType)
    all_categories = graphene.List(categorias_schema.CategoryType)
    all_tables = graphene.List(tables_schema.TableType)

    def resolve_all_tables(root, info):
        return Table.objects.all()

    def resolve_all_categories(root, info):
        return Category.objects.all()
    
    def resolve_all_products(root, info):
        return Product.objects.all()




class Mutation(graphene.ObjectType):
    create_table = tables_schema.CreateTableMutation.Field()
    
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation) 
