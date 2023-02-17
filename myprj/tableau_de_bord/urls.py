from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tableau_de_bord-index'),
    path('staff/', views.staff, name='tableau_de_bord-staff'),
    path('product/', views.product, name='tableau_de_bord-product'),
    path('order/', views.order, name='tableau_de_bord-order'),
]