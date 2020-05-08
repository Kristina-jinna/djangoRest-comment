from django.urls import path

from .views import GroupView

app_name = "articles"

urlpatterns = [
    path('groups/', GroupView.as_view()),
    path('groups/<int:pk>',GroupView.as_view()),
]
