from django.db import models
from django.utils import timezone 
from datetime import datetime



class Employee(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200)
    dob = models.DateField()
    salary = models.IntegerField()
    hire_date = models.DateField()
    gender = models.CharField(max_length=1)
    department =  models.CharField(max_length=200)
    project_id = models.CharField(max_length=200, null=True,blank=True)
    def update_hire_date_trigger(self):
        # Your trigger logic here
        if self.hire_date > datetime.now().date():
            raise ValueError("Enter Valid Hire Date")
            
    def get_employee_projects(self):
        return Project.objects.filter(project_id=self.project_id)

    def get_employee_skills(self):
        return EmpSkills.objects.filter(emp_id=self.emp_id)
class Department(models.Model):
    dept_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200, unique = True)
    address = models.CharField(max_length=200)
    def get_department_employees(self):
        return Employee.objects.filter(department=self.name)

class EmpProject(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_id = models.CharField(max_length=255)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    def check_project_hours_trigger(self):
        # Your trigger logic here
        if self.hours < 0 or self.hours > 100:
            raise ValueError('Project hours must be between 0 and 100')
    def get_project_details(self):
        return Project.objects.get(project_id=self.project_id)

class Project(models.Model):
    project_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    def get_project_employees(self):
        return Employee.objects.filter(project_id=self.project_id)


class EmpSkills(models.Model):
    emp_id = models.CharField(max_length=50, null=True,blank=True)
    skill_id = models.CharField(max_length=50)
    skill_level = models.IntegerField()

    def check_employee_exists(self):
        try:
            Employee.objects.get(emp_id=self.emp_id)
        except ObjectDoesNotExist:
            raise ValueError('Employee with emp_id {} does not exist'.format(self.emp_id))

    def check_skill_level_trigger(self):
        # Your trigger logic here
        if self.skill_level < 1 or self.skill_level > 5:
            raise ValueError('Skill level must be between 1 and 5')

    def save(self, *args, **kwargs):
        self.check_employee_exists()
        self.check_skill_level_trigger()
        super().save(*args, **kwargs)
    
