from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ..shop import views


urlpatterns = [
    path(r'^$', views.product_list, name='product_list'),
    path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
