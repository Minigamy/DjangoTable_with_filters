import django_tables2 as tables
from .models import Durations



class DurationsTable(tables.Table):
    class Meta:
        model = Durations
        template_name = "django_tables2/bootstrap.html"
        fields = ("client", "equipment", "start", "stop", "mode_id", "minutes")
