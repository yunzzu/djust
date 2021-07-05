from django.urls import path

from accountapp.views import hello_world, AccCreate

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),
    path('create/', AccCreate.as_view(), name='create'),  #class형
]