from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def Todoform(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Todoform')
    else:
        form = TodoForm()
    return render(request, 'Todoform.html', {'todos': todos, 'form': form})

def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('Todoform')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'Todoform.html', {'form': form})

def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('Todoform')
    return render(request, 'delete.html', {'todo': todo})
