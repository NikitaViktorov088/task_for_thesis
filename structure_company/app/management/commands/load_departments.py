import json

from django.core.management.base import BaseCommand
from app.models import Department


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('departments.json', 'rb') as file:
            data = json.load(file)
            for i in data:
                department = Department()
                department.name = i['name']
                department.save()
                print(i['name'])
