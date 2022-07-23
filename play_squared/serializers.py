from rest_framework import serializers
from .models import GameRecommendation, Score, Game

class GameRecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameRecommendation
        fields = ('pk','uuid', 'user_string', 'game_name', 'description' )
    
class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.StringRelatedField (
        
        many=False,
        
    )
    class Meta:
        model = Score
        fields = ('game','pk', 'amount', 'user_string')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    # game = serializers.HyperlinkedIdentityField(
    #     view_name='tail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = Game
        fields = [('name')]