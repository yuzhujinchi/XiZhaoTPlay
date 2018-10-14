from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from user_app.models import Project

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
                request.session["user"] = username
                return HttpResponseRedirect('/project_manage/')
            else:
                return HttpResponse(render(request, 'index.html', {"error": "用户名或密码错误！"}))


@login_required()
def project_manage(request):
    user = request.session.get("user", "")
    projects_all = Project.objects.all()
    print(projects_all)
    return HttpResponse(render(request, 'project_manage.html', {
        "user": user,
        "projects": projects_all}))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
