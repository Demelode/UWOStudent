from django.http import HttpResponse
from django.shortcuts import render
from website.models import Student, TimeTable, Course, ExamSchedule
from website.models import Exam, Degree, Grade, GradeBook

from website.models import Announcement, About  # remove

##### REMOVE BELOW, FOR TEST PURPOSES #####


def main(request):
    announcement_list = Announcement.objects.order_by('-date')[:3]
    context = {'announcement_list': announcement_list}
    return render(request, 'main.html', context)


def play(request):
    return render(request, 'play.html')


def hiscores(request):
    return render(request, 'hiscores.html')


def about(request):
    about_list = About.objects.order_by('title')[:1]
    context = {'about_list': about_list}
    return render(request, 'about.html', context)
##### REMOVE ABOVE, FOR TEST PURPOSES #####
