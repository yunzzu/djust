
from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import AcCreateView, AcDetailView, AcUpdateView, AcDeleteView, AcListView

app_name = 'articleapp'

urlpatterns = [
    path('list/', AcListView.as_view(), name='list'),
    path('create/', AcCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AcDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AcUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AcDeleteView.as_view(), name='delete'),
]