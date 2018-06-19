from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .serializers import BucketListSerializer
from .models import BucketList

# ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
class BucketListCreate(ListCreateAPIView):
  """View responsible for creating bucketlist items"""

  queryset = BucketList.objects.all()
  serializer_class = BucketListSerializer

  def create_bucketlist_item(self, serializer):
    """Save POST data"""
    serializer.save()
