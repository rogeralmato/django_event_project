from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class EventState(models.Model):
    state = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.state

    def get_absolute_url(self):
        return reverse('home')

class EventSubscription(models.Model):
    assistant = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, default=None)
    
    def clean(self):
        super(EventSubscription, self).clean()
        if self.email is None and self.assistant is None:
            raise ValidationError('Error! Please fill the fields.')

class Event(models.Model):
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
        return reverse('home')

    @property
    def total_subs(self):
        """
        Get the total users subscrived for an event
        :return: Integer: Total subs of the event
        """
        self.subscriptions.count()



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile/', default='images/profile/default_profile.png')

    def __str__(self):
        return str(self.user)

