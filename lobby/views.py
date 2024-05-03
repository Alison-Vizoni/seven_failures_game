from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from tester.forms import TesterForm


@csrf_exempt
def home(request):
    tester_form = TesterForm()
    return render(request, 'lobby/index.html', {'form': tester_form})


@require_http_methods(['POST'])
@csrf_exempt
def login(request):
    # data = request.POST.dict()
    # username = data.get('username')
    # password = data.get('password')

    # if not all([username, password, isinstance(username, str), isinstance(password, str)]):
    #     pass

    # try:
    #     tester = Tester.objects.get(username=username, password=password)
    # except Tester.DoesNotExist:
    #     return HttpResponse("Username or password incorrectly.", status=404)

    # make_password()

    form = TesterForm(request.POST)
    if form.is_valid():
        return redirect('show_games')

    form = TesterForm()
    return render(request, 'lobby/index.html', {'form': form})


@csrf_exempt
def show_games(request):
    return render(request, 'lobby/show_games.html')
