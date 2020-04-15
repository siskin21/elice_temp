from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    # return HttpResponse("<p>Hello World!</p>")
    return render(request, "index.html", {}) #render() :request, index.html을 조합하여 HttpResponse를 반환

def quote_view(request): 
    return render(request, "quote.html", {})