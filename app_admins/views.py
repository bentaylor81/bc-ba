from django.shortcuts import render, redirect
from app_websites.models import board_members, corp_members, resources, pages, sponsors, meta
from app_contacts.models import contact
from .forms import BoardmembersForm, CorpmembersForm, ResourcesForm, SponsorsForm, PagesForm, MetaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_users.decorators import unauthenticated_user, allowed_users

def dashboard(request):
    return render(request, 'app_admins/dashboard.html' )

### SECTION RELATING TO BOARD MEMBERS ###

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def all_board_member(request):
    context = board_members.objects.all().order_by('priority')
    return render(request, 'app_admins/board-all.html', { 'board_members': context })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_board_member(request, list_id):
    if request.method == 'POST':
        board_member = board_members.objects.get(pk=list_id)
        form = BoardmembersForm(request.POST, request.FILES or None, instance=board_member)
        if form.is_valid():
            form.save()
            messages.success(request, ('Board Member has been Edited'))
            return redirect('all-board-member')
        else: 
            messages.error(request, ('There is an Error Editing Board Member'))
            return redirect(request, 'app_admins/board-edit.html', {})
    else:
        get_board_member = board_members.objects.get(pk=list_id)
        return render(request, 'app_admins/board-edit.html', { 'get_board_member': get_board_member, })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_board_member(request):
    if request.method == 'POST':
        form = BoardmembersForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Board Member has been Added'))
            return redirect('all-board-member')
        else: 
            messages.error(request, ('There is an Error Adding Board Member'))
            return render(request, 'app_admins/board-add.html')
    else:   
        return render(request, 'app_admins/board-add.html', {})
       
### SECTION RELATING TO CORPORATE MEMBERS ###

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def all_corp_member(request):
    context = corp_members.objects.all().order_by('corp_member_name')
    return render(request, 'app_admins/corp-member-all.html', { 'corp_members': context }) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_corp_member(request, list_id):
    if request.method == 'POST':
        corp_member = corp_members.objects.get(pk=list_id)
        form = CorpmembersForm(request.POST or None, instance=corp_member)
        if form.is_valid():
            form.save()
            messages.success(request, ('Corporate Member has been Edited'))
            return redirect('all-corp-member')
        else: 
            messages.error(request, ('There is an Error Editing the Corporate Member'))
            return redirect(request, 'app_admins/board-edit.html', {})
    else:
        get_corp_member = corp_members.objects.get(pk=list_id)
        return render(request, 'app_admins/corp-member-edit.html', { 'get_corp_member': get_corp_member, })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_corp_member(request):
    if request.method == 'POST':
        form = CorpmembersForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Corporate Member has been Added'))
            return redirect('all-corp-member')
        else: 
            messages.error(request, ('There is an Error Adding Board Member'))
            return render(request, 'app_admins/corp-member-add.html')
    else:   
        return render(request, 'app_admins/corp-member-add.html', {})  

### SECTION RELATING TO RESOURCES ###

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def all_resource(request):
    context = resources.objects.all().order_by('resource_name')
    return render(request, 'app_admins/resource-all.html', { 'resources': context }) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_resource(request, list_id):
    if request.method == 'POST':
        resource = resources.objects.get(pk=list_id)
        form = ResourcesForm(request.POST or None, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, ('Resources has been Edited'))
            return redirect('all-resource')
        else: 
            messages.error(request, ('There is an Error Editing the Resource'))
            return redirect(request, 'app_admins/resource-edit.html', {})
    else:
        get_resource = resources.objects.get(pk=list_id)
        return render(request, 'app_admins/resource-edit.html', { 'get_resource': get_resource, })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_resource(request): 
    if request.method == 'POST':
        form = ResourcesForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Resource has been Added'))
            return redirect('all-resource')
        else: 
            messages.error(request, ('There is an Error Adding Resource'))
            return render(request, 'app_admins/resource-add.html')
    else:   
        return render(request, 'app_admins/resource-add.html', {})  

### SECTION RELATING TO SPONSORS ###

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def all_sponsor(request):
    context = sponsors.objects.all().order_by('sponsor_name')
    return render(request, 'app_admins/sponsor-all.html', { 'all_sponsors': context }) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_sponsor(request, list_id):
    if request.method == 'POST':
        sponsor = sponsors.objects.get(pk=list_id)
        form = SponsorsForm(request.POST, request.FILES or None, instance=sponsor)
        if form.is_valid():
            form.save()
            messages.success(request, ('Sponsor has been Edited'))
            return redirect('all-sponsor')
        else: 
            messages.error(request, ('There is an Error Editing the Sponsor'))
            return redirect(request, 'app_admins/sponsor-edit.html', {})
    else:
        get_sponsor = sponsors.objects.get(pk=list_id)
        return render(request, 'app_admins/sponsor-edit.html', { 'get_sponsor': get_sponsor, })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_sponsor(request):
    if request.method == 'POST':
        form = SponsorsForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Sponsor has been Added'))
            return redirect('all-sponsor')
        else: 
            messages.error(request, ('There is an Error Adding Sponsor'))
            return render(request, 'app_admins/sponsor-add.html')
    else:   
        return render(request, 'app_admins/sponsor-add.html', {})  

### SECTION RELATING TO OTHER PAGES ###

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def all_page(request):
    context = pages.objects.all().order_by('page_name')
    return render(request, 'app_admins/page-all.html', { 'all_pages': context }) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_page(request, list_id):
    if request.method == 'POST':
        get_page = pages.objects.get(pk=list_id)
        form = PagesForm(request.POST or None, instance=get_page)
        if form.is_valid():
            form.save()
            messages.success(request, ('Page has been Edited'))
            return redirect('all-page')
        else: 
            messages.error(request, ('There is an Error Editing the Page'))
            return redirect(request, 'app_admins/page-edit.html', {})
    else:
        get_page = pages.objects.get(pk=list_id)
        return render(request, 'app_admins/page-edit.html', { 'get_page': get_page })

### SECTION RELATING TO CONTACT EMAILS ###

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def contacts(request):
    context = contact.objects.all().order_by('-date_added')
    return render(request, 'app_admins/contact-all.html', { 'all_contacts': context }) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def view_contact(request, list_id):
    context = contact.objects.get(pk=list_id)
    return render(request, 'app_admins/contact-view.html', { 'view_contact': context })

### SECTION RELATING TO META DATA ###

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def all_meta(request):
    context = meta.objects.all().order_by('meta_page')
    return render(request, 'app_admins/meta-all.html', { 'all_meta': context }) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_meta(request, list_id):
    if request.method == 'POST':
        get_meta = meta.objects.get(pk=list_id)
        form = MetaForm(request.POST, request.FILES or None, instance=get_meta)
        if form.is_valid():
            form.save()
            messages.success(request, ('Meta Data has been Edited'))
            return redirect('all-meta')
        else: 
            messages.error(request, ('There is an Error Editing the Meta Data'))
            return redirect(request, 'app_admins/meta-edit.html', {})
    else:
        get_meta = meta.objects.get(pk=list_id)
        return render(request, 'app_admins/meta-edit.html', { 'get_meta': get_meta })

## GENERAL DELETE FUNCTION ###

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_item(request, path, list_id):
    if request.method == 'POST':
        if path == 'corporate-members':
            corp_member = corp_members.objects.get(pk=list_id)
            corp_member.delete()
            messages.success(request, ('Corporate Member has been Deleted'))
            return redirect('all-corp-member') 
        elif path == 'board':
            board_member = board_members.objects.get(pk=list_id)
            board_member.delete()
            messages.success(request, ('Board Member has been Deleted'))
            return redirect('all-board-member')   
        elif path == 'resources':
            resource = resources.objects.get(pk=list_id)
            resource.delete()
            messages.success(request, ('Resource has been Deleted'))
            return redirect('all-resource')
        elif path == 'sponsor':
            sponsor = sponsors.objects.get(pk=list_id)
            sponsor.delete()
            messages.success(request, ('Sponsor has been Deleted'))
            return redirect('all-sponsor')  
    return redirect('')









