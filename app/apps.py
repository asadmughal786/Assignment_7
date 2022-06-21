from django.apps import AppConfig
from django.core.signals import request_finished


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from . import signals
        from .models import Profile
        # request_finished.connect(signals.post_save)
        # request_finished.connect(signals.pre_delete)
        signals.post_save.connect(signals.create_profile, sender=Profile)
        # signals.post_save.connect(signals.save_profile, sender=Profile)
        
