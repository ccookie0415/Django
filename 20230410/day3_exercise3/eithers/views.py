from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment, Question
from .forms import CommentForm, QuestionForm

# Create your views here.

def index(request):
    
    form = QuestionForm()

    context ={
        'form' : form,
    }

    return render(request, 'eithers/index.html', context)

@login_required
def create(request, pk):
    question = get_object_or_404(Question, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.question = Question
        comment.save()
    return redirect('eithers:index')


def random(request):
    pass

def detail(request):
    pass

def comment(request):
    pass