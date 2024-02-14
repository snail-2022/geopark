from django.urls import path

from . import views

urlpatterns = [
    path('', views.toLogin_view),
    path('index/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('main/', views.main_page, name='main_page'),
    path('main1/', views.main, name='main'),
    path('get_worldgeopark_data/', views.get_worldgeopark_data, name='get_worldgeopark_data'),

]
