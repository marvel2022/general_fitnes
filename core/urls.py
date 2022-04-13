from django.urls import path

from .views import (
    HomeView,
    CategoryView,
    ProductDetailView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('categories/', CategoryView.as_view(), name="category"),
    path('category/<slug:slug>/', CategoryView.as_view(), name="category"),

    path('product-detail/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]