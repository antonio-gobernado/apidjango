from django.http import JsonResponse

from .models import Entrada
from .serializers import EntradaSerializer

from rest_framework.decorators import api_view


from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'POST'])
def entrada_list(request):
    if request.method=='GET':
        entradas=Entrada.objects.all()
        serializer=EntradaSerializer(entradas, many=True)
        return JsonResponse({"entradas": serializer.data})
    if request.method=='POST':
        serializer=EntradaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def entrada_detail(request,id):

    try:
        entrada=Entrada.objects.get(pk=id)

    except Entrada.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=EntradaSerializer(entrada)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=EntradaSerializer(entrada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method== 'DELETE':
        entrada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)