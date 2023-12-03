from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task
from .forms import todoform
from django.views.generic import ListView

# Create your views here.
def tasks(request):
    displaytask = Task.objects.all()
    if request.method == 'POST':
        task = request.POST['task']
        priority = request.POST['priority']
        date = request.POST['date']
        data = Task(task=task,priority=priority,date=date)
        data.save()
        print('task add')
    return render(request,'index.html',{'tasks':displaytask})
def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')
def update(request,taskid):
    task = Task.objects.get(id=taskid)
    f = todoform(request.POST or None ,instance= task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task})
    


# Generic view

# class Tasklistview(ListView):
#     model = Task
#     template_name = 'index.html'
#     context_object_name = 'tasks'