from django.contrib import admin
from .models import Student, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'regno', 'phone_number', 'student_class', 'authorized']
    list_filter = ['student_class', 'authorized']
    search_fields = ['name', 'regno']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'check_in_time', 'status']
    list_filter = ['date']
    search_fields = ['student__name']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ['student', 'date', 'check_in_time', 'status']
        else:  # Adding a new object
            return ['date', 'check_in_time', 'status']

    def save_model(self, request, obj, form, change):
        if change:  # Editing an existing object
            # Ensure check-in and check-out times cannot be modified via admin
            obj.check_in_time = Attendance.objects.get(id=obj.id).check_in_time
            obj.status = Attendance.objects.get(id=obj.id).status
        super().save_model(request, obj, form, change)

