from django.shortcuts import render, redirect
from .models import board_members, corp_members, resources, sponsors, pages, meta
from django.contrib import messages

def home(request):
    context = {
        'meta_content' : meta.objects.filter(meta_page='home')
        }
    return render(request, 'home.html', context)
    
def directory_of_members(request):
    context = { 
        'meta_content' : meta.objects.filter(meta_page='member-directory'),
        'corp_members': corp_members.objects.all().order_by('corp_member_name'),
        }
    return render(request, 'member-directory.html', context )
    
def current_sponsors(request):
    context = { 
        'meta_content' : meta.objects.filter(meta_page='current-sponsors'),
        'sponsors': sponsors.objects.all().order_by('sponsor_name'),
        }
    return render(request, 'sponsors-current.html', context )

def resources_page(request):
    context = { 
        'meta_content' : meta.objects.filter(meta_page='resources'),
        'resources': resources.objects.all().order_by('resource_name'),
        }
    return render(request, 'resources.html', context )

def who_are_we(request):  
    context = {
        'meta_content' : meta.objects.filter(meta_page='who-are-we'),
        'board_members' : board_members.objects.all().order_by('priority')
        }
    return render(request, 'who-are-we.html', context )

def page(request, page_path): 
    context = {
        'meta_content' : meta.objects.filter(meta_page=page_path),
        'page_content' : pages.objects.filter(url_path=page_path), 
        }
    return render(request, 'page.html', context)
