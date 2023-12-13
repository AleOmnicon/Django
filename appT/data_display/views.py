from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
import pandas as pd
from django.utils import timezone
import os
from django.templatetags.static import static

from .models import RawData

# Create your views here.

class IndexView(generic.ListView):
    template_name = "data_display/index.html"
    context_object_name = "rawData"

    data = RawData.objects.all()[:5]
    file = open("static/data_display/raw_data.csv")
    file.close()

    # if len(data) == 0:
    #     allData = pd.read_csv(static('data_display/rawData.csv'), delimiter=';')
    #     allData['dateTime'] = pd.to_datetime(allData['dateTime'])
    #     for item in allData.values:
    #         TimeSeries.objects.create(dateTime=item[0], value=item[1])
    
    def get_queryset(self) -> QuerySet[Any]:
        return RawData.objects.all()[:10]


