from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        duedate = request.POST.get('duedate')

        Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            duedate=duedate
        )

        return redirect('home')

    return render(request, 'add.html')


def view_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'view.html', {'task': task})


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.duedate = request.POST.get('duedate')

        task.is_complete = request.POST.get('is_complete') == 'on'

        task.save()
        return redirect('home')

    return render(request, 'update.html', {'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'delete.html', {'task': task})