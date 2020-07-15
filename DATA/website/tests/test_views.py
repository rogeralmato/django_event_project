from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User

import json
import website.views as views
from website.models import Event, EventState

class TestViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.user = User.objects.create_user(username='testusername', password='test_pass', email='testemail@email.com')
        self.state = EventState.objects.create(
            state='public'
        )
        self.event = Event.objects.create(
            title="Title title",
            description="aaaaaasasaasasasasasassasasasasasa",
            exerpt="",
            state=self.state,
            author=self.user
        )
        self.event.save()

        self.home_url = reverse('home') 
        self.user_event_url = reverse('user_event')
        self.event_detail_url = reverse('event_detail', kwargs={'pk':self.event.id})
        self.user_draft_event_url = reverse('user_draft_event')
        self.add_event_url = reverse('add_event')
        self.update_event_url = reverse('update_event', kwargs={'pk':self.event.id})
        self.delete_event_url = reverse('delete_event', kwargs={'pk':self.event.id})

    def tearDown(self):
        self.user.delete()
        self.event.delete()

    def test_HomeView_GET(self):
        request = self.factory.get(self.home_url)
        request.user = self.user
        response = views.UserEventView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_UserEventView_GET(self):
        request = self.factory.get(self.user_event_url)
        request.user = self.user
        response = views.UserEventView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_UserDraftEventView_GET(self):
        request = self.factory.get(self.user_draft_event_url)
        request.user = self.user
        response = views.UserDraftEventView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_EventDetailView_GET(self):
        request = self.factory.get(self.event_detail_url)
        request.user = self.user
        kwargs = {'pk':self.event.id}
        response = views.EventDetailView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)

    def test_AddEventView_GET(self):
        request = self.factory.get(self.add_event_url)
        request.user = self.user
        response = views.UserDraftEventView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_UpdateEventView_GET(self):
        request = self.factory.get(self.update_event_url)
        request.user = self.user
        kwargs = {'pk':self.event.id}
        response = views.EventDetailView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)

    def test_DeleteEventView_GET(self):
        request = self.factory.get(self.delete_event_url)
        request.user = self.user
        kwargs = {'pk':self.event.id}
        response = views.EventDetailView.as_view()(request, **kwargs)
        self.assertEqual(response.status_code, 200)


    

    
    