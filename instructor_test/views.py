from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from random import sample
from .models import Questions, Answer, TestPassed
from classrooms.models import Category, secCategory
from django.http import JsonResponse


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
    return render(request, 'instructor-test/teach.html', context)


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
        return render(request, 'instructor-test/test.html', context)

    if request.method == 'POST':
        q = request.session['questions']
        questions = json.loads(q)
        passed = True
        for i in range(len(questions)):
            a = questions[i]
            answer = Answer.objects.get(question=str(a['pk']), correct='true')
            b = request.POST.get(str(a['pk']))
            if b != str(answer.id):
                passed = False
        if passed:
            return redirect('test-passed')
        return redirect('test-failed')


def test_passed(request):
    return render(request, 'instructor-test/test-passed.html')


def test_failed(request):
    return render(request, 'instructor-test/test-failed.html')


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
        answeropt2 = request.POST['answeropt2']
        answeropt3 = request.POST['answeropt3']
        answeropt4 = request.POST['answeropt4']
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
    return render(request, 'instructor-test/add-question.html', context)


def instructor_test(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'instructor-test/instructor-test.html', context)


def category_test(request, id):
    category = Category.objects.get(id=id)
    categories = secCategory.objects.filter(category=category)
    context = {
        'categories': categories
    }
    return render(request, 'instructor-test/category-test.html', context)