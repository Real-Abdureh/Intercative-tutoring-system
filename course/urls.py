from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('course-selection/', views.course_selection_view, name='course-selection'),
    path('course-content/', views.course_content_view, name='course-content'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
    # path('quiz/<int:course_id>/', views.quiz_view, name='quiz'),
     
]