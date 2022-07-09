from .models import GameRecommendation, Score
from rest_framework import generics
from .serializers import GameRecommendationSerializer, ScoreSerializer

# Create your views here.
class GameRecommendationList(generics.ListCreateAPIView):
    queryset = GameRecommendation.objects.all()
    serializer_class = GameRecommendationSerializer

class GameRecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameRecommendation.objects.all()
    serializer_class = GameRecommendationSerializer

class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer