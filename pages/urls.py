from django.urls import path
from . import views

#   TODO: убрать гравную страницу
urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.pageindex, name='pageindex'),
]
