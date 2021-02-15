from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.pageindex, name='pageindex'),
]
