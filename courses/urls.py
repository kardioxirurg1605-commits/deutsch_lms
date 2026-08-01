from django.urls import path
from . import views

urlpatterns = [
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
]