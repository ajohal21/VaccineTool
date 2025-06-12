from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.http import JsonResponse
import json

urlpatterns = [
    path('', RedirectView.as_view(url='list/', permanent=True)),
    path('list/', views.list_data, name='list_data'),
    path('api/vaccines/', views.vaccine_data_api, name='vaccine_data_api'),
    # We'll add our routes here later
] 

def vaccine_data_api(request):
    with open('data/vaccine_data.json', 'r') as f:
        data = json.load(f)
    return JsonResponse(data) 