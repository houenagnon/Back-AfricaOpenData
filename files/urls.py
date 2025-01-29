from django.urls import path

import files.views

app_name = 'files'

urlpatterns = [
    path('', files.views.test),
]