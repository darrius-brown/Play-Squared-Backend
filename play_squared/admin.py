from django.contrib import admin
from .models import Score, GameRecommendation, Game

# Register your models here.
admin.site.register(Score)
admin.site.register(GameRecommendation)
admin.site.register(Game)
