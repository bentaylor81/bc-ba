from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('member-directory/', views.directory_of_members, name='member-directory'), 
    path('current-sponsors/', views.resources, name='current-sponsors'),
    path('resources/', views.resources, name='resources'),
    path('who-are-we/', views.who_are_we, name='who-are-we'),
    path('add-board-member/', views.add_board_member, name='add-board-member'), 
    path('edit-board-member/<list_id>', views.edit_board_member, name="edit-board-member"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('<page_path>/', views.page, name='pages'), 
]

