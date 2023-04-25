import json

from django.core.management.base import BaseCommand
from app.models import Employee


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('employees.json', 'rb') as file:
            data = json.load(file)
            for i in data:
                employee = Employee()
                employee.full_name = i['full_name']
                employee.position = i['position']
                employee.salary = i['salary']
                employee.age = i['age']
                employee.save()
                print(i['full_name'], i['position'])
