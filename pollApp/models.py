from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Question(models.Model):
    types = (
        ("text_answer","Text answer"),
        ("single_answer","Single answer"),
        ("multiple_answer","Multiple answer")
    )
    question_text = models.TextField()
    question_type = models.CharField(choices=types,default="single_answer",max_length=80)
    poll = models.ForeignKey(
        Poll,
        blank=True,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return self.question_text[:50]

class Choice(models.Model):
    choiceText = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question,
        on_delete = models.CASCADE,
        related_name="choices"
    )
    def __str__(self):
        return self.choiceText

class Answer(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        related_name="answers"
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    multiple_answer = models.ManyToManyField(Choice)
    single_answer = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        related_name="single_answer_choice"
    )
    text_answer = models.CharField(max_length=200)

















