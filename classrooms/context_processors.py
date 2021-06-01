from announcements.models import AnnouncementUser


def add_variable_to_context(request):
    if request.user.is_authenticated:
        announcements = AnnouncementUser.objects.filter(user=request.user)
        
        return {
            'announcementss': announcements
        }
    return {
        'announcementss': 'announcements'
        }