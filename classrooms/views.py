from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Category, secCategory, Questions, Answer, TestPassed, Classroom

# Create your views here.
def index(request):
    return render(request, 'classrooms/index.html')


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


def test(request):
    if request.session.has_key('secCategory'):
        category = request.session['secCategory']
        sec_category = secCategory.objects.get(id=category)
        questions = Questions.objects.filter(sec_category = sec_category)[:1]
        answers = []
        for question in questions:
            answer = Answer.objects.filter(question=question)
            answers.append(answer)
        context = {
            'questions': questions,
            'answers': answers
        }
    return render(request, 'classrooms/test.html', context)


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


def classroom_tutor(request, id):
    classroom = Classroom.objects.get(id=id)
    context = {
        'classroom': classroom
    }
    return render(request, 'classrooms/classroom-tutor.html', context)


def manage_days(request):
    return render(request, 'classrooms/manage-days.html')