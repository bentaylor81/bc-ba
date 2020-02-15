from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('who-are-we/', views.who_are_we, name='who-are-we'),
    path('events/', views.events, name='events'),
    path('membership/', views.membership, name='membership'),
    path('membership-types/', views.membership_types, name='membership-types'),
    path('member-directory/', views.member_directory, name='member-directory'),
    path('sponsorship/', views.sponsorship, name='sponsorship'),
    path('current-sponsors/', views.sponsors_current, name='sponsors-current'),
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
]
