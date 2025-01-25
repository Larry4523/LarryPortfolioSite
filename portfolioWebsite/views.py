from django.shortcuts import render


def home(request):
    return render(request, 'portfolioWebsite/base.html')

def resume(request):
    return render(request, 'portfolioWebsite/resume.html')