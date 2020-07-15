from django.test import SimpleTestCase
from django.urls import reverse, resolve
import website.views as views

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        resolver = resolve(reverse('home'))
        self.assertEquals(resolver.func.view_class, views.HomeView)

    def test_event_detail_url_is_resolved(self):
        resolver = resolve(reverse('event_detail', args=[1]))
        self.assertEquals(resolver.func.view_class, views.EventDetailView)

    def test_add_event_url_is_resolved(self):
        resolver = resolve(reverse('add_event'))
        self.assertEquals(resolver.func.view_class, views.AddEventView)

    def test_update_event_url_is_resolved(self):
        resolver = resolve(reverse('update_event', args=[1]))
        self.assertEquals(resolver.func.view_class, views.UpdateEventView)

    def test_delete_event_url_is_resolved(self):
        resolver = resolve(reverse('delete_event', args=[1]))
        self.assertEquals(resolver.func.view_class, views.DeleteEventView)

    def test_filter_event_url_is_resolved(self):
        resolver = resolve(reverse('filter_event', args=['public']))
        self.assertEquals(resolver.func.view_class, views.FilterEventsByStateView)

    def test_user_event_url_is_resolved(self):
        resolver = resolve(reverse('user_event'))
        self.assertEquals(resolver.func.view_class, views.UserEventView)
        
    def test_sub_event_url_is_resolved(self):
        resolver = resolve(reverse('sub'))
        self.assertEquals(resolver.func, views.subscription_toggle)

    def test_user_draft_event_url_is_resolved(self):
        resolver = resolve(reverse('user_draft_event'))
        self.assertEquals(resolver.func.view_class, views.UserDraftEventView)

    

    
    
     