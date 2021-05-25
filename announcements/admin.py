from django.contrib import admin
from . models import Announcement, AnnouncementUser


admin.site.register(Announcement)
admin.site.register(AnnouncementUser)