from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "jenkins_tutorial.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import jenkins_tutorial.users.signals  # noqa F401
        except ImportError:
            pass
