from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'portfolio/index.html',{})

def about(request):
    return render(request, 'portfolio/about.html')  # Rendre le template about.html

def projects(request):
    return render(request, 'portfolio/projects.html')  # Rendre le template projects.html