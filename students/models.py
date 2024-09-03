from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название школы")
    address = models.CharField(max_length=300, verbose_name="Адрес")
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя учителя")
    subject = models.CharField(max_length=100, verbose_name="Предмет")
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="teachers", verbose_name="Школа")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя студента")
    age = models.IntegerField(verbose_name="Возраст")
    grade = models.CharField(max_length=10, verbose_name="Класс")
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students", verbose_name="Школа")

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")
    students = models.ManyToManyField(Student, related_name="courses", verbose_name="Студенты")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="courses", verbose_name="Учитель")

    def __str__(self):
        return self.name
