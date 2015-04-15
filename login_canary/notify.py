from django.contrib.auth import get_user_model
from django.template import loader

from . import settings


def send_mail(user, subject_template_name, body_template_name, **additional_context):
    context = {
        'service_name': settings.SERVICE_NAME,
        'user': user,
    }
    context.update(**additional_context)
    subject = loader.render_to_string(subject_template_name, context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    body = loader.render_to_string(body_template_name, context)
    user.email_user(subject, body)


def send_logged_in(sender, user, **kwargs):
    if settings.NOTIFY_LOGGED_IN:
        send_mail(
            user=user,
            subject_template_name='login_canary/logged_in_subject.txt',
            body_template_name='login_canary/logged_in_body.txt',
            **kwargs
        )


def send_login_failed(sender, credentials, **kwargs):
    if settings.NOTIFY_LOGIN_FAILED:
        UserModel = get_user_model()
        username = credentials.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            pass
        else:
            send_mail(
                user=user,
                subject_template_name='login_canary/login_failed_subject.txt',
                body_template_name='login_canary/login_failed_body.txt',
            )
