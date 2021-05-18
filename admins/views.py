from django.shortcuts import render, redirect
from django.http import JsonResponse
from classrooms.forms import CategoryForm
from classrooms.models import Category, secCategory
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





def choose_category(request):
    if request.method == 'POST':
        category = request.POST['category']
        sec_categories = secCategory.objects.filter(category=category)
        data = {
            'categories': serializers.serialize('json', sec_categories)
        }
        return JsonResponse(data)
    return JsonResponse('false', safe=False)
        