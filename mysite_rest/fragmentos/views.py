from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User

from rest_framework import status, mixins, generics, permissions, renderers, viewsets

from rest_framework.decorators import api_view, action

from rest_framework.response import Response

from rest_framework.parsers import JSONParser

from rest_framework.views import APIView

from rest_framework.reverse import reverse

from fragmentos.models import Fragmento

from fragmentos.serializers import SerializadorFragmento, SerializadorUser

from fragmentos.permissions import IsOwnerOrReadOnly

# Create your views here.

#	-- VISTA PARA PORTAL DE INICIO (no usar en conjunto a la clase Router) --
'''
@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'usarios': reverse('usuarios_lista', request = request, format = format),
        'fragmentos': reverse('fragmentos_lista', request = request, format = format),
    })
'''
#	-- VISTAS VIEWSET --
# vista que automaticamente provee las acciones de un crud
# es posible añadir la accion para mostrar el highlight
class FragmentoViewSet(viewsets.ModelViewSet):
    queryset = Fragmento.objects.all()
    serializer_class = SerializadorFragmento
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail = True, renderer_classes = [renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        fragmento = self.get_object()
        return Response(fragmento.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

# vista que automaticamente provee las acciones de listar y ver detalles
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = SerializadorUser

# ---------------------------------------------------------------------------------------------
'''
#	-- VISTAS BASADAS EN CLASES GENÉRICAS USANDO MIXIN CLASSES --
# vista que lista todos los fragmentos o crea uno nuevo
class FragmentoLista(generics.ListCreateAPIView):
    # zona pruebas
    model = Fragmento
    lookup_field = 'id'
    # fin zona pruebas

    queryset = Fragmento.objects.all()
    serializer_class = SerializadorFragmento
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

# vista que muestra, actualiza o elimina un fragmento
class FragmentoDetalles(generics.RetrieveUpdateDestroyAPIView):
    # zona de pruebas
    model = Fragmento
#    lookup_field = 'id'
    # fin zona pruebas

    queryset = Fragmento.objects.all()
    serializer_class = SerializadorFragmento
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# vista para mostrar el html formateado del fragmento
class FragmentoHighlight(generics.GenericAPIView):
    queryset = Fragmento.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]
    model = Fragmento
    serializer_class = SerializadorFragmento

    def get(self, request, *args, **kwargs):
        fragmento = self.get_object()
        return Response(fragmento.highlighted)

# vista que lista todos los usuarios
class UserLista(generics.ListAPIView):
    # zona de pruebas
    model = User
    # fin zona de pruebas

    queryset = User.objects.all()
    serializer_class = SerializadorUser

class UserDetalles(generics.RetrieveAPIView):
    # zona de pruebas
    model = User
    # fin zona de pruebas

    queryset = User.objects.all()
    serializer_class = SerializadorUser

# --------------------------------------------------------------------------------------


#	-- VISTAS BASADAS EN CLASES USANDO MIXIN CLASSES --
# vista que lista todos los fragmentos o crea uno nuevo
class FragmentoLista(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):

    queryset = Fragmento.objects.all()
    serializer_class = SerializadorFragmento

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# vista que muestra, actualiza o elimina un fragmento
class FragmentoDetalles(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

    queryset = Fragmento.objects.all()
    serializer_class = SerializadorFragmento

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# --------------------------------------------------------------------------------------------------------

#	-- VISTAS BASADAS EN CLASES --
# vista que lista todos los fragmentos o crea uno nuevo
class FragmentoLista(APIView):
    def get(self, request, format = None):
        fragmentos = Fragmento.objects.all()
        serializador = SerializadorFragmento(fragmentos, many = True)
        return Response(serializador.data)

    def post(self, request, format = None):
        serializador = SerializadorFragmento(data = request.data)
        if serializador.is_valid():
            serializador.save()
            serializador.save()
            return Respons(serializador.data, status = status.HTTP_201_CREATED)
        return Response(serializador.errors, status = status.HTTP_400_BAD_REQUEST)

# vista que muestra, actualiza o elimina un fragmento
class FragmentoDetalles(APIView):
    def get_object(self, pk):
        try:
            return Fragmento.objects.get(pk = pk)
        except Fragmento.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        fragmento = self.get_object(pk)
        print("--------- pk " + str(pk) + " - code " + str(fragmento.code) + " ------")
        serializador = SerializadorFragmento(fragmento)
        return Response(serializador.data)

    def put(self, request, pk, format = None):
        fragmento = self.get_object(pk)
        serializador = SerializadorFragmento(fragmento, data = request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        fragmento = self.get_object(pk)
        fragmento.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------

#	-- VISTAS BASADAS EN FUNCIONES --
# funcionalidad de api_view para indicar una lista de métodos http que la vista debe responder
@api_view(['GET', 'POST'])
# evitar el uso de CSRF tokens para esta vista
#@csrf_exempt
def fragmento_lista(request, format = None):
    # lista todos los fragmentos o crea uno nuevo
    if request.method == 'GET':
        fragmentos = Fragmento.objects.all()
        serializador = SerializadorFragmento(fragmentos, many = True)
        return Response(serializador.data)

    elif request.method == 'POST':
        serializador = SerializadorFragmento(data = request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status = status.HTTP_201_CREATED)
        return Response(serializador.errors, status = status.HTTP_400_BAD_REQUEST)

# funcionalidad de api_view para indicar una lista de métodos http que la vista debe responder
@api_view(['GET', 'PUT', 'DELETE'])
# evitar el uso de CSRF tokens para esta vista
#@csrf_exempt#@csrf_exempt # evitar el uso de CSRF tokens para esta vista
def fragmento_detalles(request, pk, format = None):
    # Muestra, actualiza o elimina un fragmento
    try:
        fragmento = Fragmento.objects.get(pk = pk)
    except Fragmento.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = SerializadorFragmento(fragmento)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = SerializadorFragmento(fragmento, data = request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fragmento.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
'''
