from django.test import TestCase, Client
from django.contrib.auth.models import User
from project_app.models import Project, Module


class ProjectTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(username="test01", email="test01@mail.com", password="test123456")
        self.client.post(path='/login/', data={"username": "test01", "password": "test123456"})
        Project.objects.create(name="测试平台项目", description="项目描述")

    def test_project_manage(self):
        response = self.client.get('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("测试平台项目", project_html)

    def test_create_project(self):
        response = self.client.post(path='/manage/create_project/', data={"name": "创建项目1", "description": "项目描述",
                                                                          "status": False})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/manage/project_manage/')
        self.assertEqual(response.status_code, 200)
        project_html = response.content.decode("utf-8")
        self.assertIn("创建项目1", project_html)

    def test_edit_project(self):
        project = Project.objects.get(name="测试平台项目")
        pid = project.id
        response = self.client.post(path='/manage/edit_project/%d/' % pid, data={"name": "创建项目1更新",
                                                                                 "description": "项目描述更新",
                                                                                 "status": False})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/manage/project_manage/')
        self.assertEqual(response.status_code, 200)
        project_html = response.content.decode("utf-8")
        self.assertIn("创建项目1更新", project_html)
        self.assertIn("项目描述更新", project_html)

    def test_delete_project(self):
        project = Project.objects.get(name="测试平台项目")
        pid = project.id
        response = self.client.post(path='/manage/delete_project/%d/' % pid)
        self.assertEqual(response.status_code, 302)
        # response = self.client.get('/manage/project_manage/')
        # self.assertEqual(response.status_code, 200)
        project_html = response.content.decode("utf-8")
        self.assertNotIn("测试平台项目", project_html)


class ModuleTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(username="test01", email="test01@mail.com", password="test123456")
        self.client.post(path='/login/', data={"username": "test01", "password": "test123456"})
        Project.objects.create(name="测试平台项目", description="项目描述")
        project = Project.objects.get(name="测试平台项目")
        Module.objects.create(project=project, name="测试平台模块", description="模块描述")

    def test_module_manage(self):
        response = self.client.get('/manage/module_manage/')
        module_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("测试平台模块", module_html)

    def test_create_module(self):
        project = Project.objects.get(name="测试平台项目")
        response = self.client.post(path='/manage/create_module/', data={"project": project.id,
                                                                         "name": "创建模块1", "description": "模块描述"})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/manage/module_manage/')
        self.assertEqual(response.status_code, 200)
        module_html = response.content.decode("utf-8")
        self.assertIn("创建模块1", module_html)

    def test_edit_module(self):
        project = Project.objects.get(name="测试平台项目")
        module = Module.objects.get(name="测试平台模块")
        response = self.client.post(path='/manage/edit_module/%d/' % module.id, data={"project": project.id,
                                                                                "name": "测试平台模块更新",
                                                                                "description": "模块描述更新"})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/manage/module_manage/')
        self.assertEqual(response.status_code, 200)
        module_html = response.content.decode("utf-8")
        self.assertIn("测试平台模块更新", module_html)
        self.assertIn("模块描述更新", module_html)

    def test_delete_module(self):
        module = Module.objects.get(name="测试平台模块")
        response = self.client.post(path='/manage/delete_module/%d/' % module.id)
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/manage/module_manage/')
        self.assertEqual(response.status_code, 200)
        module_html = response.content.decode("utf-8")
        self.assertNotIn("测试平台模块", module_html)
