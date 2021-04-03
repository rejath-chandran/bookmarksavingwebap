from django.urls import path
from .views import PostCreateView
from . import views

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('search', views.search, name='search')
]


