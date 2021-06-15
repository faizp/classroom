from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Category, secCategory, Classroom, Day, ClassroomEnrolled, QuestionsQandA, ReplyQandA
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


def index(request):
    if request.user.is_authenticated:
        classrooms = Classroom.active_classrooms.filter(started=False).exclude(user=request.user)
    else:
        classrooms = Classroom.active_classrooms.filter(started=False)
    for classroom in classrooms:
        students = ClassroomEnrolled.objects.filter(classroom = classroom).count()
        if classroom.students <= students:
            classroom.full = True
        else:
            classroom.full = False
    context = {
        'classrooms': classrooms
    }
    return render(request, 'classrooms/index.html', context)


@login_required(login_url='login')
def create_classroom(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        title = request.POST.get('title')
        duration = request.POST.get('duration')
        language = request.POST.get('language')
        start_date = request.POST.get('start-date')
        student_number = request.POST.get('student-number')
        description = request.POST.get('description')
        category = request.session['secCategory']
        sec_category = secCategory.objects.get(id=category)
        classroom = Classroom.objects.create(user = request.user, sec_category=sec_category, title=title, students=student_number, language=language, start_date=start_date, duration=duration, description=description, video=video)
        return redirect('classroom-tutor', classroom.id)
    return render(request, 'classrooms/create-classroom.html')


@login_required(login_url='login')
def classroom_tutor(request, id):
    if Classroom.active_classrooms.get(id=id).user == request.user:
        classroom = Classroom.active_classrooms.get(id=id)
        context = {
            'classroom': classroom,
        }
        return render(request, 'classrooms/classroom-tutor.html', context)
    return redirect('classroom-student', id)

@login_required(login_url='login')
def manage_days(request, id):
    if Classroom.active_classrooms.filter(id=id).exists():
        classroom = Classroom.active_classrooms.get(id=id)
        days = Day.objects.filter(classroom=classroom)
        for day in days:
            if day.publishing_day <= datetime.now():
                day.publish = True
            else:
                day.publish = False
        context = {
            'classroom': classroom,
            'days': days,
           
        }
        return render(request, 'classrooms/manage-days.html', context)
    return redirect('index')


@login_required(login_url='login')
def add_day(request, id):
    if request.method == 'POST':
        video = request.FILES.get('video')
        title = request.POST.get('title')
        publishing_day = request.POST.get('datetime-field')    
        description = request.POST.get('description')
        classroom = Classroom.objects.get(pk=id)
        if publishing_day == "":
            Day.objects.create(classroom=classroom, video=video, video_title=title, description=description, publishing_day=datetime.now())
        else:
            Day.objects.create(classroom=classroom, video=video, video_title=title, description=description, publishing_day=publishing_day)
        classroom.started = True
        classroom.save()
        return redirect('manage-days',id)
    return render(request, 'classrooms/add-day.html')


@login_required(login_url='login')
def join_classroom(request, id):
    if Classroom.active_classrooms.get(id=id).user == request.user:
        return redirect('classroom-tutor',id)
    else:
        return redirect('classroom-student',id)


def classroom_student(request, id):
    classroom = Classroom.active_classrooms.get(id=id)
    if classroom.user != request.user:
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
    return redirect('classroom-tutor', id)


@login_required(login_url='login')
def my_classroom(request):
    classrooms_teaching = Classroom.objects.filter(user=request.user)
    for classroom in classrooms_teaching:
        if classroom.started:
            day_count = Day.objects.filter(classroom = classroom, publishing_day__lte=datetime.now()).count()
            classroom.status = day_count
        else:
            classroom.status = 'Not Started'
    classrooms_enrolled = ClassroomEnrolled.objects.filter(user=request.user)
    for classroom in classrooms_enrolled:
        if classroom.classroom.started:
            day_count = Day.objects.filter(classroom=classroom.classroom, publishing_day__lte=datetime.now()).count()
            classroom.classroom.status= day_count
        else:
            classroom.classroom.status = 'Not Started'
    print(classrooms_enrolled)
    
    context = {
        'classrooms_teaching': classrooms_teaching,
        'classrooms_enrolled': classrooms_enrolled
    }
    return render(request, 'classrooms/myclassroom.html', context)


@login_required(login_url='login')
def enroll_classroom(request, id):
    user = request.user
    classroom = Classroom.active_classrooms.get(id=id)
    ClassroomEnrolled.objects.create(user=user, classroom=classroom)
    return redirect('classroom-student', id)


@login_required(login_url='login')
def content(request, id):
    if Classroom.active_classrooms.filter(id=id).exists():
        classroom = Classroom.active_classrooms.get(id=id)
        content = Day.objects.filter(classroom = classroom, publishing_day__lte=datetime.now()).last()
        questions = QuestionsQandA.objects.filter(classroom=classroom).order_by('-pk')
        answers = ReplyQandA.objects.filter(classroom=classroom).order_by('-pk')
        context = {
            'content': content,
            'questions': questions,
            'answers': answers
        }
        return render(request, 'classrooms/days-content.html', context)
    return redirect('index')


@login_required(login_url='login')
def manage_students(request, id):
    classroom = Classroom.active_classrooms.get(id=id)
    students = ClassroomEnrolled.objects.filter(classroom=classroom)
    context = {
        'students': students,
        'classroom': classroom,
    }
    return render(request, 'classrooms/manage-students.html', context)


@login_required(login_url='login')
def remove_student(request, c_id, u_id):
    classroom = Classroom.active_classrooms.get(id=c_id)
    user = User.objects.get(id=u_id)
    student = ClassroomEnrolled.objects.get(classroom=classroom, user=user)
    student.delete()
    return redirect('manage-students', c_id)


@login_required(login_url='login')
def publish_day(request, id):
    day = Day.objects.get(id=id)
    day.publish = True
    day.save()
    return redirect('manage-days', day.classroom.id)


def delete_content(request, id):
    day = Day.objects.get(id=id)
    day.delete()
    return redirect('manage-days', day.classroom.id)


def ask_question(request, id):
    classroom = Classroom.objects.get(id=id)
    question = request.POST.get('question')
    QuestionsQandA.objects.create(classroom=classroom, question=question, user=request.user)
    return redirect('content', id)


def answer_question(request, id):
    question = QuestionsQandA.objects.get(id=id)
    answer = request.POST.get('answer')
    ReplyQandA.objects.create(question=question, classroom=question.classroom, answer=answer, user=request.user)
    return redirect('content', question.classroom.id)


def q_and_a(request, id):
    classroom = Classroom.objects.get(id=id)
    questions = QuestionsQandA.objects.filter(classroom=classroom).order_by('-pk')
    answers = ReplyQandA.objects.filter(classroom=classroom).order_by('-pk')
    context = {
        'classroom': classroom,
        'questions': questions,
        'answers': answers
    }
    return render(request, 'classrooms/qanda.html', context)


def ask_question_tutor(request, id):
    classroom = Classroom.objects.get(id=id)
    question = request.POST.get('question')
    QuestionsQandA.objects.create(classroom=classroom, question=question, user=request.user)
    return redirect('q-and-a', id)


def answer_question_tutor(request, id):
    question = QuestionsQandA.objects.get(id=id)
    answer = request.POST.get('answer')
    ReplyQandA.objects.create(question=question, classroom=question.classroom, answer=answer, user=request.user)
    return redirect('q-and-a', question.classroom.id)
    

def delete_question_tutor(request, id):
    question = QuestionsQandA.objects.get(id=id)
    question.delete()
    return redirect('q-and-a', question.classroom.id)


def delete_answer_tutor(request, id):
    answer = ReplyQandA.objects.get(id=id)
    answer.delete()
    return redirect('q-and-a', answer.classroom.id)


def delete_question(request, id):
    question = QuestionsQandA.objects.get(id=id)
    question.delete()
    return redirect('content', question.classroom.id)


def delete_answer(request, id):
    answer = ReplyQandA.objects.get(id=id)
    answer.delete()
    return redirect('content', answer.classroom.id)

 