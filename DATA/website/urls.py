from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('event/<int:pk>', EventDetailView.as_view(), name="event_detail"),
    path('event/new', AddEventView.as_view(), name='add_event'),
    path('event/<int:pk>/update', UpdateEventView.as_view(), name="update_event"),
    path('event/<int:pk>/delete', DeleteEventView.as_view(), name="delete_event"),
    path('event/user', UserEventView.as_view(), name="user_event"),
    path('event/subscription', subscription_toggle, name="sub"),
    path('event/subscription_not_logged', subscription_not_logged_toggle, name="sub_not_logged"),
    path('event/user_draft', UserDraftEventView.as_view(), name="user_draft_event"),
]
