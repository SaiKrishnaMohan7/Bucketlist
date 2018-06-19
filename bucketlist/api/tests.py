# api/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from .models import BucketList

class ModelTestCase(TestCase):
  """Test case for Bucketlist model"""

  def setUp(self):
    """Intial Setup, test client"""
    self.bucketlist_name = 'Test Driven Dev'
    self.bucketlist = BucketList(name=self.bucketlist_name)
  
  def test_model_can_create_bucketlist(self):
    """Test Bucketlist model"""
    old_count = BucketList.objects.count()
    self.bucketlist.save()
    new_count = BucketList.objects.count()
    self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
  """Test suite for Bucketlist model"""

  def setUp(self):
    """API test client"""
    self.client = APIClient()
    self.bucketlist_data = {'name': 'Make a conversational AI'}
    self.response = slef.client.post(
      reverse('create'),
      self.bucketlist_data,
      format="json"
    )
  
  def test_api_create_bucketlist_item(self):
    """Test API create"""
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
