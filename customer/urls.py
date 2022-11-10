from django.urls import path
from. import views
app_name='customer'

urlpatterns=[
  path('chome',views.home,name='home'),
  path('clogin',views.login,name='login'),
  path('cbookshelf',views.bookshelf,name='bookshelf'),
  path('caudiobook',views.audiobook,name='audiobook'),
  path('ccontact',views.contact,name='contact'),
]