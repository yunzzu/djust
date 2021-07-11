from django.urls import path

from commentapp.views import CmCreateView, CmDeleteView

app_name = 'commentapp'

urlpatterns = [
    path('create/', CmCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CmDeleteView.as_view(), name='delete'),
]