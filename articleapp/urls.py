
from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import AcCreateView, AcDetailView, AcUpdateView, AcDeleteView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('create/', AcCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AcDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AcUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AcDeleteView.as_view(), name='delete'),
]