from django.shortcuts import render

# Create your views here.


tasks = ['item 1', ' item 2', 'item 3']
    
def index(request):
    return render(request, 'tasks/index.html',{
        "tasks": tasks
    })
