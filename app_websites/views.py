from django.shortcuts import render, redirect
from .models import board_members, corp_members, resources, sponsors, pages
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def directory_of_members(request):
    context = { 
        'corp_members': corp_members.objects.all().order_by('corp_member_name'),
        }
    return render(request, 'member-directory.html', context )
    
def current_sponsors(request):
    context = { 
        'sponsors': sponsors.objects.all().order_by('sponsor_name'),
        }
    return render(request, 'sponsors-current.html', context )

def resources_page(request):
    context = { 
        'resources': resources.objects.all().order_by('resource_name'),
        }
    return render(request, 'resources.html', context )

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
