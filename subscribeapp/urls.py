
from django.urls import path
from subscribeapp.views import SubView, SubListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubView.as_view(), name='subscribe'),
    path('list/', SubListView.as_view(), name='list'),
]