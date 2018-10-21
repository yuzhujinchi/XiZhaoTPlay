from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from project_app.forms import CreateModuleForm, EditModuleForm
# Create your views here.


@login_required()
def module_manage(request):
    user = request.session.get("user", "")
    modules_all = Module.objects.all()
    return HttpResponse(render(request, 'module_manage.html', {
        "user": user,
        "modules": modules_all,
        "type": "modules_list"}))


@login_required()
def create_module(request):
    if request.method == 'POST':
        form = CreateModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data["project"]
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            Module.objects.create(project=project, name=name, description=description)
            return HttpResponseRedirect('/manage/module_manage/')

    else:
        form = CreateModuleForm()
        return render(request, 'module_manage.html', {
            "form": form,
            "type": "create"})


@login_required()
def edit_module(request, mid):
    if request.method == 'POST':
        form = EditModuleForm(request.POST)
        if form.is_valid():
            model = Module.objects.get(id=mid)
            model.project = form.cleaned_data["project"]
            model.name = form.cleaned_data["name"]
            model.description = form.cleaned_data["description"]
            model.save()
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        if mid > 0 and isinstance(mid, int):
            form = EditModuleForm(
                instance=Module.objects.get(id=mid)
            )
            return render(request, 'module_manage.html', {
                "form": form,
                "type": "edit"})


@login_required()
def delete_module(request, mid):
    Module.objects.get(id=mid).delete()
    return HttpResponseRedirect('/manage/module_manage/')
