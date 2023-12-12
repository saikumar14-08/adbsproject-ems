# employee_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('employee-list/', employee_list, name='employee_list'),
    path('project-list/', project_list, name='project_list'),
    path('add-employee/', add_employee, name='add_employee'),
    path('employee/<str:emp_id>/', employee_detail, name='employee_detail'),
]
