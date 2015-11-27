from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse, JsonResponse

from players.models import Player
import json

def getstats(request):
    if request.method == 'POST':
        # Get data
        player = request.POST['player_name']
        week = request.POST['week']
        year = request.POST['year']
        response = Player.getStats(player, week, year)
        return JsonResponse(response)

def enterName(request):
    return render(request, 'home.html')