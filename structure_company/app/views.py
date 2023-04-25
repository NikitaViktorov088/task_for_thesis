from rest_framework import filters, permissions
from rest_framework_simplejwt import authentication
from .mixins import ListCreateDeleteViewSet, ListViewSet
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from .models import Department, Employee
from .serializers import DepartmentSerailizer, EmployeeSerializer


class EmployeeViewSet(ListCreateDeleteViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('department__id',)
    search_fields = ('full_name',)
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)


class DepartmentViewSet(ListViewSet):
    queryset = Department.objects.annotate(
        employees_count=models.Count('employees'),
        total_salary=models.Sum('employees__salary')
    ).all()
    serializer_class = DepartmentSerailizer
    pagination_class = None
