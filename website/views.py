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

def user(request):
	return render(request, 'user.html')

def login(request):
    m = Student.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")

##### REMOVE ABOVE, FOR TEST PURPOSES #####
