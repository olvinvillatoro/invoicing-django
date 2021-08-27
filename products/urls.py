from django.urls import path
from . import views

#URLconfiguration
urlpatterns = [
 
 #   path('route/url', view.function)
    path('api/', views.apiOverview, name="api"),
    path('products/', views.products, name="Products"),
    path('productDetail/<str:id>/', views.productDetail, name="Products detailed data"),
    path('productCreate/', views.productCreate, name="Create a new Product"),
    path('productUpdate/<str:id>/', views.productUpdate, name="Update a Product"),
    path('productDelete/<str:id>/', views.productDelete, name="Delete a Product"),


]