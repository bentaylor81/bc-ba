from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('member-directory/', views.directory_of_members, name='member-directory'), 
    path('current-sponsors/', views.current_sponsors, name='current-sponsors'),
    path('resources/', views.resources_page, name='resources'),
    path('who-are-we/', views.who_are_we, name='who-are-we'),
    path('<page_path>/', views.page, name='pages'), 
]

