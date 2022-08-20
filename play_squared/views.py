from .models import GameRecommendation, Score
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import GameRecommendationSerializer, ScoreSerializer, UserSerializer

class CreateUser(generics.CreateAPIView):
  model = get_user_model()
  permission_classes = [permissions.AllowAny]
  serializer_class = UserSerializer

class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]

class GameRecommendationList(generics.ListCreateAPIView):
  serializer_class = GameRecommendationSerializer
  queryset = GameRecommendation.objects.all()
  permission_classes = [permissions.AllowAny] 

class GameRecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = GameRecommendationSerializer
  queryset = GameRecommendation.objects.all()
  permission_classes = [permissions.AllowAny]

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ScoreSerializer
  queryset = Score.objects.all()
  permission_classes = [permissions.AllowAny]

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)    



    # def post(self, request, *args, **kwargs):
    #     request.data['user_string'] = request.user.username
    #     return super().post(request, *args, **kwargs)

#get detail/ edit detail, destroy detail
# class GameRecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = GameRecommendation.objects.all()
#     serializer_class = GameRecommendationSerializer

#     permission_classes = [permissions.IsAuthenticated]

# class GameRecommendationUpdateProtected(generics.UpdateAPIView):
#     serializer_class = GameRecommendationSerializer
#     queryset  = GameRecommendation.objects.all()

# class ScoreList(generics.ListCreateAPIView):
#     queryset = Score.objects.all()
#     serializer_class = ScoreSerializer

# class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Score.objects.all()
#     serializer_class = ScoreSerializer



# class GameDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

# def mock_login(request):
#     return JsonResponse({'loggedIn':True, 'username': 'mock_user'})

# def mock_signup(request):
#     return JsonResponse({'loggedIn':True, 'username': 'mock_user'})    