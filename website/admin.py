from django.contrib import admin
from website.models import Announcement, About, Game


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'poster')
    fieldsets = [
        ('Announcement Title', {'fields': ['title']}),
        ('Announcement Body', {'fields': ['body']}),
        ('Announcement Poster', {'fields': ['poster']}),
    ]

admin.site.register(Announcement, AnnouncementAdmin)
