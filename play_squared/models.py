from django.db import models

class GameRecommendation(models.Model):
    user = models.CharField(max_length=100, default='unknown_user')
    game_name = models.CharField(max_length=100, default='new_game')
    description = models.TextField()

    def __str__(self):
        return self.game_name

class Score(models.Model):
    user = models.CharField(max_length=100, default='unknown_user')
    game_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.game_name