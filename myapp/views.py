from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

# Read all employee records
def read(request):
    employees = Employee.objects.all()
    return render(request, 'read.html', {'employees': employees})

# Create a new employee
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        join_date = request.POST.get('join_date')
        photo = request.FILES.get('photo')

        Employee.objects.create(
            name=name,
            department=department,
            join_date=join_date,
            photo=photo
        )
        return redirect('read')  

    return render(request, 'create.html')  

# Update an employee
def update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.department = request.POST.get('department')
        employee.join_date = request.POST.get('join_date')
        if 'photo' in request.FILES:
            employee.photo = request.FILES['photo']

        employee.save()
        return redirect('read')

    return render(request, 'update.html', {'employee': employee})

# Delete an employee
def delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('read')
    return render(request, 'delete.html', {'employee': employee})
