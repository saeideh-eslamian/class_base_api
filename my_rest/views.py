from django.shortcuts import render, HttpResponse
from .models import Articel
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ArticelSerializer
from rest_framework.response import Response
from rest_framework import status

class ArticelAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articels = Articel.objects.all()
        serializers = ArticelSerializer(articels, many=True)
        return Response(serializers.data)


    def post(self, request): 
        serializer = ArticelSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(status =status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class DetailArticelAPIView(APIView):

    def get_object(self, id):
        try:
            return Articel.objects.get(id=id)
        except Articel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    

    def get(self,request, id):
        try:
            articel = Articel.objects.get(id=id)
            serializer = ArticelSerializer(articel)
            return Response(serializer.data) 
        
        except Articel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def put(self, request, id):
         articel = self.get_object(id)
         serializer = ArticelSerializer(articel, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        articel = self.get_object(id)
        articel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
