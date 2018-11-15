from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from account.forms import ProfileForm

# Create your views here.
def login(request):
    # 이미 로그인 했으면서 또 로그인 페이지 보여달라고 할 때
    if request.user.is_authenticated:  # 유저가 로그인했으면
        return redirect('question:list')
    # 사용자가 로그인을 요청하면?
    if request.method == "POST": 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # 사용자가 입력한 정보 + 폼과 얼마나 맞는지 검증
            return redirect('question:list')
        
    # 로그인을 위한 폼을 요청했을때?
    else:
        form = AuthenticationForm()  # 이미 만든 폼
    return render(request, 'account/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('question:list')

def signup(request):
    
    if request.user.is_authenticated:
        return redirect('question:list')
    
    if request.method == "POST":
        # 사용자를 등록하는 로직
        form = UserCreationForm(request.POST)
        pro_form = ProfileForm(request.POST)  # 다시 만든 폼도 넣기

        if form.is_valid() and pro_form.is_valid():
            user = form.save()
            profile = pro_form.save(commit=False)  # 임시저장된 profile의 정보를 user와 합쳐야 한다
            profile.user = user   # user 키값에 의해 profile의 칸이 모두 채워짐
            profile.save()
            auth_login(request, user)
            return redirect('question:list')
    else:
        # 정보를 입력하는 폼을 전달
        form = UserCreationForm()
        pro_form = ProfileForm()
    return render(request, 'account/signup.html', {'form': form, 'pro_form': pro_form})


