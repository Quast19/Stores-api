from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
# Create your views here.
@api_view(["POST","GET"])
def trigger(request, *args, **kwargs):
    return Response("The report generation has be triggered...")

def give_report(request, *args, **kwargs):
    return Response("Will return the report if needed")

