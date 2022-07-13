from rest_framework import serializers
from .models import GameRecommendation, Score, Game

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
    game = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        many=False,
        read_only=True
    )
    class Meta:
        model = Score
        fields = ('game','user', 'amount', 'date')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    # game = serializers.HyperlinkedIdentityField(
    #     view_name='tail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = Game
        fields = [('name')]