from django.db import models
from django.contrib.auth.models import User


# Bit Manipulation, Trie, Segment Tree
class Misc(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lang = [(1, 'Python'), (2, 'C++'), (3, 'Java'), (4, 'Other')]
    yn = [(1, 'Yes'), (2, 'No')]

    bqs1 = models.IntegerField(choices=yn, default=2)
    bqr1 = models.IntegerField(choices=yn, default=2)
    bql1 = models.IntegerField(choices=lang, default=4)
    bqnotes1 = models.TextField(null=True, blank=True)

    tqs1 = models.IntegerField(choices=yn, default=2)
    tqr1 = models.IntegerField(choices=yn, default=2)
    tql1 = models.IntegerField(choices=lang, default=4)
    tqnotes1 = models.TextField(null=True, blank=True)

    sqs1 = models.IntegerField(choices=yn, default=2)
    sqr1 = models.IntegerField(choices=yn, default=2)
    sql1 = models.IntegerField(choices=lang, default=4)
    sqnotes1 = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.uid)

    def __getitem__(self, key):
        return getattr(self, key)
