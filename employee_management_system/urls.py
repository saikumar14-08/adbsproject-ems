"""
URL configuration for employee_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from employee_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('employee-list/', employee_list, name='employee_list'),
    path('project-list/', project_list, name='project_list'),
    path('department-list/', department_list, name='department_list'),
    path('emp-skills-list/', emp_skills_list, name='emp_skills_list'),
    path('employee-detail/', employee_detail, name='employee_detail'),
    #path('employee-detail-form/', employee_detail_form, name='employee_detail_form'),
    path('department-detail/', department_detail, name='department_detail'),
    path('skills-detail/', skills_detail, name='skills_detail'),
    path('add-employee/', add_employee, name='add_employee'),
    path('add-project/', add_project, name='add_project'),
    path('add-department/', add_department, name='add_department'),
    path('add-emp_skills/', add_emp_skills, name='add_emp_skills'),
]
