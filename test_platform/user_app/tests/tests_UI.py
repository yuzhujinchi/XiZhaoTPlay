from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from django.contrib.auth.models import User
from time import sleep
from project_app.models import Project


class LoginTests(StaticLiveServerTestCase):

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

    def test_login_failed(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        sleep(2)
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('error')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('error')
        sleep(2)
        self.driver.find_element_by_id("loginButton").click()
        sleep(2)
        error_msg = self.driver.find_element_by_id("errorMsg").text
        self.assertEqual("用户名或密码错误！", error_msg)

    def test_login_success(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        sleep(2)
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('test01')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('test123456')
        sleep(2)
        self.driver.find_element_by_id("loginButton").click()
        sleep(2)
        home_name = self.driver.find_element_by_class_name("form-signin-heading").text
        self.assertEqual("惜朝-TPlay", home_name)
