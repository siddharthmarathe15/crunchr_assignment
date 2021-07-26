import csv
from django.core.management.base import BaseCommand

from data_statistics.models import Company, Location, Employee


class Command(BaseCommand):
    help = 'Load dataset using csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Indicates the file path')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index != 0:
                    # Company object creation
                    company_name = row[9].strip()
                    company_obj, _ = Company.objects.get_or_create(name=company_name)

                    # Location object creation
                    continent = row[2].strip()
                    country = row[3].strip()
                    province = row[4].strip() if row[5] and row[4] else row[5].strip()
                    city = row[5].strip() if row[5] and row[4] else row[4].strip()
                    location_obj, _ = Location.objects.get_or_create(continent=continent,
                                                                     country=country,
                                                                     province=province,
                                                                     city=city)
                    if company_name not in location_obj.companies.values_list('name', flat=True):
                        location_obj.companies.add(company_obj)

                    # Employee object creation
                    first_name = row[7].strip()
                    last_name = row[8].strip()
                    job_title = row[1].strip().title()
                    age = round(float(row[6].strip()))
                    Employee.objects.get_or_create(first_name=first_name,
                                                   last_name=last_name,
                                                   job_title=job_title,
                                                   age=age,
                                                   location=location_obj,
                                                   company=company_obj)
                    
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
