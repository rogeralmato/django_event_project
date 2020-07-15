from django.test import TestCase
from django.contrib.auth.models import User

from website.models import Event, EventState, EventSubscription, Profile

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testusername', password='test_pass', email='testemail@email.com')
        self.state = EventState.objects.create(
            state='public'
        )
        self.event = Event.objects.create(
            title="Test title",
            description="This is a test description for the event.",
            exerpt="This is a short exerpt.",
            state=self.state,
            author=self.user
        )
        self.event.save()

    def tearDown(self):
        self.user.delete()
        self.event.delete()



    # -----------------------------
    # ---------EventTests----------
    # -----------------------------

    def test_event_state(self):
        self.assertEquals(self.event.state, self.state)

    def test_event_author(self):
        self.assertEquals(self.event.author, self.user)

    def test_event_title(self):
        self.assertEquals(self.event.title, "Test title")

    def test_event_description(self):
        self.assertEquals(self.event.description, "This is a test description for the event.")

    def test_event_exerpt(self):
        self.assertEquals(self.event.exerpt, "This is a short exerpt.")

    def test_event_subs_count_property(self):
        subscription_one = EventSubscription.objects.create(
            assistant=self.user,
            comment="User is going!"
        )
        subscription_two = EventSubscription.objects.create(
            assistant=self.user,
            comment="User is going!"
        )
        subscription_three = EventSubscription.objects.create(
            assistant=self.user,
            comment="User is going!"
        )
        event = Event.objects.create(
            title="Test title",
            description="This is a test description for the event.",
            exerpt="This is a short exerpt.",
            state=self.state,
            author=self.user
        )
        event.save()
        event.subscriptions.set([subscription_one, subscription_two, subscription_three])
        self.assertEquals(event.subscriptions.count(), 3)
        event.delete()



    # -----------------------------
    # ---EventSubscriptionTests----
    # -----------------------------

    def test_event_subscription_assistant(self):
        subscription_one = EventSubscription.objects.create(
            assistant=self.user,
            comment="User is going!"
        )
        self.assertEquals(subscription_one.assistant, self.user)

    def test_event_subscription_comment(self):
        subscription_one = EventSubscription.objects.create(
            assistant=self.user,
            comment="User is going!"
        )
        self.assertEquals(subscription_one.comment, "User is going!")



    # -----------------------------
    # -------EventStateTests-------
    # -----------------------------

    def test_event_state_state(self):
        self.assertEquals(self.state.state, 'public')



    # -----------------------------
    # --------ProfileTests---------
    # -----------------------------

    def test_profile_user(self):
        profile = Profile.objects.create(
            user=self.user,
            bio="This is the test user bio"
        )
        self.assertEquals(profile.user, self.user)

    def test_profile_bio(self):
        profile = Profile.objects.create(
            user=self.user,
            bio="This is the test user bio"
        )
        self.assertEquals(profile.bio, "This is the test user bio")

