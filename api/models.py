from django.db import models
from django.core.validators import RegexValidator

class Student(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    dob = models.DateField()
    address = models.CharField(max_length=500, blank=False)
    phone_regex = RegexValidator(regex=r'^[1-9]\d{9}$', message="Phone number must be entered in the format: 1234567890")
    phone = models.CharField(validators=[phone_regex], max_length=10, blank=False, unique=True)

class Subject(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    text_book = models.CharField(max_length=200, blank=False)

class Teacher(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)

class SubjectStudentMap(models.Model):
    class Meta:
        unique_together = (("student_id", "subject_id"),)

    student_id = models.ForeignKey(Student, on_delete=models.RESTRICT, unique=False)
    subject_id = models.ForeignKey(Subject, on_delete=models.RESTRICT, unique=False)

