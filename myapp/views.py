from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm
# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return render(request, "projects.html", {'projects': projects})

def tasks(request):
    tasks = list(Task.objects.all())
    context = {"tasks":tasks}
    return render(request, "tasks.html",context)
def task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {"task":task}
    return render(request, "task.html",context)
def form(request, id):
  
    return render(request, "form.html",{
        'form': TaskForm
    })
# Password GrupoASD123