import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
# now - datetime.timedelta(days=1)
# // Gives the previous day (to 'now')
# ... <= self.pub_date
# // If pub_date is greater/equal to prev date, returns true
# ... <= now
# // Checks if pub_date is ALSO smaller / eq to now so future dates are invalid


class Choice(models.Model):
    quesiton = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
