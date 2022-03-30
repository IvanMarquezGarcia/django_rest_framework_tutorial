from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from fragmentos.models import Fragmento

from fragmentos.serializers import SerializadorFragmento

# Create your views here.

@csrf_exempt
def fragmento_lista(request):
    # lista todos los fragmentos o crea uno nuevo
    if request.method == 'GET':
        fragmentos = Fragmento.objects.all()
        serializador = SerializadorFragmento(fragmentos, many = True)
        return JsonResponse(serializador.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializador = SerializadorFragmento(data = data)
        if serializador.is_valid():
            serializador.save()
            return JsonResponse(serializador.data, status = 201)
        return JsonResponse(serializador.errors, status = 400)

@csrf_exempt
def fragmento_detalles(request, pk):
    # Muestra, actualiza o elimina un fragmento
    try:
        fragmento = Fragmento.objects.get(pk = pk)
    except Fragmento.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializador = SerializadorFragmento(fragmento)
        return JsonResponse(serializador.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializador = SerializadorFragmento(fragmento, data = data)
        if serializador.is_valid():
            serializador.save()
            return JsonResponse(serializador.data)
        return JsonResponse(serializador.errors, status = 400)

    elif request.method == 'DELETE':
        fragmento.delete()
        return HttpResponse(status=204)
