from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 

    path('board/', views.all_board_member, name='all-board-member'),
    path('board/edit/<list_id>', views.edit_board_member, name='edit-board-member'),
    path('board/add/', views.add_board_member, name='add-board-member'), 

    path('corporate-members/', views.all_corp_member, name='all-corp-member'),
    path('corporate-members/edit/<list_id>', views.edit_corp_member, name='edit-corp-member'),
    path('corporate-members/add/', views.add_corp_member, name='add-corp-member'),

    path('resources/', views.all_resource, name='all-resource'),
    path('resources/edit/<list_id>', views.edit_resource, name='edit-resource'),
    path('resources/add/', views.add_resource, name='add-resource'),

    path('sponsors/', views.all_sponsor, name='all-sponsor'),
    path('sponsors/edit/<list_id>', views.edit_sponsor, name='edit-sponsor'),
    path('sponsors/add/', views.add_sponsor, name='add-sponsor'),

    path('pages/', views.all_page, name='all-page'),
    path('pages/edit/<list_id>', views.edit_page, name='edit-page'),
  
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<list_id>', views.view_contact, name='view-contact'),

    path('meta/', views.all_meta, name='all-meta'),
    path('meta/edit/<list_id>', views.edit_meta, name='edit-meta'),

    path('<path>/delete/<list_id>', views.delete_item, name='delete-item'),
   ]
