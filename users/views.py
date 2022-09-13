from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core import exceptions
from django.db.models.signals import post_save
from django.dispatch import receiver

from .forms import UserRegistrationForm
from dsasheet.models import *


@receiver(post_save, sender=User)
def init_new_user(instance, created, raw, **kwargs):
    # raw is set when model is created from loaddata.
    if created and not raw:
        arrays.Array.objects.create(uid=instance)
        maths.Maths.objects.create(uid=instance)
        stacks.Stack.objects.create(uid=instance)
        hash.Hash.objects.create(uid=instance)
        strings.String.objects.create(uid=instance)
        recursion.Recur.objects.create(uid=instance)
        linklist.LinkedL.objects.create(uid=instance)
        trees.Tree.objects.create(uid=instance)
        heaps.Heap.objects.create(uid=instance)
        traversal.Trav.objects.create(uid=instance)
        graphs.Graph.objects.create(uid=instance)
        dynamic.DynamicP.objects.create(uid=instance)
        miscs.Misc.objects.create(uid=instance)


def home_view(request):
    context = {
    }
    return render(request, 'users/home.html', context)


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Hi, {username} your account was created')
        return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required()
def profile_view(request):
    context = {}
    return render(request, 'users/profile.html', context)


@login_required()
def delete_account_view(request):
    print(request.user, 'delete')
    try:
        obj = User.objects.get(username=request.user)
        obj.delete()
        messages.success(request, 'Your Account was deleted successfully')
        return redirect('login')
    except exceptions.ObjectDoesNotExist:
        messages.warning(request, 'Account does not exist')
        return redirect('login')
