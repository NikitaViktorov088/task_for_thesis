from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('departments', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
