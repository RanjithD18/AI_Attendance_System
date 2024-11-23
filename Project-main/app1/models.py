from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=255)
    regno = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    student_class = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/')
    authorized = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.student.name} - {self.date}"

    def mark_checked_in(self):
        self.check_in_time = timezone.now()
        self.status = 'Present'
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only on creation
            self.date = timezone.now().date()
        super().save(*args, **kwargs)

