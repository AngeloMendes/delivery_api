from django.conf.urls import url
from . import views
from rest_framework.documentation import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

schema_view = get_schema_view(title="BrejAPP API", description="API Documentation to BrejAPP service", version="1.0.0",
                              renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

app_name = "api-docs"

urlpatterns = [
    url('^$', schema_view, name="docs"),
    url(r'^products/$', views.ProductList.as_view(), name='product-list')
]
