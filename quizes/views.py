from django.shortcuts import render
from .models import Quiz
from quizes.models import *
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk = pk)
    return render(request, 'quizes/quiz.html', {'obj':quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk = pk)
    questions =[]
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers}) 
    return JsonResponse({
            'data': questions,
            'time':quiz.time,        
    })
          
def save_quiz_view(request, pk):
    # print(request.POST)
         

    if request.is_ajax():
        questions = []
        data = request.POST
        data_= dict(data.lists())
        data_.pop('csrfmiddlewaretoken') 
        print(data_)

        for k in data_.keys():
            print('key:', k)
            question = Question.objects.get(text = k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk = pk)
        score =0
        multiplier= 100/quiz.number_of_question
        results = []
        correct_answer = None
        for q in questions:
            a_selected = request.POST.get(q.text)
            print('Selected:', a_selected)

    return JsonResponse({'text':'works'})        