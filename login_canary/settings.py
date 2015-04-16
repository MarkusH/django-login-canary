from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

NOTIFY_LOGGED_IN = getattr(settings, 'LOGIN_CANARY_NOTIFY_LOGGED_IN', True)

NOTIFY_LOGIN_FAILED = getattr(settings, 'LOGIN_CANARY_NOTIFY_LOGIN_FAILED', False)

SERVICE_NAME = getattr(settings, 'LOGIN_CANARY_SERVICE_NAME')
if SERVICE_NAME is None:  # pragma: no cover
    raise ImproperlyConfigured('You need to set LOGIN_CANARY_SERVICE_NAME.')
