from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework.parsers import JSONParser

from rest_framework.views import APIView

from fragmentos.models import Fragmento

from fragmentos.serializers import SerializadorFragmento

# Create your views here.

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
'''
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
