from django.conf.urls import url

from . import views # dot means import from the root location, and import the views module

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
]
