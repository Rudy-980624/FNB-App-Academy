from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_noop as _noop
from django.utils.translation import gettext as _
_  # noqa: F401, E402


class SurveysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'surveys'

    verbose_name = _noop('Surveys')
    label = 'surveys'
    verbose_name_plural = _('Surveys')
    def ready(self):
        from . import signals  # noqa: F401, E402
        from . import handlers  # noqa: F401, E402
        from . import tasks  # noqa: F401, E402
        from . import hooks  # noqa: F401, E402
        from . import utils  # noqa: F401, E402
        from . import views  # noqa: F401, E402
        from . import urls  # noqa: F401, E402
        from . import models  # noqa: F401, E402
        from . import admin  # noqa: F401, E402
        from . import forms  # noqa: F401, E402
        from . import migrations  # noqa: F401, E402
        from . import tests  # noqa: F401, E402
        from . import management  # noqa: F401, E402
        from . import api  # noqa: F401, E402
        
