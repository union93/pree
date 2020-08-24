from django.contrib import auth
from django.shortcuts import redirect, render

from accounts.models import User


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                email=request.POST['email'],
                username=request.POST['nickname'],
                password=request.POST['password1'],
                date_of_birth =request.POST['date_time'],
                phone=request.POST['phone']
            )
            auth.login(request, user)
            return redirect('')
        return render(request,'3_sign_up_page/sign_up.hmtl')
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email,password =password)
        if user is not None:
            auth.login(request, user )
            return redirect('')
        else:
            return render(request,'2_login_page/front_login.html',{'error': '이메일 혹은 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request,'2_login_page/front_login.html' )

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('')
    return render(request,'2_login_page/front_login.html')