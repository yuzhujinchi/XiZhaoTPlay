# Generated by Django 2.1.1 on 2018-10-14 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='模块名称')),
                ('description', models.TextField(default='', verbose_name='模块描述')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='项目名称')),
                ('description', models.TextField(default='', verbose_name='项目描述')),
                ('status', models.BooleanField(default=False, verbose_name='项目状态')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.Project'),
        ),
    ]
