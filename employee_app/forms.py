# employee_app/forms.py
from django import forms
from .models import Employee, Project, Department, EmpSkills

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class EmpSkillsForm(forms.ModelForm):
    class Meta:
        model = EmpSkills
        fields = '__all__'
