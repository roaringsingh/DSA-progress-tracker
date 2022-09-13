from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserQuestionSet(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    link = models.URLField()
    solved = models.BooleanField(default=False)
    revised = models.BooleanField(default=False)
    lang = [(1, 'Python'), (2, 'C++'), (3, 'Java'), (4, 'Other')]
    language = models.IntegerField(choices=lang, default=4)
    notes = models.TextField(null=True)
