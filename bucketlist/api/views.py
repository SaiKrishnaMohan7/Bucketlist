from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import BucketListSerializer
from .models import BucketList

# ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
class BucketListCreateView(ListCreateAPIView):
  """View responsible for creating bucketlist items"""

  queryset = BucketList.objects.all()
  serializer_class = BucketListSerializer

  def create_bucketlist_item(self, serializer):
    """Save POST data"""
    serializer.save()

# RetrieveUpdateDestroyAPIView is a generic view that provides GET(one), PUT, PATCH and DELETE method handlers.
class DetailsView(RetrieveUpdateDestroyAPIView):
  """View responsible for Read, Update and Delete"""

  queryset = BucketList.objects.all()
  serializer_class = BucketListSerializer