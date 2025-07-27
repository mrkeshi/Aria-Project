from django.apps import AppConfig


class WorkspaceModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workspace_module'
    def ready(self):
        import workspace_module.signals.handlers
