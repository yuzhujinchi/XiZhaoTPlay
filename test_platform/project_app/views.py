from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from .forms import CreateProjectForm, EditProjectForm
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
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            Project.objects.create(name=name, description=description)
            return HttpResponseRedirect('/project/project_manage/')

    else:
        form = CreateProjectForm()
        return render(request, 'project_manage.html', {
            "form": form,
            "type": "create"})


@login_required()
def edit_project(request, pid):
    if request.method == 'POST':
        form = EditProjectForm(request.POST)
        if form.is_valid():
            model = Project.objects.get(id=pid)
            model.name = form.cleaned_data["name"]
            model.description = form.cleaned_data["description"]
            model.status = form.cleaned_data["status"]
            model.save()
            return HttpResponseRedirect('/project/project_manage/')
    else:
        if pid > 0 and isinstance(pid, int):
            form = EditProjectForm(
                instance=Project.objects.get(id=pid)
            )
            return render(request, 'project_manage.html', {
                "form": form,
                "type": "edit"})


@login_required()
def delete_project(request, pid):
    Project.objects.get(id=pid).delete()
    return HttpResponseRedirect('/project/project_manage/')
