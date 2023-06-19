from django.urls import path
from .views import file_upload_view, TextDetailView

app_name = 'pdf2textapp'

urlpatterns = [
    path('', file_upload_view, name='upload-pdf'),
    path('detail/<int:pk>/', TextDetailView.as_view(), name='pdf-info'),
]
