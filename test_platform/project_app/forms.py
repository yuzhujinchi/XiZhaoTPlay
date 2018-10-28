from django import forms
from .models import Project, Module

# class ProjectForm(forms.Form):
#     name = forms.CharField(label='项目名称', max_length=100)
#     description = forms.CharField(label="项目描述", widget=forms.Textarea)


class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'status']


class EditProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ["created_at"]


class CreateModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        exclude = ["created_at"]


class EditModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        exclude = ["created_at"]
