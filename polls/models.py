from django.db import models


# Create your models here.
class Question (models.Model):
    question_text = models.CharField(max_length=200)

    pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)

    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

class QuestionTest (models.Model):
    subject = models.CharField(max_length=100)

    context = models.TextField(max_length=6000)

    inDate = models.DateField("등록 날짜")

    def __str__(self):
        return self.subject

