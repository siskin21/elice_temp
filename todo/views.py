from django.shortcuts import render
from .models import Todo  # . : 현재 디렉토리

# Create your views here.
def todo_view(request):
    todos = Todo.objects.all()
    data = {
            "todos" : todos,
    }
    return render(request, "todo_list.html", data)

def in_progress_view(request):
    todos = Todo.objects.all()
    data = {
            "todos" : todos,
    }
    return render(request, "in_progress.html", data)

# def var_view(request):
#     present = [1, 2, 3, 4, 5]
#     return render(request, "var.html", {"students":present}) 
#      #var.html 에서 students라는 변수를 사용하면 present 값을 리턴해줌