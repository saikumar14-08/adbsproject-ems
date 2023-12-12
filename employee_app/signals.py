# signals.py

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Employee, EmpProject, EmpSkills

@receiver(pre_save, sender=Employee)
def update_hire_date(sender, instance, **kwargs):
    instance.update_hire_date_trigger()

@receiver(pre_save, sender=EmpProject)
def check_project_hours(sender, instance, **kwargs):
    instance.check_project_hours_trigger()

@receiver(pre_save, sender=EmpSkills)
def emp_skills_pre_save(sender, instance, **kwargs):
    """
    Signal handler for pre-save operations on EmpSkills model.
    """
    instance.check_employee_exists()
    instance.check_skill_level_trigger()
