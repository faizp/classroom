from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Category, secCategory, Classroom, Day, ClassroomEnrolled


def index(request):
    classrooms = Classroom.objects.all()
    context = {
        'classrooms': classrooms
    }
    return render(request, 'classrooms/index.html', context)


@login_required
def create_classroom(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        title = request.POST.get('title')
        duration = request.POST.get('duration')
        language = request.POST.get('language')
        start_date = request.POST.get('start-date')
        student_number = request.POST.get('student-number')
        description = request.POST.get('description')
        print(video, title, duration, language, start_date, student_number, description)
        category = request.session['secCategory']
        sec_category = secCategory.objects.get(id=category)
        classroom = Classroom.objects.create(user = request.user, sec_category=sec_category, title=title, students=student_number, language=language, start_date=start_date, duration=duration, description=description, video=video)
        return redirect('classroom-tutor', classroom.id)
    return render(request, 'classrooms/create-classroom.html')


@login_required
def classroom_tutor(request, id):
    classroom = Classroom.objects.get(id=id)
    context = {
        'classroom': classroom
    }
    return render(request, 'classrooms/classroom-tutor.html', context)


@login_required
def manage_days(request, id):
    classroom = Classroom.objects.get(id=id)
    days = Day.objects.filter(classroom=classroom)
    context = {
        'classroom': classroom,
        'days': days
    }
    return render(request, 'classrooms/manage-days.html', context)


@login_required
def add_day(request, id):
    if request.method == 'POST':
        video = request.FILES.get('video')
        title = request.POST.get('title')
        description = request.POST.get('description')
        classroom = Classroom.objects.get(pk=id)
        Day.objects.create(classroom=classroom, video=video, video_title=title, description=description)
        return redirect('manage-days',id)
    return render(request, 'classrooms/add-day.html')


@login_required
def join_classroom(request, id):
    if Classroom.objects.get(id=id).user == request.user:
        return redirect('classroom-tutor',id)
    else:
        return redirect('classroom-student',id)


def classroom_student(request, id):
    classroom = Classroom.objects.get(id=id)
    if ClassroomEnrolled.objects.filter(user=request.user, classroom=classroom).exists():
        classroom.classroom_status = 'enrolled'
    else:
        classroom.classroom_status = 'enroll'
    classroom_enrolled = ClassroomEnrolled.objects.filter(classroom=classroom).count()
    classroom.seats_left = classroom.students - classroom_enrolled
    context = {
        'classroom': classroom
    }
    return render(request, 'classrooms/classroom-student.html', context)


def my_classroom(request):
    classrooms_teaching = Classroom.objects.filter(user=request.user)
    classrooms_enrolled = ClassroomEnrolled.objects.filter(user=request.user)
    context = {
        'classrooms_teaching': classrooms_teaching,
        'classrooms_enrolled': classrooms_enrolled
    }
    return render(request, 'classrooms/myclassroom.html', context)


def enroll_classroom(request, id):
    user = request.user
    classroom = Classroom.objects.get(id=id)
    ClassroomEnrolled.objects.create(user=user, classroom=classroom)
    return redirect('classroom-student', id)