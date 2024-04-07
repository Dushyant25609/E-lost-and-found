from django.urls import path
from . import views

urlpatterns = [
    path('student/signup/', views.student_signup, name='student_signup'),
    path('student/login/', views.students_login,name="student_login"),
    path('organisation/login/', views.organisation_login, name="organization_login"),
    # Add URLs for signup success pages if needed
]
