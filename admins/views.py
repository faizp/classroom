from django.shortcuts import render, redirect
from django.http import JsonResponse
from classrooms.forms import CategoryForm
from classrooms.models import Category, secCategory, Questions, Answer
from django.core import serializers


# Create your views here.
def admin_login(request):
    if request.method == 'POST' :
         if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username == 'admin' and password == 'admin':
                request.session['password'] = password
                return JsonResponse('true', safe=False)
            else:
                return JsonResponse('false', safe=False)
    return render(request, 'admins/admin-login.html')

def admin_home(request):
    return render(request, 'admins/dashboard.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('add-category')

    form = CategoryForm()
    categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'admins/category.html', context)


def sec_category(request):
    if request.method == 'POST':
        category = request.POST['category']
        category_selected = Category.objects.get(id=category)
        result_category = secCategory.objects.filter(category=category_selected)
        cateogories = serializers.serialize('json', result_category)
        data = {
            'categories': cateogories
        }
        return JsonResponse(data)
    return JsonResponse('false', safe=False)


def instructor_test(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'admins/instructor-test.html', context)


def category_test(request, id):
    category = Category.objects.get(id=id)
    categories = secCategory.objects.filter(category=category)
    context = {
        'categories': categories
    }
    return render(request, 'admins/category-test.html', context)


def questions(request, id):
    sec_category = secCategory.objects.get(id=id)
    questions = Questions.objects.filter(sec_category=sec_category)
    if questions == None:
        return JsonResponse('false', safe=False)
    data = {
        'questions': serializers.serialize('json', questions)
    }
    return JsonResponse(data)


def answers(request, id):
    question = Questions.objects.get(id=id)
    answers = Answer.objects.filter(question=question)
    correct_answer = Answer.objects.filter(question=question, correct=True)
    data = {
        'answers': serializers.serialize('json', answers),
        'correctAnswer': serializers.serialize('json', correct_answer)
    }
    return JsonResponse(data)


def add_question(request):
    if request.method == 'POST':
        sub_category = request.POST['subCategory']
        question1 = request.POST['question1']
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        answer3 = request.POST['answer3']
        answer4 = request.POST['answer4']
        answeropt1 = request.POST['answeropt1']
        if answeropt1 == 'true':
            answeropt1 = True
        else:
            answeropt1 = False
        answeropt2 = request.POST['answeropt2']
        if answeropt2 == 'true':
            answeropt2 = True
        else:
            answeropt2 = False
        answeropt3 = request.POST['answeropt3']
        if answeropt3 == 'true':
            answeropt3 = True
        else:
            answeropt3 = False
        answeropt4 = request.POST['answeropt4']
        if answeropt4 == 'true':
            answeropt4 = True
        else:
            answeropt4 = False
        count = 0
        lis = [answeropt1, answeropt2, answeropt3, answeropt4]
        for i in range(len(lis)):
            if lis[i] == 'true':
                count += 1
        if count>1:
            return JsonResponse('false', safe=False)
        sec_category = secCategory.objects.get(id=sub_category)
        question_created = Questions.objects.create(sec_category=sec_category, question=question1)
        Answer.objects.create(question=question_created, answer=answer1, correct=answeropt1)
        Answer.objects.create(question=question_created, answer=answer2, correct=answeropt2)
        Answer.objects.create(question=question_created, answer=answer3, correct=answeropt3)
        Answer.objects.create(question=question_created, answer=answer4, correct=answeropt4)
        return JsonResponse('true', safe=False)
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'admins/add-question.html', context)


def choose_category(request):
    if request.method == 'POST':
        category = request.POST['category']
        sec_categories = secCategory.objects.filter(category=category)
        data = {
            'categories': serializers.serialize('json', sec_categories)
        }
        return JsonResponse(data)
    return JsonResponse('false', safe=False)
        