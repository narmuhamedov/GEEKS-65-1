from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('persons_mk/', views.persons_mk_view, name='persons_mk'),
]
