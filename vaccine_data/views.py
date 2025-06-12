from django.shortcuts import render
import zipfile
import json
from django.db import transaction
from .models import Country, Vaccine
from bs4 import BeautifulSoup
import os
from django.http import HttpResponse



def list_data(request):
    """Read data from JSON file and display"""
    try:
        with open('data/vaccine_data.json', 'r') as f:
            data = json.load(f)
        return render(request, 'vaccine_data/list_data.html', {'data': data})
    except FileNotFoundError:
        return HttpResponse("Please run the data extraction script first.")