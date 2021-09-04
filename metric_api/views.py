from django.shortcuts import render
import prometheus_client
from django.http import HttpResponse
from .models import Tasks
# Create your views here.


def index(request):
    return HttpResponse("hello world")

from django.shortcuts import render,redirect
from .models import Tasks
# Create your views here.


def task_index(request):
    if request.method == 'POST':
        data=request.POST.get('task')
        t=Tasks(task=data)
        t.save()
    else:
        return render(request,"tasks/index.html",{
        "tasks":Tasks.objects.all()
    })


    return render(request,"tasks/index.html",{
        "tasks":Tasks.objects.all()
    })

def delete(request,r_id):
    data= Tasks.objects.get(id =r_id)
    data.delete()
    return render(request,"tasks/index.html",{
        "tasks":Tasks.objects.all()
    })

def update_template(request,r_id):
    data= Tasks.objects.get(id =r_id)
    return render(request,"tasks/update.html",{
        "data":data.task,
        "id":r_id
    })
    
def update(request,r_id):
    data= Tasks.objects.get(id =r_id)
    data.task=request.POST.get('task')
    data.save()
    return redirect('/task',name=task_index)

# def metrics(request):
#     metrics_page = prometheus_client.generate_latest()
#     return HttpResponse(
#             metrics_page,
#             content_type=prometheus_client.CONTENT_TYPE_LATEST)

