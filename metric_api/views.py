from django.shortcuts import render
import prometheus_client
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("hello world")

def metrics(request):
    metrics_page = prometheus_client.generate_latest()
    return HttpResponse(
            metrics_page,
            content_type=prometheus_client.CONTENT_TYPE_LATEST)
