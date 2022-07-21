from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class GameRecommendation(models.Model):
    game_name = models.CharField(max_length=100, default='new_game')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_recommendations', null=True)

    def __str__(self):
        return self.game_name
class Game(models.Model):
    name =  models.CharField(max_length=100, default='game_name')
    def __str__(self):
        return self.name

class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='scores', default=0)
    amount = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores', null=True)

    def __str__(self):
        return self.amount






