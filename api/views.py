from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from . import models
# Create your views here.
@api_view(["POST","GET"])
def trigger(request, *args, **kwargs):
    all_records = offset.objects.all()
    a = 10
    for i in all_records:
        print(all_records.store_id)
        a = a - 1
        if(a < 0):
            break
    return Response("The report generation has be triggered...")

def give_report(request, *args, **kwargs):
    return Response("Will return the report if needed")

