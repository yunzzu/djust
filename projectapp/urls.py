
from django.urls import path
from projectapp.views import PjListView, PjCreateView, PjDetailView

app_name = 'projectapp'

urlpatterns = [
    path('list/', PjListView.as_view(), name='list'),
    path('create/', PjCreateView.as_view(), name='create'),
    path('detail/<int:pk>', PjDetailView.as_view(), name='detail'),
]