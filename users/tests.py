from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.test import TestCase

from users.forms import CustomUserCreationForm
from users.views import SignUpView


class CutomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='user@test.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'user@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='testsuperuser',
            email='superuser@test.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testsuperuser')
        self.assertEqual(user.email, 'superuser@test.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('users:signup')
        self.response = self.client.get(url)

    def test_signup_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        print(view)
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)
