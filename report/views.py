from django.shortcuts import render, redirect
from classrooms.models import Day
from report.models import ReportClassroom


def manage_reports(request):
    reports = ReportClassroom.objects.all()
    context = {
        'reports': reports
    }
    return render(request, 'report/report.html', context)


def report(request, id):
    user = request.user
    day = Day.objects.get(id=id)
    subject = request.POST.get('subject')
    description = request.POST.get('description')
    ReportClassroom.objects.create(user=user, day=day, subject=subject, description=description)
    return redirect('content', day.classroom.id)