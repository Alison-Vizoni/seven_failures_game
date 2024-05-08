from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from lobby.utils import create_access_token
from tester.forms import TesterForm


@csrf_exempt
def home(request):
    tester_form = TesterForm()
    return render(request, 'lobby/index.html', {'form': tester_form})


@require_http_methods(['POST'])
@csrf_exempt
def login(request):
    form = TesterForm(request.POST)
    if form.is_valid():
        token = create_access_token(form.username)
        url = '/games/?' + urlencode({
            'token': token
        })
        return redirect(url)

    return render(request, 'lobby/index.html', {'form': form})


@csrf_exempt
def show_games(request):
    return render(request, 'lobby/show_games.html')
