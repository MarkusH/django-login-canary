from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.utils.translation import ugettext_lazy as _

from .notify import send_logged_in, send_login_failed


class LoginCanaryConfig(AppConfig):
    name = 'login_canary'
    verbose_name = _("Login Canary")

    def ready(self):
        user_logged_in.connect(send_logged_in)
        user_login_failed.connect(send_login_failed)
