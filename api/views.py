from django.shortcuts import render
from reservas.models import Reservas
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, mixins
from .serializers import ReservasSerializer
from rest_framework.decorators import api_view

# Create your views here.

class ReservaViewset(viewsets.ModelViewSet):
    serializer_class = ReservasSerializer
    queryset = Reservas.objects.all()
    print("estoy en api")
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class ReservaDetailsViewset(viewsets.ModelViewSet):
    serializer_class = ReservasSerializer
    queryset = Reservas.objects.all()
    
    def get(self,request, pk):
        return self.list(request,pk)
    
    def put(self,request, pk):
        return self.update(request,pk)
    
    def delete(self,request, pk):
        return self.destroy(request, pk)
    
    
    
    

""" @api_view(['GET','POST'])
def reservas_list(request):
    
    if request.method == "GET":
        reservas = Reservas.objects.all()
        serializer = ReservasSerializer(reservas, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ReservasSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reservas_details(request, pk):
    try:
        reserva = Reservas.objects.get(pk=pk)
    except Reservas.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = ReservasSerializer(reserva, many=True)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = ReservasSerializer(reserva = request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
 """