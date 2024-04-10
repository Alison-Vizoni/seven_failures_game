from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
def home(request):
    return render(request, 'lobby/index.html')


@require_http_methods(['POST'])
@csrf_exempt
def login(request):
    data = request.POST.dict()
    return redirect('show_games')


@csrf_exempt
def show_games(request):
    return render(request, 'lobby/show_games.html')


def _validate_token(token):
    pass
