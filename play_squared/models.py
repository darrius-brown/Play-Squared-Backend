from tkinter import CASCADE
from django.db import models

class GameRecommendation(models.Model):
    user = models.CharField(max_length=100, default='unknown_user')
    game_name = models.CharField(max_length=100, default='new_game')
    description = models.TextField()

    def __str__(self):
        return self.game_name
class Game(models.Model):
    name =  models.CharField(max_length=100, default='game_name')
    def __str__(self):
        return self.name

class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='scores', default=1)
    user = models.CharField(max_length=100, default='unknown_user')
    amount = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.amount






