from django.shortcuts import render, redirect
from classrooms.models import Day, Classroom
from instructor_test.models import TestPassed
from report.models import ReportClassroom
from announcements.models import AnnouncementAdmin, MessageAdmin


def manage_reports(request):
    reports = ReportClassroom.objects.all().order_by('-pk')
    for report in reports:
        if MessageAdmin.objects.filter(classroom=report.day.classroom).exists():
            report.message_status = True
        else:
            report.message_status = False
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


def review_report(request, id):
    report = ReportClassroom.objects.get(id=id)
    if MessageAdmin.objects.filter(classroom = report.day.classroom).exists():
        response = MessageAdmin.objects.filter(classroom = report.day.classroom).first()
        print(response)
        report.response = True
        context = {
            'report': report,
            'response': response
        }
    else:
        report.response = False
        context = {
            'report': report
        }
    return render(request, 'report/review-report.html', context)


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


def block_warn_classroom(request, id):
    report = ReportClassroom.objects.get(id=id)
    headline = request.POST.get('subject')
    description = request.POST.get('description')
    classroom = Classroom.objects.get(id=report.day.classroom.id)
    AnnouncementAdmin.objects.create(classroom=classroom, headline=headline, content=description)
    classroom.is_active = False
    classroom.save()
    return redirect('review-report', id)


def unblock_reported_classroom(request, id):
    report = ReportClassroom.objects.get(id=id)
    classroom = Classroom.objects.get(id=report.day.classroom.id)
    annoucement_admin = AnnouncementAdmin.objects.filter(classroom=classroom)
    message_admin = MessageAdmin.objects.filter(classroom=classroom)
    classroom.is_active = True
    classroom.save()
    report.delete()
    annoucement_admin.delete()
    message_admin.delete()
    return redirect('reports')


def reported_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    if AnnouncementAdmin.objects.filter(classroom=classroom).exists():
        message = AnnouncementAdmin.objects.filter(classroom=classroom).first()
        if MessageAdmin.objects.filter(classroom=classroom).exists():
            message.status = True
        else:
            message.status = False
        context = {
            'message': message
        }
        return render(request, 'report/reported-classroom.html', context)
    return redirect('my-classroom')


def send_message_admin(request, id):
    classroom = Classroom.objects.get(id=id)
    if request.method == 'POST':
        message = request.POST.get('message')
        MessageAdmin.objects.create(classroom=classroom, content=message)
    return redirect('reported-classroom', id)


def delete_report(request, id):
    report = ReportClassroom.objects.get(id=id)
    report.delete()
    return redirect('reports')