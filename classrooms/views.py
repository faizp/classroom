from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Category, secCategory, Questions, Answer, TestPassed, Classroom, Day
from random import sample
from django.core import serializers
import json


# Create your views here.
def index(request):
    classrooms = Classroom.objects.all()
    context = {
        'classrooms': classrooms
    }
    return render(request, 'classrooms/index.html', context)


@login_required
def teach(request):
    if request.method == 'POST':
        category = request.POST['category']
        sec_category = secCategory.objects.get(id=category)
        if TestPassed.objects.filter(sec_category=sec_category, user=request.user).exists():
            return JsonResponse('passed', safe=False)
        if Questions.objects.filter(sec_category=sec_category).exists():
            request.session['secCategory'] = category
            return JsonResponse('true', safe=False)
        return JsonResponse('false', safe=False)
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'classrooms/teach.html', context)


@login_required
def test(request):
    if request.method == 'GET':
        category = request.session['secCategory']
        sec_category = secCategory.objects.get(id=category)
        items = Questions.objects.filter(sec_category = sec_category) 
        if len(items) >= 5:
            a = 5
        else:
            a = len(items)
        questions = sample(list(items), a)
        request.session['questions'] = serializers.serialize('json', questions)
        print(questions)
        
        answers = []
        for question in questions:
            answer = Answer.objects.filter(question=question)
            answers.append(answer)
        context = {
            'questions': questions,
            'answers': answers
        }
        return render(request, 'classrooms/test.html', context)
    if request.method == 'POST':
        q = request.session['questions']
        questions = json.loads(q)
        print(questions)
        passed = True
        for i in range(len(questions)):
            a = questions[i]
            answer = Answer.objects.get(question=str(a['pk']), correct='true')
            b = request.POST.get(str(a['pk']))
            if b != str(answer.id):
                passed = False
        print(passed)
        if passed:
            return redirect('test-passed')
        return redirect('test-failed')
    


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
    context = {
        'classroom': classroom
    }
    return render(request, 'classrooms/classroom-student.html', context)


def test_passed(request):
    return render(request, 'classrooms/test-passed.html')


def test_failed(request):
    return render(request, 'classrooms/test-failed.html')