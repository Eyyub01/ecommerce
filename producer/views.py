from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Producer
from .serializers import ProducerSerializer

class ProducerListView(APIView):
    def get(self, request):
        producers = Producer.objects.all()
        serializer = ProducerSerializer(producers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProducerDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Producer, pk=pk)

    def get(self, request, pk):
        producer = self.get_object(pk)
        serializer = ProducerSerializer(producer)
        return Response(serializer.data)

    def put(self, request, pk):
        producer = self.get_object(pk)
        serializer = ProducerSerializer(producer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        producer = self.get_object(pk)
        producer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)