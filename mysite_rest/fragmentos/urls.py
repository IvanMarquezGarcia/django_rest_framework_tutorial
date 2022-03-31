from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from fragmentos import views


urlpatterns = [
    path('', views.fragmento_lista),
    path('fragmentos/', views.fragmento_lista),
    path('fragmentos/<int:pk>/', views.fragmento_detalles),
]

urlpatterns = format_suffix_patterns(urlpatterns)
