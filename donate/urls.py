from donate.views import(home_View)
from django.urls import path


app_name = 'dnd'

urlpatterns = [
    path("", home_View.as_view(), name='home')
]