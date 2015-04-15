===================
django-login-canary
===================

**django-login-canary** is a reusable Django application to notify users upon successful and failed logins.

License
=======

MIT


Installation
============

1. Install from PyPI::

    pip install django-login-canary

2. Add ``'login_canary'`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        # ...
        'login_canary',
    ]


Configuration
=============

``LOGIN_CANARY_NOTIFY_FAILED_LOGIN``
------------------------------------

Notify users upon failed logins. Use with caution!

Default: ``False``


``LOGIN_CANARY_NOTIFY_LOGIN``
-----------------------------

Notify users upon successful logins.

Default: ``True``


``LOGIN_CANARY_SERVICE_NAME``
-----------------------------

The name of your service. Required. String
