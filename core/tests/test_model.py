from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_craete_user_with_successful(self):
        email = "test@example.com"
        password = "Test123#"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@EXAMPLE.COM"
        user = get_user_model().objects.create_user(email=email)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        password = "Test123#"

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser("test@example.com", "test123")

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
