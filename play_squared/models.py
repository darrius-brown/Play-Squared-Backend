
import uuid
from django.db import models
from django.contrib.auth.models import User

class GameRecommendation(models.Model):
    uuid = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4)
    game_name = models.CharField(max_length=100, default='new_game')
    description = models.TextField()
    author = models.ForeignKey(User, related_name='game_recommendation', on_delete=models.CASCADE, default=1)
 
    def __str__(self):
        return self.game_name


class Score(models.Model):
    game = models.CharField(max_length=100, default = 'game')
    amount = models.CharField(max_length=100)
    board = models.CharField(max_length=100, default = '4x4')
    author = models.ForeignKey(User, related_name='score', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.amount






