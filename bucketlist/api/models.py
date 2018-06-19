from django.db import models

class BucketList(models.Model):
  """BucketList model Class"""

  name = models.CharField(max_length=255, blank=False, unique=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    """Human Readable"""
    return '{}'.format(self.name)

