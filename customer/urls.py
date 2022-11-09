from django.urls import path
from. import views

urlpatterns=[
  path('chome',views.home),
  path('clogin',views.login),
  path('cbookshelf',views.bookshelf),
  path('caudiobook',views.audiobook),
  path('ccontact',views.contact),
]