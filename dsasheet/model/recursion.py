from django.db import models
from django.contrib.auth.models import User


# Recursion, Backtracking and Design
class Recur(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lang = [(1, 'Python'), (2, 'C++'), (3, 'Java'), (4, 'Other')]
    yn = [(1, 'Yes'), (2, 'No')]

    rqs1 = models.IntegerField(choices=yn, default=2)
    rqr1 = models.IntegerField(choices=yn, default=2)
    rql1 = models.IntegerField(choices=lang, default=4)
    rqnotes1 = models.TextField(null=True, blank=True)
    rqs2 = models.IntegerField(choices=yn, default=2)
    rqr2 = models.IntegerField(choices=yn, default=2)
    rql2 = models.IntegerField(choices=lang, default=4)
    rqnotes2 = models.TextField(null=True, blank=True)
    rqs3 = models.IntegerField(choices=yn, default=2)
    rqr3 = models.IntegerField(choices=yn, default=2)
    rql3 = models.IntegerField(choices=lang, default=4)
    rqnotes3 = models.TextField(null=True, blank=True)
    rqs4 = models.IntegerField(choices=yn, default=2)
    rqr4 = models.IntegerField(choices=yn, default=2)
    rql4 = models.IntegerField(choices=lang, default=4)
    rqnotes4 = models.TextField(null=True, blank=True)
    rqs5 = models.IntegerField(choices=yn, default=2)
    rqr5 = models.IntegerField(choices=yn, default=2)
    rql5 = models.IntegerField(choices=lang, default=4)
    rqnotes5 = models.TextField(null=True, blank=True)
    rqs6 = models.IntegerField(choices=yn, default=2)
    rqr6 = models.IntegerField(choices=yn, default=2)
    rql6 = models.IntegerField(choices=lang, default=4)
    rqnotes6 = models.TextField(null=True, blank=True)
    rqs7 = models.IntegerField(choices=yn, default=2)
    rqr7 = models.IntegerField(choices=yn, default=2)
    rql7 = models.IntegerField(choices=lang, default=4)
    rqnotes7 = models.TextField(null=True, blank=True)
    rqs8 = models.IntegerField(choices=yn, default=2)
    rqr8 = models.IntegerField(choices=yn, default=2)
    rql8 = models.IntegerField(choices=lang, default=4)
    rqnotes8 = models.TextField(null=True, blank=True)
    rqs9 = models.IntegerField(choices=yn, default=2)
    rqr9 = models.IntegerField(choices=yn, default=2)
    rql9 = models.IntegerField(choices=lang, default=4)
    rqnotes9 = models.TextField(null=True, blank=True)
    rqs10 = models.IntegerField(choices=yn, default=2)
    rqr10 = models.IntegerField(choices=yn, default=2)
    rql10 = models.IntegerField(choices=lang, default=4)
    rqnotes10 = models.TextField(null=True, blank=True)
    rqs11 = models.IntegerField(choices=yn, default=2)
    rqr11 = models.IntegerField(choices=yn, default=2)
    rql11 = models.IntegerField(choices=lang, default=4)
    rqnotes11 = models.TextField(null=True, blank=True)
    rqs12 = models.IntegerField(choices=yn, default=2)
    rqr12 = models.IntegerField(choices=yn, default=2)
    rql12 = models.IntegerField(choices=lang, default=4)
    rqnotes12 = models.TextField(null=True, blank=True)
    rqs13 = models.IntegerField(choices=yn, default=2)
    rqr13 = models.IntegerField(choices=yn, default=2)
    rql13 = models.IntegerField(choices=lang, default=4)
    rqnotes13 = models.TextField(null=True, blank=True)
    rqs14 = models.IntegerField(choices=yn, default=2)
    rqr14 = models.IntegerField(choices=yn, default=2)
    rql14 = models.IntegerField(choices=lang, default=4)
    rqnotes14 = models.TextField(null=True, blank=True)
    rqs15 = models.IntegerField(choices=yn, default=2)
    rqr15 = models.IntegerField(choices=yn, default=2)
    rql15 = models.IntegerField(choices=lang, default=4)
    rqnotes15 = models.TextField(null=True, blank=True)
    rqs16 = models.IntegerField(choices=yn, default=2)
    rqr16 = models.IntegerField(choices=yn, default=2)
    rql16 = models.IntegerField(choices=lang, default=4)
    rqnotes16 = models.TextField(null=True, blank=True)

    bmqs1 = models.IntegerField(choices=yn, default=2)
    bmqr1 = models.IntegerField(choices=yn, default=2)
    bmql1 = models.IntegerField(choices=lang, default=4)
    bmqnotes1 = models.TextField(null=True, blank=True)
    bmqs2 = models.IntegerField(choices=yn, default=2)
    bmqr2 = models.IntegerField(choices=yn, default=2)
    bmql2 = models.IntegerField(choices=lang, default=4)
    bmqnotes2 = models.TextField(null=True, blank=True)

    bhqs1 = models.IntegerField(choices=yn, default=2)
    bhqr1 = models.IntegerField(choices=yn, default=2)
    bhql1 = models.IntegerField(choices=lang, default=4)
    bhqnotes1 = models.TextField(null=True, blank=True)
    bhqs2 = models.IntegerField(choices=yn, default=2)
    bhqr2 = models.IntegerField(choices=yn, default=2)
    bhql2 = models.IntegerField(choices=lang, default=4)
    bhqnotes2 = models.TextField(null=True, blank=True)
    bhqs3 = models.IntegerField(choices=yn, default=2)
    bhqr3 = models.IntegerField(choices=yn, default=2)
    bhql3 = models.IntegerField(choices=lang, default=4)
    bhqnotes3 = models.TextField(null=True, blank=True)
    bhqs4 = models.IntegerField(choices=yn, default=2)
    bhqr4 = models.IntegerField(choices=yn, default=2)
    bhql4 = models.IntegerField(choices=lang, default=4)
    bhqnotes4 = models.TextField(null=True, blank=True)

    dqs1 = models.IntegerField(choices=yn, default=2)
    dqr1 = models.IntegerField(choices=yn, default=2)
    dql1 = models.IntegerField(choices=lang, default=4)
    dqnotes1 = models.TextField(null=True, blank=True)
    dqs2 = models.IntegerField(choices=yn, default=2)
    dqr2 = models.IntegerField(choices=yn, default=2)
    dql2 = models.IntegerField(choices=lang, default=4)
    dqnotes2 = models.TextField(null=True, blank=True)
    dqs3 = models.IntegerField(choices=yn, default=2)
    dqr3 = models.IntegerField(choices=yn, default=2)
    dql3 = models.IntegerField(choices=lang, default=4)
    dqnotes3 = models.TextField(null=True, blank=True)
    dqs4 = models.IntegerField(choices=yn, default=2)
    dqr4 = models.IntegerField(choices=yn, default=2)
    dql4 = models.IntegerField(choices=lang, default=4)
    dqnotes4 = models.TextField(null=True, blank=True)
    dqs5 = models.IntegerField(choices=yn, default=2)
    dqr5 = models.IntegerField(choices=yn, default=2)
    dql5 = models.IntegerField(choices=lang, default=4)
    dqnotes5 = models.TextField(null=True, blank=True)
    dqs6 = models.IntegerField(choices=yn, default=2)
    dqr6 = models.IntegerField(choices=yn, default=2)
    dql6 = models.IntegerField(choices=lang, default=4)
    dqnotes6 = models.TextField(null=True, blank=True)
    dqs7 = models.IntegerField(choices=yn, default=2)
    dqr7 = models.IntegerField(choices=yn, default=2)
    dql7 = models.IntegerField(choices=lang, default=4)
    dqnotes7 = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.uid)

    def __getitem__(self, key):
        return getattr(self, key)
