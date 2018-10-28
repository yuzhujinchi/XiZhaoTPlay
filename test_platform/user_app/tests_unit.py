from django.test import TestCase, Client
from django.contrib.auth.models import User


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username="test01", email="test01@mail.com", password="test123456")
        self.client = Client()

    def test_user_can_login(self):
        """Users that can login successfully"""
        user = User.objects.get(username="test01")
        self.assertEqual(user.email, "test01@mail.com")

    def test_user_create(self):
        """Users that can be created successfully"""
        User.objects.create_user(username="test02", email="test02@mail.com", password="test654321")
        user = User.objects.get(username="test02")
        self.assertEqual(user.email, "test02@mail.com")

    def test_user_update(self):
        """Users that can be updated successfully"""
        user = User.objects.get(username="test01")
        user.username = "test01_u"
        user.email = "test01_u@mail.com"
        user.save()
        user = User.objects.get(username="test01_u")
        self.assertEqual(user.email, "test01_u@mail.com")

    def test_user_delete(self):
        """Users that can be deleted successfully"""
        user = User.objects.get(username="test01")
        user.delete()
        users = User.objects.all()
        self.assertEqual(len(users), 0)


class UserLoginTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="test01", email="test01@mail.com", password="test123456")
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_action_null(self):
        """用户名密码为空"""
        response = self.client.post(path='/login/', data={"username": "", "password": ""})
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码为空", login_html)

    def test_login_action_error(self):
        """用户名密码错误"""
        response = self.client.post(path='/login/', data={"username": "error", "password": "error"})
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码错误", login_html)

    def test_login_action_success(self):
        """用户名密码正确，登录成功"""
        response = self.client.post(path='/login/', data={"username": "test01", "password": "test123456"})
        self.assertEqual(response.status_code, 302)


class UserLogoutTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="test01", email="test01@mail.com", password="test123456")
        self.client = Client()
        self.client.post(path='/login/', data={"username": "test01", "password": "test123456"})

    def test_logout(self):
        response = self.client.post(path='/logout/')
        self.assertEqual(response.status_code, 302)
