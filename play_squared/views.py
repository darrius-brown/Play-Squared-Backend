from .models import GameRecommendation, Score
from django.db.models.functions import Cast
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import GameRecommendationSerializer, ScoreSerializer, UserSerializer

class CreateUser(generics.CreateAPIView):
  model = get_user_model()
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]


class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.extra(select={'score': 'CAST(amount AS INTEGER)'}).order_by('-score')[:10]
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

class GameRecommendationList(generics.ListCreateAPIView):
  serializer_class = GameRecommendationSerializer
  queryset = GameRecommendation.objects.all()
  permission_classes = [permissions.IsAuthenticated] 

class GameRecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = GameRecommendationSerializer
  queryset = GameRecommendation.objects.all()
  permission_classes = [permissions.IsAuthenticated]

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ScoreSerializer
  queryset = Score.objects.all()
  permission_classes = [permissions.IsAuthenticated]

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)    