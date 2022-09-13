from django.urls import path, include
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
    path('arrays/', array, name='array'),
    path('math/', math, name='math'),
    path('stack/', stack, name='stack'),
    path('hashing/', hashing, name='hashing'),
    path('string/', string, name='string'),
    path('recursion/', rec, name='recursion'),
    path('list/', llist, name='list'),
    path('tree/', tree, name='tree'),
    path('heap/', heap, name='heap'),
    path('trav/', trav, name='trav'),
    path('graph/', graph, name='graph'),
    path('dp/', dp, name='dp'),
    path('misc/', misc, name='misc'),

]
