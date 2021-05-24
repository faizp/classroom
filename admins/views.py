from django.shortcuts import render, redirect
from django.http import JsonResponse
from classrooms.forms import CategoryForm
from classrooms.models import Category, secCategory, Classroom, Day
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


def add_sec_category(request):
    if request.method == 'POST':
        category_chosed = request.POST.get('chosed-category')
        sec_category = request.POST.get('sec-category')
        category = Category.objects.get(id=category_chosed)
        secCategory.objects.create(category=category, name=sec_category)
        return redirect('add-category')
    return redirect('add-category')


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


def choose_category(request):
    if request.method == 'POST':
        category = request.POST['category']
        sec_categories = secCategory.objects.filter(category=category)
        data = {
            'categories': serializers.serialize('json', sec_categories)
        }
        return JsonResponse(data)
    return JsonResponse('false', safe=False)


def manage_classroom(request):
    if request.method == 'POST':
        categories = Category.objects.all()
        id = request.POST.get('sub-category')
        sec_category = secCategory.objects.get(id=id)
        classrooms = Classroom.objects.filter(sec_category=sec_category)
        for classroom in classrooms:
            if classroom.started:
                day_count = Day.objects.filter(classroom = classroom, publish = True).count()
                classroom.status = day_count
            else:
                classroom.status = 'Not Started'
                
        context = {
            'classrooms': classrooms,
            'categories': categories
        }
        return render(request, 'admins/manage-classrooms.html', context)

    categories = Category.objects.all()
    classrooms = Classroom.objects.all()
    for classroom in classrooms:
        if classroom.started:
            day_count = Day.objects.filter(classroom = classroom, publish = True).count()
            classroom.status = day_count
        else:
            classroom.status = 'Not Started'

    context = {
        'classrooms': classrooms,
        'categories': categories
    }
    return render(request, 'admins/manage-classrooms.html', context)
        

def delete_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    classroom.delete()
    return redirect('manage-classrooms')


def block_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    classroom.is_active = False
    classroom.save()
    return redirect('manage-classrooms')


def unblock_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    classroom.is_active = True
    classroom.save()
    return redirect('manage-classrooms')