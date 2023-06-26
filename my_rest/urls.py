from django.urls import path
from . import views

urlpatterns = [
    path('articel/',views.ArticelAPIView.as_view()),
    path('articel/<int:id>/', views.DetailArticelAPIView.as_view()),
]
