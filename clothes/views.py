from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Clothing
from .serializers import ClothingSerializer
from producer.models import Producer
from .tasks import send_clothing_added_email  # Import the Celery task

class ClothingListView(APIView):
    def get(self, request):
        clothes = Clothing.objects.all()
        serializer = ClothingSerializer(clothes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ClothingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_clothing_added_email.delay(serializer.data['id']) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClothingDetailView(APIView):
    def get_object(self, pk):
        try:
            return Clothing.objects.get(pk=pk)
        except Clothing.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        clothing = self.get_object(pk)
        serializer = ClothingSerializer(clothing)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        clothing = self.get_object(pk)
        serializer = ClothingSerializer(clothing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        clothing = self.get_object(pk)
        clothing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProducerClothingListView(APIView):
    def get(self, request, producer_id):
        producer = get_object_or_404(Producer, pk=producer_id)
        clothes = Clothing.objects.filter(producer=producer)
        serializer = ClothingSerializer(clothes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)