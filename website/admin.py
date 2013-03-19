from django.contrib import admin
from website.models import Student, TimeTable, Course, ExamSchedule
from website.models import Exam, Degree, Grade, GradeBook

from website.models import Announcement, About  # remove test


##### REMOVE BELOW, FOR TEST PURPOSES #####


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'poster')
    fieldsets = [
        ('Announcement Title', {'fields': ['title']}),
        ('Announcement Body', {'fields': ['body']}),
        ('Announcement Poster', {'fields': ['poster']}),
    ]

admin.site.register(Announcement, AnnouncementAdmin)


##### REMOVE ABOVE, FOR TEST PURPOSES #####


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_number')
    fieldsets = [
        ('Student Info',
            {'fields': ('first_name',
                        'last_name',
                        'address',
                        'postal_code',
                        'student_number',
                        'visa_exp_date',
                        'visa_type',
                        'visa_country',
                        'citizen_country',
                        'citizen_status',
                        'birth_date')}),
        ('Owing', {'fields': ['money_owing']}),
        ('Other',
            {'fields': ('degree',
                        'time_table',
                        'exam_schedule')}),
    ]

admin.site.register(Student, StudentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_number', 'name')
    fieldsets = [
        ('Course Info',
            {'fields': ('course_id',
                        'course_number',
                        'name',
                        'section',
                        'location',
                        'start_time',
                        'end_time')})
    ]

admin.site.register(Course, CourseAdmin)


class DegreeAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree_type', 'program_type')
    fieldsets = [
        ('Degree Info',
            {'fields': ('school',
                        'program_type',
                        'length',
                        'degree_type',
                        'first_module',
                        'second_module')})
    ]

admin.site.register(Degree, DegreeAdmin)


class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'date', 'time', 'room')
    fieldsets = [
        ('Exam Info',
            {'fields': ('course',
                        'date',
                        'time',
                        'room',
                        'name_range')})
    ]

admin.site.register(Exam, ExamAdmin)


class ExamScheduleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Exam Schedule Info',
            {'fields': (['exams'])})
    ]

admin.site.register(ExamSchedule, ExamScheduleAdmin)


class TimeTableAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Time Table Info',
            {'fields': (['courses'])})
    ]

admin.site.register(TimeTable, TimeTableAdmin)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('course', 'grade')
    fieldsets = [
        ('Grade Info',
            {'fields': ('course',
                        'grade')})
    ]

admin.site.register(Grade, GradeAdmin)


class GradeBookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Grade Book Info',
            {'fields': (['grades'])})
    ]

admin.site.register(GradeBook, GradeBookAdmin)
