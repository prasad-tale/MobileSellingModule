from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.home, name = 'home'),
    path('sell/', views.sellproduct, name = 'sell'),
    path('view/<str:pk_id>/', views.get_post, name = 'view')

]