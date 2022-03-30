from django.urls import path

from fragmentos import views


urlpatterns = [
    path('', views.fragmento_lista),
    path('fragmentos/', views.fragmento_lista),
    path('fragmentos/<int:pk>/', views.fragmento_detalles),
]
