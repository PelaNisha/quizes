from django.db import models
from quizes.models import Quiz
# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length= 120)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length= 120)     
    correct = models.BooleanField(default = False)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
           
    def __str__(self):
        return f"question:{self.question.text}, answer:{self.text},correct: {self.correct}"       