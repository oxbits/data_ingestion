from django.conf.urls import include, url

urlpatterns = [
    url(r'^progressbarupload/?', include('progressbarupload.urls')),
]