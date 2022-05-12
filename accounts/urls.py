from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard/create_contact/', views.dashboard_create, name= 'dashcreate'),
    path('dashboard/vercontato/<int:contato_id>', views.ver_contato, name ='ver_contato' ),
    path('dashboard/vercontato/<int:contato_id>/edit', views.edit_contato, name='edit_contato'),
    path('dashboard/vercontato/<int:contato_id>/excluir', views.excluir_contato, name='excluir_contato'),
    path('dashboard/busca/', views.busca, name='busca'),
] 