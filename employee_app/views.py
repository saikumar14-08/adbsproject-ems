

# Create your views here.
# employee_app/views.py
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
def home(request):
    employees = Employee.objects.all()
    projects = Project.objects.all()
    departments = Department.objects.all()
    emp_skills = EmpSkills.objects.all()
    context = {
        'employees': employees,
        'projects': projects,
        'departments': departments,
        'emp_skills': emp_skills,
    }

    return render(request, 'home.html', context)
    #return render(request, 'home.html',{'employees': employees}, {'projects': projects}, {'departments': departments}, {'emp_skills': emp_skills})
"""def employee_detail(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        employee = get_object_or_404(Employee, emp_id=emp_id)

        # Fetch additional details (projects, skills, etc.) if needed
        projects = EmpProject.objects.filter(employee=employee)
        skills = EmpSkills.objects.filter(employee=employee)

        # Return details in JSON format
        data = {
            'employee_name': employee.name,
            'employee_email': employee.email,
            'employee_dob': str(employee.dob),
            'employee_salary': str(employee.salary),
            'projects': [{'project_id': project.id, 'project_name': project.name} for project in projects],
            'skills': [{'skill_id': skill.id, 'skill_name': skill.name} for skill in skills],
        }

        return JsonResponse(data)

    return render(request, 'employee_detail.html')"""
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})
def emp_skills_list(request):
    emp_skills = EmpSkills.objects.all()
    return render(request, 'emp_skills_list.html', {'emp_skills': emp_skills})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list page
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})

"""def employee_detail_form(request):
    return render(request, 'employee_detail_form.html')"""
def employee_detail(request):
    form_submitted = False
    employee = None
    projects = []
    skills = []

    if request.method == 'POST':
        form_submitted = True
        emp_id = request.POST.get('emp_id')
        employee = get_object_or_404(Employee, emp_id=emp_id)
        # Assuming you have appropriate methods to fetch projects and skills for the employee
        projects = employee.get_employee_projects()
        skills = employee.get_employee_skills()

    return render(request, 'employee_detail.html', {'employee': employee, 'projects': projects, 'skills': skills, 'form_submitted': form_submitted})

def department_detail(request):
    form_submitted = False
    department = None
    employees = []

    if request.method == 'POST':
        form_submitted = True
        dept_id = request.POST.get('dept_id')
        department = get_object_or_404(Department, dept_id=dept_id)
        employees = department.get_department_employees()

    return render(request, 'department_detail.html', {'department': department, 'employees': employees, 'form_submitted': form_submitted})

def skills_detail(request):
    form_submitted = False
    employee = []
    
    skills = []

    if request.method == 'POST':
        form_submitted = True
        emp_id = request.POST.get('emp_id')
        employee = get_object_or_404(Employee, emp_id=emp_id)
        skills = employee.get_employee_skills()
    return render(request, 'skills_detail.html', {'employee': employee, 'skills': skills, 'form_submitted': form_submitted})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirect to the project list page
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Redirect to the department list page
    else:
        form = DepartmentForm()

    return render(request, 'add_department.html', {'form': form})

def add_emp_skills(request):
    if request.method == 'POST':
        form = EmpSkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_skills_list')  # Redirect to the emp skills list page
    else:
        form = EmpSkillsForm()

    return render(request, 'add_emp_skills.html', {'form': form})
