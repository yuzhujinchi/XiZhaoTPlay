from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Project
# Create your views here.


@login_required()
def project_manage(request):
    user = request.session.get("user", "")
    projects_all = Project.objects.all()
    return HttpResponse(render(request, 'project_manage.html', {
        "user": user,
        "projects": projects_all,
        "type": "projects_list"}))


@login_required()
def create_project(request):
    user = request.session.get("user", "")
    projects_all = Project.objects.all()
    return HttpResponse(render(request, 'project_manage.html', {
        "user": user,
        "projects": projects_all,
        "type": "create_project"}))

