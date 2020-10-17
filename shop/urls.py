from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'shop'
router = DefaultRouter()
router.register(r'Product', views.ProductViewSet)


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    url(r'^api/', include(router.urls))
]
