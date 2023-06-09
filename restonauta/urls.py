"""restonauta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

from users.api.router import router_user
from categorias.Api.router import router_category
from products.Api.router import ruoter_product
from tables.Api.ruoter import router_table
from orders.Api.router import router_order
from payments.Api.router import router_payment
from weather.views import clima


schema_view = get_schema_view(
    openapi.Info(
        title="RestoNauta - APIDOCS",
        default_version='v1',
        description="Documentación",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="restonauta@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router_user.urls)),
    path('api/', include('users.api.router')),
    path('api/', include(router_category.urls)),
    path('api/', include(ruoter_product.urls)),
    path('api/', include(router_table.urls)),
    path('api/', include(router_order.urls)),
    path('api/', include(router_payment.urls)),
    path('weather-data/', clima, name="clima"),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
