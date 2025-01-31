from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from themes import views


urlpatterns = [
    path('',views.ThemeList.as_view()),
    path('<uuid:pk>/', views.ThemeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)