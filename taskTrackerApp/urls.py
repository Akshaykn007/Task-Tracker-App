from django.urls import path

# from taskTrackerApp.models import Team
from .views import *
from django.urls import re_path
from . import views
urlpatterns = [
    path('ping',PingAPI.as_view()),
    path('team',CreateTeam.as_view()),
    path('availability', TeamAvailability.as_view()),
    path('task',CreateTask.as_view()),
    path('task/<int:task_id>/<str:field>',TaskEditor.as_view()),
    re_path(r'^report/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[\w-]+)/$',TaskUpdates.as_view())
]