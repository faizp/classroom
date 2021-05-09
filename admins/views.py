from django.shortcuts import render, redirect
from django.http import JsonResponse
from classrooms.forms import CategoryForm

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
    return render(request, 'admins/admin-index.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            return redirect('add-category')
    form = CategoryForm()
    return render(request, 'admins/add-category.html', {'form': form})