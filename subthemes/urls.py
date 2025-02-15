from django.urls import path
from .views import SubthemeListCreateAPIView, SubthemeDetailAPIView

urlpatterns = [
    path('theme/<uuid:theme_id>/', SubthemeListCreateAPIView.as_view(), name='subtheme-list-create'),
    path('subthemes/<uuid:id>/', SubthemeDetailAPIView.as_view(), name='subtheme-detail'),
]
