from .models import Inspection
from django_filters import FilterSet, NumberFilter, CharFilter


class InspectionFilter(FilterSet):

    class Meta:
        model = Inspection
        #fields = ['project_number', 'owner']
        fields = {
            'project_number': ['contains'],
            'client': ['exact'],
            'title': ['contains'],
        }

class InspectionTitleFilter(FilterSet):
    class Meta:
        model = Inspection
        # fields = ['project_number', 'owner']
        fields = {
            'project_number': ['contains'],
            'title': ['contains'],
        }