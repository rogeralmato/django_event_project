from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class EventState(models.Model):
    """
    EventState model to represent a state of the events

    Args:
        state: string which is an state

    Returns:
        [EventState]: Returns an EventState
    """
    state = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.state

    def get_absolute_url(self):
        return reverse('home')

class EventSubscription(models.Model):
    """
    EventSubscription model to represent subscriptions of events in the web app

    Args:
        assistant: registered user or Null, who has subscrived to the event
        comment: comment of the subscription details
        email: email of the person who has registered to the email

    Raises:
        ValidationError: if assistant and email is None
        
    Returns:
        [EventSubscription]: Returns an EventSubscription
    """
    assistant = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, default=None)
    
    def clean(self):
        super(EventSubscription, self).clean()
        if self.email is None and self.assistant is None:
            raise ValidationError('Error! Please fill the fields.')

class Event(models.Model):
    """
    Event model to represent an event in the web app

    Args:
        title: title of the event
        author: author of the event, OneToMany relationship with User model
        description: description of the event
        exerpt: short description of the event to be shown at home page
        header_image: image that represents the event
        publication_date: when is the event published
        state: OneToMany relationship with the EventState Model
        subscriptions: ManyToManyRelationship with the EventSubscriptions Model

    Returns:
        [Event]: Returns an Event
    """
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    exerpt = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default_image.png') # in a production enviroment that would be an aws media storage or similar
    publication_date = models.DateField(auto_now_add=True)
    state = models.ForeignKey(EventState, on_delete=models.CASCADE, default='public')
    subscriptions = models.ManyToManyField(EventSubscription)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        """
        Get the absolute url to return to home page when viewing an event.
        Returns: Url path to home page
        """
        return reverse('home')

    @property
    def total_subs(self):
        """
        Get the total users subscrived for an event
        Returns: Integer: Total subs of the event
        """
        self.subscriptions.count()



class Profile(models.Model):
    """
    Profile Model used for extending the Django default User Model.

    Args:
        user: django default auth model (one to one relation)
        bio: short description of the user bio
        profile_pic: profile picture of the user

    Returns:
        [Profile]: Returns a Profile
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile/', default='images/profile/default_profile.png')

    def __str__(self):
        return str(self.user)

