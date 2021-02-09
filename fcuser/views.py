from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    # if request.method == 'GET':
    #     return render(request, 'login.html')

    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = 'Enter all items'
    #     else: 
    #         fcuser = Fcuser.objects.get(username = username)
    #         if password == fcuser.password:
    #             # if check_password(password, fcuser.password): 
    #             # 였는데 일치하면 ㅇㅇ이라는 뜻인줄 알았는데 값이 정반대로 나옴. 뭐임??
    #             # ???? 도대체 왜 check_password가 반대값으로 나는 거임?
    #             request.session['user'] = fcuser.id
    #             return redirect('/')
    #         else:
    #             res_data['error'] = 'Worng Password'

    #     return render(request, 'login.html', res_data)

def home(request):
    # user_pk = request.session.get('user')
    # if user_pk:
    #     fcuser = Fcuser.objects.get(pk=user_pk) 
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

# 프론트엔드에서 보통 비밀번호 재확인 등 설정을 많이 하지만
# 백엔드에서도 할 수 있음

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = 'Enter all items'
        elif password != re_password:
            # return HttpResponse('비밀번호가 다릅니다!')
            res_data['error'] = 'Input same passwords'
        else:
            fcuser = Fcuser(
            username = username,
            useremail = useremail,
            password = password,
            )

            fcuser.save()    

        return render(request, 'register.html', res_data)
    




