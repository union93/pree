from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserFrom, LoginForm
from .models import User


def signup(request):
    if request.method == "POST":
        form = UserFrom(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
        else:
            form = UserFrom()
            return render(request, '3_sign_up_page/sign_up.html',{'form': form})

def login_f(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, '2_login_page/front_login.html', {'form': form})

def index(request):
    return render(request, '1_main_page/home.html')
