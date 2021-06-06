from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    forums = Forum.objects.all()
    cont = forums.count()
    discussions = []

    for forum in forums:
        discussions.append(forum.discussion_set.all())

    context = {
        'forums' : forums,
        'count' : cont,
        'discussions' : discussions
    }
    return render(request, 'home.html', context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context = {
        'form' : form
    }
    return render(request, 'addInForum.html', context)

def addInDiscussion(request):
    discuss = CreateInDiscuss()
    if request.method == 'POST':
        discuss = CreateInDiscuss(request.POST)
        if discuss.is_valid():
            discuss.save()
            return redirect('/')

    context = {
        'discuss' : discuss
    }
    return render(request, 'addInDiscussion.html', context)