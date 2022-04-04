from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from fragmentos import views

#	-- URLS PARA VISTAS BASADAS EN CLASES --
urlpatterns = [
    path('', views.api_root),

    path('fragmentos/',
         views.FragmentoLista.as_view(),
         name = 'fragmentos_lista'),

    path('fragmentos/<int:pk>/',
         views.FragmentoDetalles.as_view(),
         name = 'fragmentos_detalles'),

    path('fragmentos/<int:pk>/highlight/',
         views.FragmentoHighlight.as_view(),
         name = 'fragmentos_detalles_highlight'),

    path('usuarios/',
         views.UserLista.as_view(),
         name = 'usuarios_lista'),

    path('usuarios/<int:pk>/',
         views.UserDetalles.as_view(),
         name = 'usuarios_detalles'),
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
