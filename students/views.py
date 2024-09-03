from django.shortcuts import render
from .models import Student, Course

def student_list(request):
    students = Student.objects.select_related('school').all()
    return render(request, 'students/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.select_related('teacher__school').prefetch_related('students').all()
    return render(request, 'students/course_list.html', {'courses': courses})
