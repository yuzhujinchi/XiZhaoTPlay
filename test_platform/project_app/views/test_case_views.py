from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from project_app.forms import CreateModuleForm, EditModuleForm
# Create your views here.


@login_required()
def test_case_manage(request):
    return HttpResponse(render(request, 'test_case_manage.html'))
