import django_filters
from django_filters import DateTimeFilter, RangeFilter, TimeFilter, DurationFilter

from .models import *


class DurationsFilter(django_filters.FilterSet):
    start = DateTimeFilter(field_name='start', lookup_expr='gte', label='Start datetime')
    stop = DateTimeFilter(field_name='stop', lookup_expr='lte', label='Stop datetime')
    minutes = RangeFilter(field_name='minutes')

    class Meta:
        model = Durations
        fields = '__all__'
        exclude = ['minutes', 'start', 'stop']
