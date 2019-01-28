from django.shortcuts import render
from votes.models import Candidate, Position, Vote

# Create your views here.
def index(request):
    candidate_list = Candidate.objects.order_by('position')

def candidate_detail(request):
    return HttpResponse("This is the candidate_detail page")

def candidate_create(request):
    return HttpResponse("This is the candidate_create page")

def candidate_update(request):
    return HttpResponse("This is the candidate_update page")

def position_create(request):
    return HttpResponse("This is the position_create page")

def vote(request):
    return HttpResponse("This is the vote page")
