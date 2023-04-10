from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Todo
from .forms import TodoForm

# Create your views here.

@login_required
def index(request):
    completed = request.GET.get('completed') or False
    todos = Todo.objects.filter(completed=completed)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
    else:
        form = TodoForm()

    context = {
        'form' : form,
        'todos' : todos,    
    }

    return render(request, 'todos/index.html', context)

def complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todos:index')

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
        
def delete(request,pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            todo.delete()
            return redirect('todos:index')
