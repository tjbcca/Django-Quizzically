from django.shortcuts import render
from app.models import *
import random

def freeplay(request, points, status):
    if Questions.objects.count() == 0:
        load_questions()
    qid = QInfo(random.randint(1,Questions.objects.count()),'id')
    return render(request, 'freeplay.html', {'question':QInfo(qid,'question'),'answer':QInfo(qid,'answer'),'choices':split_choices(qid),'category':QInfo(qid,'category'),'points':points,'goodJob':(1 + points),'status':status})
def teams(request, team1, team2, team3, team4):
    if Questions.objects.count() == 0:
        load_questions()
    teamScores = {'team1': team1, 'team2': team2, 'team3': team3, 'team4': team4}
    max_value = max(teamScores.values())
    leaders = [var for var, value in teamScores.items() if value == max_value and value != 0]
    qid = QInfo(random.randint(1,Questions.objects.count()),'id')
    return render(request, 'teams.html', {'question':QInfo(qid,'question'),'answer':QInfo(qid,'answer'),'choices':split_choices(qid),'category':QInfo(qid,'category'),'team1':team1,'team2':team2,'team3':team3,'team4':team4,'1V':(1 + team1),'2V':(1 + team2),'3V':(1 + team3),'4V':(1 + team4),'lead': leaders})
def home(request):
    load_questions()
    count = Questions.objects.count()
    qid = QInfo(random.randint(1,count),'id')
    return render(request, 'home.html', {'question': QInfo(qid,'question'),'answer': QInfo(qid,'answer'), 'qCount': count})