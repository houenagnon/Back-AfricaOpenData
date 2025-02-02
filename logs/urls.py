from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from logs import views


urlpatterns = [
    path('',views.LogList.as_view()),
    path('<uuid:pk>/', views.LogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)