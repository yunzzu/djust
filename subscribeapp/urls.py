
from django.urls import path
from subscribeapp.views import SubView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubView.as_view(), name='subscribe'),
]