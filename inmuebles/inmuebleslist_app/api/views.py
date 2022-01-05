from rest_framework.response import Response
from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer
from rest_framework.decorators import api_view

#se decora con la api view de rest
@api_view(['GET','POST'])
#mostrar todos los inmuebles
def inmueble_list(request):
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
       de_serializer = InmuebleSerializer(data=request.data)
       if de_serializer.is_valid():
           de_serializer.save()
           return Response(de_serializer.data)
       else:
           
           return Response(de_serializer.errors)

#mostrar una busqueda
@api_view(['GET','PUT','DELETE'])
def inmueble_detalle(request, id_inmueble):
    if request.method == 'GET':
        inmueble = Inmueble.objects.get(pk=id_inmueble)
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        inmueble = Inmueble.objects.get(pk=id_inmueble)
        de_serializer = InmuebleSerializer(inmueble,data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors)
    
    if request.method == 'DELETE':
        inmueble = Inmueble.objects.get(pk=id_inmueble)
        inmueble.delete()
        data = {
            "resultado": True
        }
        return Response()