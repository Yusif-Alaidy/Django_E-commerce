from django.urls import path
from . import views 
app_name = 'accounts'
urlpatterns = [
    path('join_us', views.join_us, name='join_us'),
    path('logout', views.logout_user, name='logout')
]
