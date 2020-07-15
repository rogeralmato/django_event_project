from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from django.contrib.auth.models import User

from .forms import SignUpForm, EditUserForm, PasswordChangingForm, SignUpProfileForm, EditProfileForm

from website.models import Profile, Event

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
"""
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    """

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        profile_form = SignUpProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        form = SignUpForm()
        profile_form = SignUpProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/register.html', context)

def edit_settings(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, instance=user.profile)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('home')
    else:
        form = EditUserForm(instance=user)
        profile_form = EditProfileForm(instance=user.profile)

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/edit_settings.html', context)

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        events = Event.objects.filter(author__id = page_user.user_id)
        num_public = events.filter(state__state = 'public').count()
        num_private = events.filter(state__state = 'private').count()
        num_draft = events.filter(state__state = 'draft').count()
        
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        context['page_user'] = page_user
        context['num_public_events'] = num_public
        context['num_private_events'] = num_private
        context['num_draft_events'] = num_draft
        return context

