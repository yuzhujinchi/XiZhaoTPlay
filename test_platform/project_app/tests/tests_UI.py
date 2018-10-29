from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from django.contrib.auth.models import User
from time import sleep
from project_app.models import Project, Module
from selenium.webdriver.support.select import Select


class ProjectTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        User.objects.create_user(username="test01", email="test01@mail.com", password="test123456")
        Project.objects.create(name="测试平台项目", description="项目描述")
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('test01')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('test123456')
        sleep(2)
        self.driver.find_element_by_id("loginButton").click()
        sleep(3)

    def test_project_manage(self):
        project_lists = self.driver.find_element_by_id("projectLists").text
        self.assertIn("测试平台项目", project_lists)

    def test_create_project(self):
        self.driver.find_element_by_id("createButton").click()
        sleep(1)
        project_name = self.driver.find_element_by_id("id_name")
        project_name.send_keys("UI自动化项目01")
        project_desc = self.driver.find_element_by_id("id_description")
        project_desc.send_keys("UI自动化项目描述balabalabala")
        sleep(1)
        self.driver.find_element_by_id("createSubmitButton").click()
        sleep(2)
        project_lists = self.driver.find_element_by_id("projectLists").text
        self.assertIn("UI自动化项目01", project_lists)
        self.assertIn("UI自动化项目描述balabalabala", project_lists)

    def test_edit_project(self):
        self.driver.find_element_by_id("editButton").click()
        sleep(2)
        project_name = self.driver.find_element_by_id("id_name")
        project_name.send_keys("UI自动化项目更新01")
        project_desc = self.driver.find_element_by_id("id_description")
        project_desc.send_keys("UI自动化项目描述更新balabalabala")
        self.driver.find_element_by_id("id_status").click()
        sleep(1)
        self.driver.find_element_by_id("editSubmitButton").click()
        sleep(1)
        project_lists = self.driver.find_element_by_id("projectLists").text
        self.assertIn("UI自动化项目更新01", project_lists)
        self.assertIn("UI自动化项目描述更新balabalabala", project_lists)

    def test_delete_project(self):
        self.driver.find_element_by_id("deleteButton").click()
        sleep(1)
        self.driver.switch_to.alert.accept()
        project_lists = self.driver.find_element_by_id("projectLists").text
        self.assertNotIn("测试平台项目", project_lists)


class ModuleTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        User.objects.create_user(username="test01", email="test01@mail.com", password="test123456")
        Project.objects.create(name="测试平台项目", description="项目描述")
        project = Project.objects.get(name="测试平台项目")
        Module.objects.create(project=project, name="测试平台模块", description="模块描述")
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('test01')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('test123456')
        sleep(2)
        self.driver.find_element_by_id("loginButton").click()
        sleep(2)
        self.driver.get('%s%s' % (self.live_server_url, '/manage/module_manage/'))
        sleep(2)

    def test_module_manage(self):
        module_lists = self.driver.find_element_by_id("moduleLists").text
        self.assertIn("测试平台模块", module_lists)

    def test_create_module(self):
        self.driver.find_element_by_id("createButton").click()
        sleep(1)
        s1 = Select(self.driver.find_element_by_id('id_project'))
        s1.select_by_index(1)
        project_name = self.driver.find_element_by_id("id_name")
        project_name.send_keys("UI自动化模块01")
        project_desc = self.driver.find_element_by_id("id_description")
        project_desc.send_keys("UI自动化模块描述balabalabala")
        sleep(1)
        self.driver.find_element_by_id("createSubmitButton").click()
        sleep(2)
        module_lists = self.driver.find_element_by_id("moduleLists").text
        self.assertIn("UI自动化模块01", module_lists)
        self.assertIn("UI自动化模块描述balabalabala", module_lists)

    def test_edit_module(self):
        self.driver.find_element_by_id("editButton").click()
        sleep(2)
        project_name = self.driver.find_element_by_id("id_name")
        project_name.send_keys("UI自动化模块更新01")
        project_desc = self.driver.find_element_by_id("id_description")
        project_desc.send_keys("UI自动化模块描述更新balabalabala")
        self.driver.find_element_by_id("editSubmitButton").click()
        sleep(1)
        module_lists = self.driver.find_element_by_id("moduleLists").text
        self.assertIn("UI自动化模块更新01", module_lists)
        self.assertIn("UI自动化模块描述更新balabalabala", module_lists)

    def test_delete_module(self):
        self.driver.find_element_by_id("deleteButton").click()
        sleep(1)
        self.driver.switch_to.alert.accept()
        module_lists = self.driver.find_element_by_id("moduleLists").text
        self.assertNotIn("测试平台模块", module_lists)
