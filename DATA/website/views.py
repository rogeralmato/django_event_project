from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.template import RequestContext

import json

from .models import Event, EventState, User, EventSubscription
from .forms import EventForm, UpdateEventForm


class HomeView(ListView):
    """
    Class based view for the home view.

    Args:
        model: Event
        template_name:homeview.html

    """
    model = Event
    template_name = 'homeview.html'
    
    def get_queryset(self):
        # Query the public events if not logged in and also the private ones if logged in
        ordering = ['-publication_date', '-id']
        if self.request.user.is_authenticated:
            return Event.objects.filter(~Q(state__state = 'draft')).order_by(*ordering)
        else:
            return Event.objects.filter(state__state = 'public').order_by(*ordering)
        

@method_decorator(login_required, name='dispatch')
class UserEventView(ListView):
    """
    Class based view for the events of a particular User.

    Args:
        model: Event
        template_name:homeview.html
        
    """
    model = Event
    template_name = 'homeview.html'
    
    def get_queryset(self):
        # Query the events of the user which are not draft
        ordering = ['-publication_date', '-id']
        return Event.objects.filter(author__id = self.request.user.id).filter(~Q(state__state = 'draft')).order_by(*ordering)

@method_decorator(login_required, name='dispatch')
class UserDraftEventView(ListView):
    """
    Class based view for the drafts events of a particular User.

    Args:
        model: Event
        template_name:homeview.html
        
    """
    model = Event
    template_name = 'homeview.html'
    
    def get_queryset(self):
        # Query only the events of the corresponding user
        ordering = ['-publication_date', '-id']
        return Event.objects.filter(author__id = self.request.user.id).filter(state__state = 'draft').order_by(*ordering)

class EventDetailView(UserPassesTestMixin, DetailView):
    """
    Class based view for the page of a particular event. 

    Args:
        model: Event
        template_name:event_details.html
        
    """
    model = Event
    template_name = 'event_details.html'

    def test_func(self):
        # Function to make sure that the person who is accessing an event has permisions to do it.
        event = self.get_object()
        if self.request.user.is_authenticated:
            return True
        else:
            return event.state.state == 'public' 

    def get_context_data(self, *args, **kwargs):
        # Function to add to context if the user has previously subscrived to the event or not
        context = super().get_context_data(**kwargs)
        subscrived = False
        event = get_object_or_404(Event, id=self.kwargs['pk'])
        if event.subscriptions.filter(assistant__id=self.request.user.id).exists():
            subscrived = True
        context['is_subscrived'] = subscrived
        return context

@method_decorator(login_required, name='dispatch')
class AddEventView(CreateView):
    """
    Class based view for creating a new event.

    Args:
        model: Event
        form_class = EventForm
        template_name:add_event.html
        
    """
    model = Event
    form_class = EventForm
    template_name = 'add_event.html'

    def form_valid(self, form):
        # Function to check that the form is valid
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class UpdateEventView(UserPassesTestMixin, UpdateView):
    """
    Class based view for updating an event.

    Args:
        model: Event
        form_class = UpdateEventForm
        template_name:update_event.html
        
    """
    model = Event
    form_class = UpdateEventForm
    template_name = 'update_event.html'

    def test_func(self):
        # Function to test the access to the view
        return self.request.user.id == self.get_object().author.id

@method_decorator(login_required, name='dispatch')
class DeleteEventView(UserPassesTestMixin, DeleteView):
    """
    Class based view for delating an event.

    Args:
        model: Event
        template_name:delete_event.html
        
    """
    model = Event
    template_name = 'delete_event.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        # Function to test the access to the view
        return self.request.user.id == self.get_object().author.id


@login_required
def subscription_toggle(request):
    """
    Function to update the subscription to an event using a jquery function.
    The author is logged in.

    Args:
        request

    Returns:
        [int]: [num_subs] Number of subscrivers to the event
        [bool]: [sub_status] If the user is subscrived or unsubscrived
        [str]: [email] Email of the person subscrived
        
    """
    context = RequestContext(request)
    event_id = None
    sub_status = None
    num_subs = 0

    if request.method == 'GET':
        event_id = request.GET['event_id']
        sub_status = request.GET['subs_status'] == 'true'
        comment = request.GET['subs_comment']
    
    if event_id != None:
        event = Event.objects.get(id=int(event_id))
        user = User.objects.get(id=request.user.id)
        email = user.email
        if event:
            if sub_status:
                subs = event.subscriptions.get(assistant__id=user.id)
                event.subscriptions.remove(subs)
                subs.delete()
            else:
                event_subs = EventSubscription(assistant=user, comment=comment)
                event_subs.save()
                event.subscriptions.add(event_subs)
            event.save()
            sub_status = not sub_status
            num_subs = event.subscriptions.count()

    ctx = {'num_subs': num_subs, 'sub_status': sub_status, 'email': email}

    return HttpResponse(json.dumps(ctx), content_type='application/json')

def subscription_not_logged_toggle(request):
    """
    Function to update the subscription to an event using a jquery function.
    The author is not logged in.

    Args:
        request

    Returns:
        [int]: [num_subs] Number of subscrivers to the event
        
    """
    context = RequestContext(request)
    num_subs = 0
    if request.method == 'GET':
        event_id = request.GET['event_id']
        email = request.GET['subs_email']
        comment = request.GET['subs_comment']
    
    if event_id != None:
        event = Event.objects.get(id=int(event_id))
        if event:
            event_subs = EventSubscription(assistant=None, comment=comment, email=email)
            event_subs.save()
            event.subscriptions.add(event_subs)
            event.save()
            num_subs = event.subscriptions.count()

    ctx = {'num_subs': num_subs}

    return HttpResponse(json.dumps(ctx), content_type='application/json')