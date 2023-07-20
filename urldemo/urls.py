from django.urls import path
from . import views


urlpatterns = [
    #.../123/my-article/
    path('<int:article_id>/<slug:slug>/', views.article_detail, name='article_detail'),
    #.../product/abc/123/
    path('<str:product_name>/<int:product_id>/', views.product_detail, name='product_detail')
]
