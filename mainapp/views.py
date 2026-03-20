from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request, id):
    return render(request, 'projects.html', {'project_id': id})

def info(request):
    ip = request.META.get('REMOTE_ADDR')
    browser = request.META.get('HTTP_USER_AGENT')
    return HttpResponse(f"<h3>Пайдаланушы ақпараты:</h3><p>IP: {ip}</p><p>Браузер: {browser}</p>")