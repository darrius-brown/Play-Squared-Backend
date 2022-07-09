from rest_framework import serializers
from .models import GameRecommendation, Score

class GameRecommendationSerializer(serializers.HyperlinkedModelSerializer):
    # game_recommendation = serializers.HyperlinkedIdentityField(
    #     view_name='game_recommendation_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = GameRecommendation
        fields = ('pk', 'user', 'game_name', 'description' )
    
class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    # score = serializers.HyperlinkedIdentityField(
    #     view_name='score_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = Score
        fields = ('user', 'game_name', 'amount', 'date')