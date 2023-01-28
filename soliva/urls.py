from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/student', views.create_student),
    path('create/subject', views.create_subject),
    path('create/teacher', views.create_teacher),
    path('enroll/student/<int:student_id>/subject/<int:subject_id>', views.enroll_student),
    path('teachers/student/<int:student_id>', views.all_teachers),
]
