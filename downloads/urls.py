from django.urls import path

from downloads.views import DownloadList, DownloadDetail

urlpatterns = [
    path('', DownloadList.as_view(), name='download-list'),
    path('<uuid:pk>/', DownloadDetail.as_view(), name='download-detail'),
]
