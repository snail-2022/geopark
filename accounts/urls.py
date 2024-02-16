from django.urls import path

from . import views

urlpatterns = [
    path('', views.toLogin_view),
    path('index/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('main/', views.main_page, name='main_page'),
    path('get_worldgeopark_data/', views.get_worldgeopark_data, name='get_worldgeopark_data'),
    path('manage/', views.manage_page, name='manage_page'),
    path('add/', views.add_page, name='add_page'),
    path('search/', views.search_page, name='search_page'),
    path('delete/', views.detele_page, name='detele_page'),
    path('list/', views.list_page, name='list_page'),
    path('toadd/', views.add_worldgeopark),
    path('success/', views.success_page,name='success_page'),
    path('todelete/', views.delete_worldgeopark),

]
