from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index (request,):
    title = "Django "
    return render(request,"index.html", {
        'title':title
        })

def about(request):
    return render(request,"about.html")

def hello (request, id):
    return HttpResponse("<h2>Hola %s </h2>"% id) 


def projects(request):
    projects = list(Project.objects.all().values())
    return render(request,"projects/projects.html", {
        'projects': projects
    })

def task(request):
    # task = Task.objects.get(id = id)
    tasks = Task.objects.all()
    return render(request,"tasks/tasks.html",{
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request,"tasks/create_task.html", {
        'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                        description=request.POST['description'], project_id=1)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request,"projects/create_projects.html", {
        'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    print(project)
    return render(request,'projects/detail.html',{
        'project':project,
        'tasks':tasks
    })