from django.contrib import admin
from .models import Department, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'full_name',
                    'position',
                    'salary',
                    'age',
                    'department'
                    )
    list_filter = ('department',)
    search_fields = ('full_name', 'position')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')
    search_fields = ('name', 'director__name')
