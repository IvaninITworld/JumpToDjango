from django.shortcuts import render, redirect
# authenticate : 사용자 인증 담당
# login : 로그인 담당
from django.contrib.auth import authenticate, login
from common.forms import UserForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # form.cleaned_data.get : 폼의 입력값을 개별적으로 얻고 싶은 경우
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            form = UserForm()
        return render(request, 'common/signup.html', {'form': form})
