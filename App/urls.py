from django.urls import path
from .views import Home,About,Schedule,Portfolio

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('schedule/', Schedule.as_view(), name='schedule'),
    path('portfolio/', Portfolio.as_view(), name='portfolio'),
]