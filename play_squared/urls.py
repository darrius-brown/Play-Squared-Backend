from django.urls import path
from . import views

urlpatterns = [
    path('gamerecommendation/', views.GameRecommendationList.as_view(), name='gamerecommendation_list'),
    path('gamerecommendation/<int:pk>/', views.GameRecommendationDetail.as_view(), name='gamerecommendation_detail'),
    path('score/', views.ScoreList.as_view(), name='score_list'),
    path('score/<int:pk>/', views.ScoreDetail.as_view(), name='score_detail'),
]