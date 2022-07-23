from .models import GameRecommendation, Score, Game
from rest_framework import generics, permissions
# from rest_framework.permissions import AllowAny
from django.http import JsonResponse, HttpResponse
from .serializers import GameRecommendationSerializer, ScoreSerializer, GameSerializer
#get
def listGameRecommendations(request):
    GameRecommendations = GameRecommendation.objects.all().values()
    GameRecommendation_list = list(GameRecommendations)
    return JsonResponse(GameRecommendation_list, safe=False)
#get/create
class GameRecommendationList(generics.ListCreateAPIView):
    queryset = GameRecommendation.objects.all()
    serializer_class = GameRecommendationSerializer

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.data['user_string'] = request.user.username
        return super().post(request, *args, **kwargs)

#get detail/ edit detail, destroy detail
class GameRecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = GameRecommendation.objects.all()
    serializer_class = GameRecommendationSerializer

class GameRecommendationUpdateProtected(generics.UpdateAPIView):
    serializer_class = GameRecommendationSerializer
    queryset  = GameRecommendation.objects.all()

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

def mock_login(request):
    return JsonResponse({'loggedIn':True, 'username': 'mock_user'})

def mock_signup(request):
    return JsonResponse({'loggedIn':True, 'username': 'mock_user'})    