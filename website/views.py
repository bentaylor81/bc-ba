from django.shortcuts import render
from .models import board_members, pages

def home(request):
    return render(request, 'home.html', {})

def directory_of_members(request):
    return render(request, 'member-directory.html', {})
    
def sponsors_current(request):
   return render(request, 'sponsors-current.html', {})

def resources(request):
    return render(request, 'resources.html', {})

def who_are_we(request):
    context = board_members.objects.all().order_by('priority')
    return render(request, 'who-are-we.html', {
        'board_members': context
        })

def page(request, page_path): 
    context = {
        'page_content' : pages.objects.filter(url_path=page_path) 
        }
    return render(request, 'page.html', context)
