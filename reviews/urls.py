from django.urls import path

from . import views
urlpatterns = [
   path('', views.reviews_view, name='index')
]