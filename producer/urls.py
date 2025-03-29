from django.urls import path
from .views import ProducerListView, ProducerDetailView

urlpatterns = [
    path('producers/', ProducerListView.as_view(), name='producer-list'),
    path('producers/<int:pk>/', ProducerDetailView.as_view(), name='producer-detail'),
]