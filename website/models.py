import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


########## REMOVE BELOW. THIS IS TO SHOW HOW STUFF INTERACTS ############
class Announcement(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User)

    def was_posted_today(self):
        return was_posted(1)

    def was_posted(self, compdate):
        return self.date >= timezone.now() - datetime.timedelta(days=compdate)


class About(models.Model):
    title = models.CharField(max_length=50)
########## REMOVE ABOVE. THIS IS TO SHOW HOW STUFF INTERACTS ############


class Course(models.Model):
    course_id = models.IntegerField()  # Unique?
    course_number = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    section = models.IntegerField()
    location = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
        pass


class Degree(models.Model):
    school = models.CharField(max_length=30)
    program_type = models.CharField(max_length=30)
    length = models.IntegerField()
    degree_type = models.CharField(max_length=30)
    first_module = models.CharField(max_length=30, blank=True)
    second_module = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        pass


class Exam(models.Model):
    course = models.ForeignKey(Course)
    date = models.DateField()
    time = models.TimeField()
    room = models.CharField(max_length=20)
    name_range = models.CharField(max_length=20)

    def __unicode__(self):
        pass


class ExamSchedule(models.Model):
    exams = models.ManyToManyField(Exam, verbose_name='exams',
                                   related_name='exams_rev', null=True)

    def __unicode__(self):
        pass


class TimeTable(models.Model):
    courses = models.ManyToManyField(Course, verbose_name='courses',
                                     related_name='courses_rev', null=True)

    def __unicode__(self):
        pass


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    student_number = models.CharField(max_length=10)  # Should it be char? Mark: No, it's a numeric field

    visa_exp_date = models.DateField(blank=True)
    visa_type = models.CharField(max_length=20, blank=True)
    visa_country = models.CharField(max_length=20, blank=True)
    citizen_country = models.CharField(max_length=20)
    citizen_status = models.CharField(max_length=20)
    birth_date = models.CharField(max_length=20)

    money_owing = models.FloatField()

    degree = models.ForeignKey(Degree)
    time_table = models.ForeignKey(TimeTable)
    exam_schedule = models.ForeignKey(ExamSchedule)

    password = models.CharField(max_length=30)  # How should this be done? Mark: Alphanumeric encrypted MD5?

    def get_full_name(self):
        return first_name + " " + last_name

    def __unicode__(self):
        pass


class Grade(models.Model):
    course = models.ForeignKey(Course)
    grade = models.FloatField()

    def __unicode__(self):
        pass


class GradeBook(models.Model):
    grades = models.ManyToManyField(Grade)

    def __unicode__(self):
        pass
