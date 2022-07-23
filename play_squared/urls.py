from django.urls import path
from . import views

urlpatterns = [
    # path('gamerecs/', views.listGameRecommendations),

    path('gamerecs/', views.GameRecommendationList.as_view(), name='gamerecommendation_read'),
    path('gamerecs/create', views.GameRecommendationList.as_view(), name='gamerecommendation_create'),
    path('gamerecs/<int:pk>', views.GameRecommendationDetail.as_view(), name='gamerecommendation_detail'),
    path('mock_login', views.mock_login),
    path('mock_signup', views.mock_signup),
    path('leaderboard/', views.ScoreList.as_view(), name='score_read'),
    path('simon/', views.ScoreList.as_view(), name='score_create'),
    # path('score/<int:pk>/', views.ScoreDetail.as_view(), name='score_detail'),
    # path('game/', views.GameList.as_view(), name='game_list'),
    # path('game/<int:pk>/', views.GameDetail.as_view(), name='game_detail'),
  
]