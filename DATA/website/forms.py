from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    For for creating a new Event.
    Args:
        forms 

    Returns:
        Form
    """
    class Meta:
        model = Event
        fields = ('title', 'state', 'exerpt', 'description', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'exerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def clean(self):
        # Function to test the values of the form
        super(EventForm, self).clean()
        
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            self._errors['description'] = self.error_class(['A minimum description of the event is required.'])
        return self.cleaned_data



class UpdateEventForm(forms.ModelForm):
    """
    For for updating an Event.
    Args:
        forms 

    Returns:
        Form
    """
    class Meta:
        model = Event
        fields = ('title', 'state', 'exerpt', 'description', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'exerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

