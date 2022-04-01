from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from fragmentos import views

#	-- URLS PARA VISTAS BASADAS EN CLASES --
urlpatterns = [
    path('', views.FragmentoLista.as_view()),
    path('fragmentos/', views.FragmentoLista.as_view()),
    path('fragmentos/<int:pk>/', views.FragmentoDetalles.as_view()),
    path('usuarios/', views.UserLista.as_view()),
    path('usuarios/<int:pk>/', views.UserDetalles.as_view()),
]

# ------------------------------------------------------------------------------------

'''
#	-- URLS PARA VISTAS BASADAS EN FUNCIONES --
urlpatterns = [
    path('', views.fragmento_lista),
    path('fragmentos/', views.fragmento_lista),
    path('fragmentos/<int:pk>/', views.fragmento_detalles),
]
'''

urlpatterns = format_suffix_patterns(urlpatterns)
