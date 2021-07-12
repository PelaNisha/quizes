from django.db import models

# Create your models here.
DIFF_CHOICES = (
    ('easy','easy'),
    ('medium', 'medium'),
    ('hard','hard')
)
class Quiz(models.Model):
    name = models.CharField(max_length= 120)
    topic = models.CharField(max_length= 120)
    number_of_question = models.IntegerField()
    time = models.IntegerField(help_text= 'duration of the quiz in minutes')
    score = models.IntegerField(help_text= 'required score in %')
    difficulty = models.CharField(max_length= 120, choices = DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        return self.question_set.all()


    class Meta:
        verbose_name_plural = 'Quizes'   