from rest_framework import serializers

from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'full_name',
            'photo',
            'position',
            'salary',
            'age',
            'department'
        )


class DepartmentSerailizer(serializers.ModelSerializer):
    total_salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    employees_count = serializers.IntegerField()

    class Meta:
        model = Department
        fields = ('id', 'name', 'director', 'employees_count', 'total_salary')
