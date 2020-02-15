from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def who_are_we(request):
    return render(request, 'who-are-we.html', {})

def events(request):
    return render(request, 'events.html', {})

def membership(request):
    return render(request, 'membership.html', {})

def membership_types(request):
    return render(request, 'membership-types.html', {})

def member_directory(request):
    return render(request, 'member-directory.html', {})

def sponsorship(request):
    return render(request, 'sponsorship.html', {})

def sponsors_current(request):
    return render(request, 'sponsors-current.html', {})

def resources(request):
    return render(request, 'resources.html', {})

def contact(request):
    return render(request, 'contact.html', {})
