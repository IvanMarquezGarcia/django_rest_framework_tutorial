from django.urls import path, include

from rest_framework import renderers

from rest_framework.routers import DefaultRouter

from rest_framework.urlpatterns import format_suffix_patterns

from fragmentos import views

#	-- URLS USANDO CLASE Router --
router = DefaultRouter()
router.register(r'fragmentos', views.FragmentoViewSet, basename = "fragmentos")
router.register(r'usuarios', views.UserViewSet, basename = "usuarios")

urlpatterns = [
    path('', include(router.urls)),
]

# -------------------------------------------------------------------------------------------
'''
#	-- URLS PARA VISTAS BASADAS EN CLASES VIEWSETS --
fragmentos_lista = views.FragmentoViewSet.as_view({'get': 'list',
                                             'post': 'create'
})

fragmentos_detalles = views.FragmentoViewSet.as_view({'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update',
                                                'delete': 'destroy'
})

fragmentos_detalles_highlight = views.FragmentoViewSet.as_view({'get': 'highlight',
}, renderer_classes = [renderers.StaticHTMLRenderer])

usuarios_lista = views.UserViewSet.as_view({'get': 'list',
})

usuarios_detalles = views.UserViewSet.as_view({'get': 'retrieve',
})


urlpatterns = [
    path('', views.api_root),

    path('fragmentos/',
         fragmentos_lista,
         name = 'fragmentos_lista'),

    path('fragmentos/<int:pk>/',
         fragmentos_detalles,
         name = 'fragmentos_detalles'),

    path('fragmentos/<int:pk>/highlight/',
         fragmentos_detalles_highlight,
         name = 'fragmentos_detalles_highlight'),

    path('usuarios/',
         usuarios_lista,
         name = 'usuarios_lista'),

    path('usuarios/<int:pk>/',
         usuarios_detalles,
         name = 'usuarios_detalles'),
]

# ------------------------------------------------------------------------------------

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


#	-- URLS PARA VISTAS BASADAS EN FUNCIONES --
urlpatterns = [
    path('', views.fragmento_lista),
    path('fragmentos/', views.fragmento_lista),
    path('fragmentos/<int:pk>/', views.fragmento_detalles),
]
'''

# no usar en conjunto a la clase Router
#urlpatterns = format_suffix_patterns(urlpatterns)
