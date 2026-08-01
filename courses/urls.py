from django.urls import path
from . import views

urlpatterns = [
    path('', views.chapter_list, name='chapter_list'), # Asosiy kirish sahifasi
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
]