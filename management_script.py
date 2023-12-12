# management_script.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "employee_management_system.settings")
django.setup()

from employee_app.models import Employee, EmpProject, Project, Department, EmpSkills

# Your management tasks here
