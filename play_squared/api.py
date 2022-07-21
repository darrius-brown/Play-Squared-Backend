from .models import  GameRecommendation, Score
from rest_framework import permissions, viewsets
from .serializers import   GameRecommendationSerializer, ScoreSerializer

class GameRecommendationViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = GameRecommendationSerializer
    def get_queryset(self):
        return self.request.user.game_recommendations.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ScoreViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ScoreSerializer
    def get_queryset(self):
        return self.request.user.scores.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)