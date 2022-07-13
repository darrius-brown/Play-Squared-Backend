from .models import GameRecommendation, Score, Game
from rest_framework import generics
from .serializers import GameRecommendationSerializer, ScoreSerializer, GameSerializer

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

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer