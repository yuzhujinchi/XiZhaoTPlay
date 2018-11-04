from django.urls import path

from project_app.views import project_views, module_views

urlpatterns = [
    # 项目管理
    path('project_manage/', project_views.project_manage),
    path('create_project/', project_views.create_project),
    path('edit_project/<int:pid>/', project_views.edit_project),
    path('delete_project/<int:pid>/', project_views.delete_project),
    # 模块管理
    path('module_manage/', module_views.module_manage),
    path('create_module/', module_views.create_module),
    path('edit_module/<int:mid>/', module_views.edit_module),
    path('delete_module/<int:mid>/', module_views.delete_module),
]