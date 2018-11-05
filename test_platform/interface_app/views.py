from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json


# Create your views here.
@login_required()
def case_manage(request):
    """
    测试用例管理
    :param request: 请求
    :return:
    """
    if request.method == "GET":
        return render(request, "case_manage.html", {"type": "list"})
    else:
        return HttpResponse("404")


@login_required()
def debug(request):
    """
    创建/调试接口
    :param request:请求
    :return:
    """
    if request.method == "GET":
        return render(request, "api_debug.html", {"type": "debug"})
    else:
        return HttpResponse("404")


@login_required()
def api_debug(request):
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        # parm_type = request.POST.get("parm_type")
        header = request.POST.get("req_header")
        parameter = request.POST.get("req_parameter")

        try:
            parameter_dict = json.loads(parameter.replace("'", "\""))
            header_dict = json.loads(header.replace("'", "\""))
        except Exception as e:
            return HttpResponse("".format(e))

        r = None
        if method == "GET":
            r = requests.get(url, params=parameter_dict)
        if method == "POST":
            r = requests.post(url, data=parameter_dict, headers=header_dict)

        return HttpResponse(r.text)

    else:
        return render(request, "api_debug.html", {"type": "debug"})
