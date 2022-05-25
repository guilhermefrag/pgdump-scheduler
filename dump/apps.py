from django.apps import AppConfig
from .jobs import run

class TerminalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dump'
    
    def ready(self):
        run.start()
