from django.test import TestCase
from website.forms import EventForm, UpdateEventForm
from website.models import EventState

class TestForms(TestCase):

    # -----------------------------
    # -------EventFormTests--------
    # -----------------------------

    def test_event_form_valid_data(self):
        state = EventState.objects.create(
            state='public'
        )
        form = EventForm(data={
            'title': 'Title for the event',
            'state': state,
            'exerpt': 'Short exerpt for the event',
            'description': 'This is the long description of this awesome event.'
        })

        self.assertTrue(form.is_valid())

    def test_event_form_no_data(self):
        form = EventForm(data={

        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


    
    # -----------------------------
    # ----UpdateEventFormTests-----
    # -----------------------------

    def test_update_event_form_valid_data(self):
        state = EventState.objects.create(
            state='public'
        )
        form = EventForm(data={
            'title': 'Title for the event',
            'state': state,
            'exerpt': 'Short exerpt for the event',
            'description': 'This is the long description of this awesome event.'
        })

        self.assertTrue(form.is_valid())

    def test_update_event_form_no_data(self):
        form = EventForm(data={

        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)