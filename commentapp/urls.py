from django.urls import path

from commentapp.views import CmCreateView

app_name = 'commentapp'

urlpatterns = [
    path('create/', CmCreateView.as_view(), name='create'),
]