from django.contrib import admin
from user_app.models import Project, Module


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "status", "created_at"]


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
