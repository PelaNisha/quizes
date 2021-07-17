from django.urls import path
from .views import(
    QuizListView,
    quiz_view,
    quiz_data_view,
)

app_name = 'quizes'


urlpatterns = [
    path('', QuizListView.as_view(), name='main_view'),
    path('<pk>/', quiz_view, name = 'quiz_view' ),
    path('<pk>/data/', quiz_data_view, name = 'quiz_data_view'),

]