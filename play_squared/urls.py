from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('gamerecs/', views.GameRecommendationList.as_view(), name='gamerecommendation_read'),
    path('gamerecs/<int:pk>', views.GameRecommendationDetail.as_view(), name='gamerecommendation_detail'),
    path('leaderboard/', views.ScoreList.as_view(), name='score_read'),
]