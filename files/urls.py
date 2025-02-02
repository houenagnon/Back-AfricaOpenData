from django.urls import path
from .views import FileList, FileDetail

urlpatterns = [
    path('', FileList.as_view(), name='file-list'),
    path('<uuid:pk>/', FileDetail.as_view(), name='file-detail'),
]
