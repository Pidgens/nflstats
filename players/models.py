from django.db import models

# Create your models here.

import nflgame

class Player(models.Model):

    name = models.CharField(max_length=40, default='T.Brady')
    week = models.IntegerField(default=5)
    year = models.IntegerField(default=2015)

    ERROR = {
        'status': -1,
    }
    SUCCESS = {
        'status' : 1
    }

    def getGames(self, year, week_num, home=None, away=None):
        games = nflgame.games(year=year, week=week_num)
        list_ofPlayers = nflgame.combine_game_stats(games)
        return list_ofPlayers

    @staticmethod
    def getStats(name, week, year):
        print 'SOMETHING HERE'
        name = str(name)
        week = int(week)
        year = int(year)
        games = nflgame.games(year=year, week=week)
        listofPlayers = nflgame.combine_game_stats(games)
        player = listofPlayers.name(name)
        if not player:
            Player.ERROR['message'] = 'Player does not exist.'
            return Player.ERROR
        else:
            playerStats = player.formatted_stats()
            Player.SUCCESS['message'] = playerStats
            player_save = Player(
                name=name,
                week=week,
                year=year,
            )
            player_save.save()
            return Player.SUCCESS