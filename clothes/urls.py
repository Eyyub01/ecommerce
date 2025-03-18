from django.urls import path
from .views import *

urlpatterns = [
    path('clothes/', ClothingListView.as_view(), name='clothes_list'),
    path('clothes/<int:pk>/', ClothingDetailView.as_view(), name='clothes_detail_view' ),
    path('producers/<int:producer_id>/clothes/', ProducerClothingListView.as_view(), name='producer-clothing-list')
]