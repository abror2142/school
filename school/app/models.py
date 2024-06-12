from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    experience = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.teacher} {self.subject}"


class Class(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject)
    teacher_subjects = models.ManyToManyField(TeacherSubject)
    
    def __str__(self) -> str:
        return self.name
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    class_field = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    
class Lesson(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    lesson_date = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.name
    

class LessonVideo(models.Model):
    
    def file_size(value):
        limit = 20 * 1024 * 1024
        if value.size > limit:
            raise ValidationError("File too long. Size should not exceed 2 Mib.")
    
    name = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='lesson/video/', validators=[
        FileExtensionValidator(['mp4', 'avi']),
        file_size
    ])

    def __str__(self) -> str:
        return f"{self.lesson} {self.name}"
    
    
    