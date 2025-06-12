from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='list/', permanent=True)),
    path('list/', views.list_data, name='list_data'),
    # We'll add our routes here later
] 