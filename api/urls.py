
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('trigger_report/',views.trigger),
    path('get_report/', views.give_report),
]
