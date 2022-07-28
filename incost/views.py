from .models import Durations
from django_tables2 import SingleTableView

from .tables import DurationsTable

from .filters import DurationsFilter


class DurationsListView(SingleTableView):
    model = Durations
    table_class = DurationsTable
    template_name = 'incost/table.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        myFilter = DurationsFilter(self.request.GET, queryset)
        return myFilter.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        myFilter = DurationsFilter(self.request.GET, queryset)
        context['myFilter'] = myFilter
        return context




