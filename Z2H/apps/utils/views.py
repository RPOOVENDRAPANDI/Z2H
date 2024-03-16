from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import State, District
from .serializers import StateSerializer, DistrictSerializer

# Create your views here.

class StateView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class DistrictView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = '[0-9a-f-]{36}'

    def get_queryset(self):
        return District.objects.filter(state__uid=self.kwargs['state_uid'])


