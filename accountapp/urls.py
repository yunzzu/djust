from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccCreate, AccDetail

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccCreate.as_view(), name='create'),          #class형
    path('detail/<int:pk>', AccDetail.as_view(), name='detail'),  #특정 유저의 primary key가 필요함
]