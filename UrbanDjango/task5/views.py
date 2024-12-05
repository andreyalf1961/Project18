from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['Bob', 'Tom', 'Peter', 'Mary']


# Create your views here.
def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in users and password == repeat_password and int(age) >= 18:
                info['welcome'] = f'Приветствуем, {username}!'
                return render(request, 'fifth_task/registration_page.html', {'welcome': info['welcome']})

            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page.html', {'error': info['error']})
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', {'error': info['error']})
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', {'error': info['error']})

    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users and password == repeat_password and int(age) >= 18:
            info['welcome'] = f'Приветствуем, {username}!'
            return render(request, 'fifth_task/registration_page.html', {'welcome': info['welcome']})

        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'fifth_task/registration_page.html', {'error': info['error']})
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'fifth_task/registration_page.html', {'error': info['error']})
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'fifth_task/registration_page.html', {'error': info['error']})

    return render(request, 'fifth_task/registration_page.html')
