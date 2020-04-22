from django.shortcuts import render
from .models import Todo  # . : 현재 디렉토리

# Create your views here.
def todo_view(request):
    todos = Todo.objects.all()
    data = {
            "todos" : todos,
    }
    return render(request, "todo_list.html", data)