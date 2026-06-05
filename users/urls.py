from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='reg'),
    path('login/', views.auth_login_view, name='log'),
    path('logout/', views.auth_logout_view, name='unlog'),
    path('user_list/', views.user_list_view, name='us_lst')
]