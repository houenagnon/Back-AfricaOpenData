from django.urls import path

import themes.views

app_name = 'themes'

urlpatterns = [
    path('', themes.views.test),
]