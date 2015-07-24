import csv
from django.core.management.base import BaseCommand, CommandError
from socios.models import Socio


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        path = options['path']
        socios = []
        with open(path, 'rb') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['dni']:
                    socio = Socio(dni=row['dni'])
                    socios.append(socio)
        Socio.objects.bulk_create(socios)
        print ('Created {} socios.'.format(len(socios)))
