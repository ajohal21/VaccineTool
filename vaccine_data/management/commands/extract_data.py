from django.core.management.base import BaseCommand
from vaccine_data.views import extract_data_to_json

class Command(BaseCommand):
    help = 'Extract vaccine data from HTML files and save to JSON'

    def handle(self, *args, **options):
        self.stdout.write('Starting data extraction...')
        extract_data_to_json()
        self.stdout.write(self.style.SUCCESS('Successfully extracted data to JSON')) 