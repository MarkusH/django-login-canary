from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.test.signals import setting_changed
from django.test.utils import override_settings


def update_login_canary_settings(**kwargs):
    setting = kwargs['setting']
    if setting.startswith('LOGIN_CANARY_'):
        from login_canary import settings
        setting = setting[13:]
        setattr(settings, setting, kwargs['value'])

setting_changed.connect(update_login_canary_settings)


class LoggedInTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            'user', 'user@example.com', 'password',
        )

    def test_user_login(self):
        self.assertEqual(len(mail.outbox), 0)
        self.client.login(username='user', password='password')
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.subject, 'Successful login on Test Service')
        self.assertIn('Dear user,\n', message.body)
        self.assertIn(
            'somebody successfully logged in to your account on Test Service.\n',
            message.body,
        )
        self.assertEqual(message.to, [self.user.email])

    @override_settings(LOGIN_CANARY_NOTIFY_LOGGED_IN=True)
    def test_user_login_active(self):
        self.assertEqual(len(mail.outbox), 0)
        self.client.login(username='user', password='password')
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.subject, 'Successful login on Test Service')
        self.assertIn('Dear user,\n', message.body)
        self.assertIn(
            'somebody successfully logged in to your account on Test Service.\n',
            message.body,
        )
        self.assertEqual(message.to, [self.user.email])

    @override_settings(LOGIN_CANARY_NOTIFY_LOGGED_IN=False)
    def test_user_login_inactive(self):
        self.assertEqual(len(mail.outbox), 0)
        self.client.login(username='user', password='password')
        self.assertEqual(len(mail.outbox), 0)


class LoginFailedTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            'user', 'user@example.com', 'password',
        )

    def test_login_failed(self):
        self.assertEqual(len(mail.outbox), 0)
        self.client.login(username='user', password='wrong')
        self.assertEqual(len(mail.outbox), 0)

    @override_settings(LOGIN_CANARY_NOTIFY_LOGIN_FAILED=True)
    def test_login_failed_active(self):
        self.assertEqual(len(mail.outbox), 0)
        self.client.login(username='user', password='wrong')
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.subject, 'Failed login attempt on Test Service')
        self.assertIn('Dear user,\n', message.body)
        self.assertIn(
            'somebody tried to login to your account on Test Service but '
            'provided invalid credentials.\n',
            message.body,
        )
        self.assertEqual(message.to, [self.user.email])

    @override_settings(LOGIN_CANARY_NOTIFY_LOGIN_FAILED=False)
    def test_login_failed_inactive(self):
        self.assertEqual(len(mail.outbox), 0)
        self.client.login(username='user', password='wrong')
        self.assertEqual(len(mail.outbox), 0)

    @override_settings(LOGIN_CANARY_NOTIFY_LOGIN_FAILED=True)
    def test_login_failed_unknwon_user(self):
        self.assertEqual(len(mail.outbox), 0)
        self.client.login(username='unknown', password='wrong')
        self.assertEqual(len(mail.outbox), 0)
