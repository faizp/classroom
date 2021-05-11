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
    print(categories)
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
    print(correct_answer)
    data = {
        'answers': serializers.serialize('json', answers),
        'correctAnswer': serializers.serialize('json', correct_answer)
    }
    return JsonResponse(data)
