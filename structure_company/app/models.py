from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(
        upload_to='employee_photos/',
        null=True, blank=True
    )
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        related_name='employees',
        null=True
    )

    def __str__(self):
        return self.full_name


class Department(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='department_director'
    )

    def __str__(self):
        return self.name
