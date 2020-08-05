from django urls import path
from . import views

app_name='introduction'
url patterns = [
        path('', views.profile, name="profile"),
]