from django.urls import path
from . import views
from . import views
urlpatterns = [
    path('capture_student/', views.capture_student, name='capture_student'),
    path('', views.home, name='home'),
    path('selfie-success/', views.selfie_success, name='selfie_success'),
    # path('capture-and-recognize/', views.capture_and_recognize, name='capture_and_recognize'),
    path('students/attendance/', views.student_attendance_list, name='student_attendance_list'),
    path('students/', views.student_list, name='student-list'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('students/<int:pk>/authorize/', views.student_authorize, name='student-authorize'),
    path('students/<int:pk>/delete/', views.student_delete, name='student-delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('submit-location/', views.submit_location, name='submit_location'),
    path('face_verification/', views.face_verification, name='face_verification')
]
    
