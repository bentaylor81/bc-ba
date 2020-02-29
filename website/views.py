from django.shortcuts import render, redirect
from .models import board_members, pages
from .forms import BoardmembersForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def directory_of_members(request):
    return render(request, 'member-directory.html', {})
    
def sponsors_current(request):
   return render(request, 'sponsors-current.html', {})

def resources(request):
    return render(request, 'resources.html', {})

def add_board_member(request):
    if request.method == 'POST':
        form = BoardmembersForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Board Member has been Added'))
            return redirect('who-are-we')
        else: 
            messages.success(request, ('There is an Error Adding Board Member'))
            return render(request, 'board-member-add.html')
    else:   
        return render(request, 'board-member-add.html', {})

def edit_board_member(request, list_id):
    if request.method == 'POST':
        board_member = board_members.objects.get(pk=list_id)
        form = BoardmembersForm(request.POST or None, instance=board_member)
        if form.is_valid():
            form.save()
            messages.success(request, ('Board Member has been Edited'))
            return redirect('who-are-we')
        else: 
            messages.success(request, ('There is an Error Editing Board Member'))
            return redirect(request, 'board_member_edit.html', {})
    else:
        get_board_member = board_members.objects.get(pk=list_id)
        return render(request, 'board-member-edit.html', {'get_board_member': get_board_member})
        
def delete(request, list_id):
    if request.method == 'POST':
        board_member = board_members.objects.get(pk=list_id)
        board_member.delete()
        messages.success(request, ('Board Member has been Deleted'))
        return redirect('who-are-we')
    else:
        messages.success(request, ('Delete Unsuccesful'))
        return redirect('who-are-we')         

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
