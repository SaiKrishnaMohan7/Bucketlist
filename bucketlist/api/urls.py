# api/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BucketListCreateView
from .views import DetailsView

urlpatterns = {
    url(r'^bucketlist/$', BucketListCreateView.as_view(), name="create"),
    url(r'^bucketlist/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
}
# format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs.
# It appends the format to be used to every URL in the pattern.
urlpatterns = format_suffix_patterns(urlpatterns)