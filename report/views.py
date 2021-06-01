from django.shortcuts import render, redirect
from classrooms.models import Day, Classroom
from instructor_test.models import TestPassed
from report.models import ReportClassroom


def manage_reports(request):
    if request.session.has_key('password'):
        reports = ReportClassroom.objects.all()
        context = {
            'reports': reports
        }
        return render(request, 'report/report.html', context)
    return redirect('admin-login')


def report(request, id):
    user = request.user
    day = Day.objects.get(id=id)
    subject = request.POST.get('subject')
    description = request.POST.get('description')
    ReportClassroom.objects.create(user=user, day=day, subject=subject, description=description)
    return redirect('content', day.classroom.id)


def review_report(request, id):
    if request.session.has_key('password'):
        report = ReportClassroom.objects.get(id=id)
        context = {
            'report': report
        }
        return render(request, 'report/review-report.html', context)
    return redirect('admin-login')


def delete_reported_classroom(request, id):
    report = ReportClassroom.objects.get(id=id)
    classroom = Classroom.objects.get(id=report.day.classroom.id)
    classroom.delete()
    return redirect('reports')


def delete_block_reported_classroom(request, id):
    report = ReportClassroom.objects.get(id=id)
    classroom = Classroom.objects.get(id=report.day.classroom.id)
    tutor = TestPassed.objects.get(user=classroom.user, sec_category=classroom.sec_category)
    print(report, classroom, tutor)
    tutor.delete()
    classroom.delete()
    return redirect('reports')