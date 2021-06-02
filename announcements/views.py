from django.shortcuts import render, redirect
from classrooms.models import Classroom, Day, ClassroomEnrolled, QuestionsQandA, ReplyQandA
from . models import Announcement, AnnouncementUser



def announcements(request, id):
    if Classroom.objects.filter(id=id).exists():
        classroom = Classroom.objects.get(id=id)
        announcements = Announcement.objects.filter(classroom = classroom).order_by('-date_posted')
        questions = QuestionsQandA.objects.filter(classroom=classroom).order_by('-pk')
        answers = ReplyQandA.objects.filter(classroom=classroom).order_by('-pk')
        context = {
            'classroom': classroom,
            'announcements': announcements,
            'questions': questions,
            'answers': answers
        }
    return render(request, 'announcements/announcements.html', context)


def add_announcement(request, id):
    classroom = Classroom.objects.get(id=id)
    headline = request.POST.get('subject')
    message = request.POST.get('message-text')
    announcement = Announcement.objects.create(classroom=classroom, headline=headline, content=message)
    students = ClassroomEnrolled.objects.filter(classroom=classroom)
    for student in students:
        AnnouncementUser.objects.create(announcement=announcement, user=student.user)
    return redirect('announcements', id)


def all_announcements(request):
    announcements = AnnouncementUser.objects.filter(user=request.user).order_by('-pk') 
    print(announcements)   
    context = {
        'announcements': announcements
    }
    print(context)
    return render(request, 'announcements/all-announcements.html', context)


def mark_read(request, id):
    announcement = AnnouncementUser.objects.get(id=id)
    announcement.read = True
    announcement.save()
    return redirect('all-announcements')
