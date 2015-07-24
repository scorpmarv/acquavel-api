import csv
from django.core.management.base import BaseCommand, CommandError
from socios.models import Plan


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        path = options['path']
        planes = []
        with open(path, 'rb') as f:
            reader = csv.DictReader(f)
            for row in reader:
                desc_lower = row['descripcion_concepto'].lower()
                if row['tipo'] == 'S' or 'promo' in desc_lower or 'curso' in desc_lower:
                    plan = Plan(id=int(float(row['concepto'])), descripcion=row['descripcion_concepto'],
                                cant_clases=int(float(row['cantidad_clases'])))
                    planes.append(plan)
        Plan.objects.bulk_create(planes)
        print ('Created {} planes.'.format(len(planes)))

