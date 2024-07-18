
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Employee, Attendance, Leave

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')

# @login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# @login_required
def dashboard(request):
    # user = request.user
    # employee = Employee.objects.get(user=user)
    return render(request, 'dashboard.html')

# @login_required
def mark_attendance(request):
    if request.method == 'POST':
        # Assuming we have a form to mark attendance with employee ID and check-in time
        employee_id = request.POST['employee_id']
        check_in_time = request.POST['check_in_time']
        # Retrieve the employee
        employee = Employee.objects.get(pk=employee_id)
        # Create attendance entry
        Attendance.objects.create(employee=employee, check_in=check_in_time)
        return redirect('dashboard')
    return render(request, 'mark_attendance.html')

# @login_required
def apply_leave(request):
    if request.method == 'POST':
        # Assuming we have a form to apply for leave with start date, end date, and reason
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reason = request.POST['reason']
        # Create leave request
        Leave.objects.create(employee=request.user.employee, start_date=start_date, end_date=end_date, reason=reason)
        return redirect('dashboard')
    return render(request, 'apply_leave.html')
