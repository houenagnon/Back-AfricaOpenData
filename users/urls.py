from django.urls import path

import users.views

app_name = 'users'

urlpatterns = [
    path('', users.views.UserList.as_view()),
]