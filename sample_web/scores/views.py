from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Scores


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def get_score(request, user_input=None):
    if request.method == 'GET':
        result = int(user_input) + 1
        score = Scores.objects.create(result=result, user=request.user)
        return JsonResponse({'result': score.result})
