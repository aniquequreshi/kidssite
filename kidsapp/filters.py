import django_filters
from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.widgets import RangeWidget

from .models import Denial

class DenialFilter(FilterSet):
    follow_up_date = django_filters.DateFromToRangeFilter()
    # follow_up_date__lt = django_filters.Da


    # Works, but don't need it
    # o = django_filters.OrderingFilter(
    #     choices=(
    #         ('date_of_service', 'Date of Service'),
    #         ('carrier', 'Carrier'),
    #         ('code', 'Code'),
    #         ('status', 'Status'),
    #     ),
    #     fields={
    #         ('date_of_service', 'Date of Service'),
    #         ('carrier', 'Carrier'),
    #         ('code', 'Code'),
    #         ('status', 'Status'),
    #     },
    # )

    # def get_queryset(self):
    #     qs = self.model.objects.none()
    #     denial_filtered_list = DenialFilter(self.request.GET, queryset=qs)
    #     return denial_filtered_list.qs

    class Meta:
        model = Denial
        fields = ['status', 'carrier', 'follow_up_date', 'reason_code', 'visit_id' ]
        follow_up_date_range = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))
        # order_by_field = 'date_of_service'  GOOD

