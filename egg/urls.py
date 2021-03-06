"""egg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home_view #home 폴더 안 views.py 파일의 home_view 함수를 불러 옴
from home.views import quote_view
from todo.views import todo_view
from todo.views import in_progress_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view), #호출한 url에 도메인 뒤 하위 폴더가 없을 때-> home_view를 실행 
    path('quote/', quote_view),
    path('todos/', todo_view, name='todos'),
    path('todos/in_progress', in_progress_view, name='in progress')
]
