from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.


def index(request):
    return HttpResponse(render(request, 'index.html'))


def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return HttpResponse(render(request, 'index.html', {"error": "用户名或密码为空！"}))

        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponse(render(request, 'project_manage.html'))
            else:
                return HttpResponse(render(request, 'index.html', {"error": "用户名或密码错误！"}))


