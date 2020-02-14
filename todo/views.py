from django.shortcuts import HttpResponse, render, redirect, HttpResponseRedirect, get_object_or_404,render_to_response
from .models import *
from .forms import *
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.core import serializers

# Create your views here.
# render(request, 'blog/addition.html', locals()),  redirect(view_name, k)

def base(request):
    return render(request, 'todo/base.html')

def todos(request):
    d_todos = Todoproject.objects.all()
    data = serializers.serialize('json', d_todos)
    return JsonResponse(data, safe=False)

def add(request):
    todo_i = request.POST['todo_i']
    #if todo_i.trim().length < 0:
        
    print("voila ", todo_i)
    newTodo = Todoproject(todo = todo_i)
    newTodo.save()
    return redirect(todos)
    # d_todos = Todoproject.objects.all()
    # data = serializers.serialize('json', d_todos)
    # return JsonResponse(data, safe=False)


def delete(request):
    id = request.GET['id']
    todo_delete = Todoproject.objects.get(id=id)
    print(todo_delete)
    todo_delete.delete()
    return redirect(todos)
    # d_todos = Todoproject.objects.all()
    # data = serializers.serialize('json', d_todos)
    # return JsonResponse(data, safe=False)