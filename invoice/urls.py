from django.urls import path
from . import views

#URLconfiguration
urlpatterns = [
 
 #   path('route/url', view.function)
    path('hello/', views.say_hello, name="hola") ,
    path('print/', views.show_response, name="home"),
    path('products/', views.show_products, name="products")

]