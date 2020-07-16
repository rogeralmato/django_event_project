# DJANGO PROJECT
This is a Django Events site project. The main idea is to create a site where users can post, see and subscribe to events. All the functionalities are listed below:
* Users Need to be able to register and login.
* Users can post an event.
* Only Authenticated users should be able to post an event.
* An event should have a title, description, date, author, and a state.
* The state of an event can be:
* "Draft" -> unpublished
* "Public" -> public and everyone can see it.
* "Private" -> only logged in users can see it.
* A page to display all events is required. The list of events will have a link on each event to its details page.
* Another page will display an event's full details along with a subscription form at the bottom of the page to add an event_subscription.
* An event subscription contains the user name, email and "comment".
* The app needs to support at least one language other than the default English language.

**TABLE OF CONTENTS**
- [DJANGO PROJECT](#django-project)
  - [Project Structure](#project-structure)
    - [Django](#django)
    - [Docker](#docker)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation](#installation-1)
    - [Deployment](#deployment)
  - [Interface Description](#interface-description)
    - [Home Page](#home-page)
    - [Login Page](#login-page)
    - [Register Page](#register-page)
    - [Change Password And Change user info](#change-password-and-change-user-info)
    - [Create Event](#create-event)
    - [User Events](#user-events)
    - [Profile](#profile)
  - [System Architecture](#system-architecture)
    - [Project Container (django)](#project-container-django)
    - [Postgress Container](#postgress-container)
    - [Selenium Hub Container](#selenium-hub-container)
    - [Desktop Chrome Selenium node](#desktop-chrome-selenium-node)
    - [Desktop Firefox Selenium node](#desktop-firefox-selenium-node)
  - [Django Project Arhitecture](#django-project-arhitecture)
    - [Website Django App](#website-django-app)
    - [Authentification Django App](#authentification-django-app)
    - [Functional tests Folder](#functional-tests-folder)
  - [Django Project Models](#django-project-models)
    - [Event Model (website)](#event-model-website)
    - [EventState Model (website)](#eventstate-model-website)
    - [EventSubscription Model (website)](#eventsubscription-model-website)
    - [Profile Model (website)](#profile-model-website)
    - [User Model (authentification)](#user-model-authentification)
  - [Django Project Views](#django-project-views)
    - [Home View](#home-view)
    - [User Draft Events View](#user-draft-events-view)
    - [Event Detail View](#event-detail-view)
    - [Add Event View](#add-event-view)
    - [Update Event View](#update-event-view)
    - [Delete Event View](#delete-event-view)
  - [Django Project Forms](#django-project-forms)
    - [Event Form (website app)](#event-form-website-app)
    - [Update Event Form (website app)](#update-event-form-website-app)
    - [Create User Form (authentification app)](#create-user-form-authentification-app)
    - [Create Profile Form (authentification app)](#create-profile-form-authentification-app)
    - [Edit Profile Form (authentification app)](#edit-profile-form-authentification-app)
    - [Password Change Form (authentification app)](#password-change-form-authentification-app)
  - [Django Unit Tests](#django-unit-tests)
  - [Django Functional Tests](#django-functional-tests)
  - [Frontend](#frontend)
    - [Theme Used](#theme-used)
    - [Client Side](#client-side)
  - [What's next?](#whats-next)
    - [Improving User Experience with React Components](#improving-user-experience-with-react-components)
    - [Scaling Django Web App](#scaling-django-web-app)
  - [Author](#author)

## Project Structure

The project is structured using `docker-compose`, running in different containers, as we will see in the following sections. 

The django part is inside it's own container and has a volume *DATA* (see DATA folder in the project tree). The same happens with the postgres container which keeps the data in another volume represented by the *postgres-data* folder. 

The tree of the project is the following:

```
opportiunity_network
├── DATA
│   ├── authentication
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── registration
│   │   │       ├── edit_settings.html
│   │   │       ├── login.html
│   │   │       ├── password.html
│   │   │       ├── profile.html
│   │   │       └── register.html
│   │   ├── urls.py
│   │   └── views.py
│   ├── functional_tests
│   │   ├── __init__.py
│   │   ├── test_website_home_page.py
│   │   └── test_website_login.py
│   ├── locale
│   │   └── es
│   │       └── LC_MESSAGES
│   │           ├── django.mo
│   │           └── django.po
│   ├── manage.py
│   ├── media
│   │   └── images
│   │       ├── ...
│   │       └── profile
│   │           └── ...
│   ├── opportiunity_network
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── static
│   │   ├── authentication
│   │   │   ├── css
│   │   │   │   └── styles.css
│   │   │   └── images
│   │   │       └── ...
│   │   ├── error_pages
│   │   │   └── css
│   │   │       └── style.css
│   │   └── website
│   │       ├── css
│   │       │   ├── cs-skin-elastic.css
│   │       │   ├── lib
│   │       │       └── ...
│   │       │   ├── style.css
│   │       │   └── style.css.map
│   │       ├── fonts
│   │       │   └── ...
│   │       ├── images
│   │       │   └──...
│   │       ├── js
│   │       │   ├── dashboard.js
│   │       │   ├── init
│   │       │   │   └── ...
│   │       │   ├── jquery.js
│   │       │   ├── lib
│   │       │   │   └── ...
│   │       │   ├── main.js
│   │       │   ├── rango-ajax.js
│   │       │   ├── vmap.sampledata.js
│   │       │   └── widgets.js
│   │       └── scss
│   │           ├── style.css
│   │           ├── style.css.map
│   │           └── style.scss
│   └── website
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── migrations
│       │   └── ...
│       ├── models.py
│       ├── templates
│       │   ├── 400.html
│       │   ├── 403.html
│       │   ├── 404.html
│       │   ├── 500.html
│       │   ├── add_event.html
│       │   ├── delete_event.html
│       │   ├── event_details.html
│       │   ├── home.html
│       │   ├── homeview.html
│       │   ├── includes
│       │   │   ├── footer.html
│       │   │   ├── header.html
│       │   │   └── leftsidebar.html
│       │   ├── layouts
│       │   │   ├── base.html
│       │   │   └── error.html
│       │   └── update_event.html
│       ├── tests
│       │   ├── __init__.py
│       │   ├── test_forms.py
│       │   ├── test_models.py
│       │   ├── test_url.py
│       │   └── test_views.py
│       ├── urls.py
│       └── views.py
├── Dockerfile
├── README.md
├── docker-compose.yml
├── postgres-data
└── requirements.txt
```

### Django
This project builds an event web platform to connect event organizers with the assitants. Django is used as a web framework to build the web app, and as a consequence all the project revolves around this part.

### Docker
The project is develop as a microservice hence Docker is used to contenerize the different parts of this project. The idea is that the Django web app could be scalable in the future.

Docker is also used to encapsulate the django project and all it's dependencies together, so the web app can easily be installed in another pc or server. 


## Installation
This section will give a coppy of this project up and running in your computer or server.

### Requirements
The only requirement is to hava a computer or server in which `Docker` can be installed. An installation guide for Docker can be found [HERE](https://docs.docker.com/engine/install/).

### Installation
Once docker is installed on your machine we can proceed with the project installation.

```
git clone https://github.com/rogeralmato/django_event_project.git
cd django_event_project
```

### Deployment
Finally, we can deploy the django project by:
```
docker-compose up -d
```
It will take a while to install all the project and containers dependencies. When it's done, in order to see the django project, in your browser go to:

[http://0.0.0.0:8000/](http://0.0.0.0:8000/)

![Home Page](https://i.ibb.co/Z8G9nxv/Screenshot-2020-07-16-at-09-39-42.png)

## Interface Description
In this section we will descripbe the interface features, even though the web has been develop to be easy to use.
### Home Page
![Home Page](https://i.ibb.co/HKcqbgB/Screenshot-2020-07-16-at-12-06-38.png)
Card:
![Home Page Card](https://i.ibb.co/N7045Km/Screenshot-2020-07-16-at-12-10-16.png)

### Login Page
![Login Page](https://i.ibb.co/5MyCzyT/Screenshot-2020-07-16-at-12-15-40.png)

### Register Page
Identical to Login Page

### Change Password And Change user info
Identical to Register Page

### Create Event
![Create account Page](https://i.ibb.co/8zM3FJP/Screenshot-2020-07-16-at-12-16-20.png)
![Create account Page](https://i.ibb.co/0XJ89hr/Screenshot-2020-07-16-at-12-16-29.png)

### User Events
Identical to Home Page

### Profile
![Profile account Page](https://i.ibb.co/82hThzB/Screenshot-2020-07-16-at-12-16-56.png)
![Profile account Page](https://i.ibb.co/TMP75Mx/Screenshot-2020-07-16-at-12-17-04.png)


## System Architecture
As we previously explained, the Django app is developed as a microservice for all it's benefits. The application is structured in 5 different containers:
* Django Container
* Postgres Container
* Selenium Hub Container
* Desktop Chrome Selenium node
* Desktop Firefox Selenium node

Docker-compose code:
```
version: '3'
    
services:
  db:
    image: postgres
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
      - ./postgres-data:/var/lib/postgresql/data
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    stdin_open: true
    tty: true
    volumes:
      - ./DATA:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
      - selenium_hub
      - selenium_chrome

  selenium_hub:
    container_name: selenium_hub
    image: selenium/hub
    ports:
      - "4444:4444"
  selenium_chrome:
    container_name: selenium_chrome
    image: selenium/node-chrome-debug
    environment:
      - HUB_HOST=selenium_hub
      - HUB_PORT=4444
    ports:
      - "5900:5900"
    depends_on:
      - selenium_hub
  selenium_firefox:
    container_name: selenium_firefox
    image: selenium/node-firefox-debug
    environment:
      - HUB_PORT_4444_TCP_ADDR=selenium_hub
      - HUB_PORT_4444_TCP_PORT=4444
    ports:
      - "5901:5900"
    depends_on:
      - selenium_hub

```

### Project Container (django)
Is the main container of the project and contains de Django web app and all it's dependences. We will go through all the details in the project architectures, models, views, forms, unit tests and functional tests sections.

Dockerfile of the container:
```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim
RUN apt-get install gettext -y

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000
STOPSIGNAL SIGINT
```

### Postgress Container
This is a database container which contains all the information for the django container. It has been separed from the django app in another container for the following reasons:
* Security: Separating the database in it's own container makes it more secure and we could also add more security firewalls...
* Back ups: We could also design a backup system to be added to the container.
* Real World: In a real world django app it is common to have the database externaly or even more than one database, which is another reason to keep it separatly in this project. 

### Selenium Hub Container
This cointainer is used for the functional tests together with the chrome and the firefox container. This container make's available the functional tests with different devices and webdrivers (Chrome, Firefox, safari...). We can see the structure:

![Selenium hub](https://www.selenium.dev/documentation/es/images/grid.png)

Selenium hub makes it easy to test the django app with different devices and browsers.

### Desktop Chrome Selenium node
Container which contains all the dependences to act as a webdriver for a selenium functional test acting like a desktop computer with chrome browser.

### Desktop Firefox Selenium node
Container which contains all the dependences to act as a webdriver for a selenium functional test acting like a desktop computer with firefox browser.

## Django Project Arhitecture
In this section we will go through the django apps inside the django project. Django structure is intended to separate the functionalities over different apps in the same project.

### Website Django App
This is the main app and contains all the development for the website and events.

### Authentification Django App
The project uses the default Django authentification system because it is very secure and elaborated. It has been develop in separeted app. It is true that in the website django app the `auth` model has been extended, but the login and registration is being done with the defualt django auth mdoel.

### Functional tests Folder
This folder contains all the functional test using the selenium-hub container. It tests all the main features of the app. 

## Django Project Models 
As we said previously, the django project has two apps, one for the website and the other one for the django authentification system. In this section we will go through the models in the django website app.

### Event Model (website)
```
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
```
The Event model has all the information which an event needs. Point out that it has a OneToMany (`ForeignKey`) relationship with the State model and a ManyToMany relationship with the EventSubscription model.

### EventState Model (website)
```
class EventState(models.Model):
    state = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.state

    def get_absolute_url(self):
        return reverse('home')
```
The EventState model has only a state field. It contains three possible EventState in the database: public, private or draft. The users cannot add or delete any of the those three EventState.

### EventSubscription Model (website)
```
class EventSubscription(models.Model):
    assistant = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, default=None)
    
    def clean(self):
        super(EventSubscription, self).clean()
        if self.email is None and self.assistant is None:
            raise ValidationError('Error! Please fill the fields.')
```
The EventSubscription comes from a many to many relationship with the Events. The `clean` function ensures that or either the user is logged in (for which we have his/her credentials) or gives the email.  

### Profile Model (website)
```
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile/', default='images/profile/default_profile.png')

    def __str__(self):
        return str(self.user)
```
As we previously said, the `user (django auth)` model has been extended in order to add information to users. To do that, a OneToOne relationship has been used for the user, and a bio and an profile pictures field has been added.

### User Model (authentification)
From the authentification app in the django project, we have the default `auth` model from django.

## Django Project Views
Another part in a django project are the views. For the views, the project only uses class based views. 

### Home View
```
class HomeView(ListView):
    model = Event
    template_name = 'homeview.html'
    
    def get_queryset(self):
        ordering = ['-publication_date', '-id']
        if self.request.user.is_authenticated:
            return Event.objects.filter(~Q(state__state = 'draft')).order_by(*ordering)
        else:
            return Event.objects.filter(state__state = 'public').order_by(*ordering)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        subscriptions = EventSubscription.objects.all()
        context['subscriptions'] = subscriptions
        return context
```
It is a class based views which inherits from the ListView. It has a `get_queryset` method in order to filter the Event types if the user is authenticated or not.

### User Events View
```
@method_decorator(login_required, name='dispatch')
class UserEventView(ListView):
    model = Event
    template_name = 'homeview.html'
    
    def get_queryset(self):
        ordering = ['-publication_date', '-id']
        return Event.objects.filter(author__id = self.request.user.id).filter(~Q(state__state = 'draft')).order_by(*ordering)
```
It is a class based view which requires the user to be logged in. It has a `get_queryset` method to get all the user events which are not draft.

### User Draft Events View
```
@method_decorator(login_required, name='dispatch')
class UserDraftEventView(ListView):
    model = Event
    template_name = 'homeview.html'
    
    def get_queryset(self):
        ordering = ['-publication_date', '-id']
        return Event.objects.filter(author__id = self.request.user.id).filter(state__state = 'draft').order_by(*ordering)
```
Similar to the previous view, but it displays the user draft events.

### Event Detail View
```
class EventDetailView(UserPassesTestMixin, DetailView):
    model = Event
    template_name = 'event_details.html'

    def test_func(self):
        event = self.get_object()
        if self.request.user.is_authenticated:
            return True
        else:
            return event.state.state == 'public' 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        subscrived = False
        event = get_object_or_404(Event, id=self.kwargs['pk'])
        if event.subscriptions.filter(assistant__id=self.request.user.id).exists():
            subscrived = True
        context['is_subscrived'] = subscrived
        return context
```
This class based view displays the details of an event. It has a `test_func`, which ensures that if the user is not logged in, the event is 'public'. The `get_context_data` method is used for telling to the view if the user has been subscrived to this event previously (if logged in).

### Add Event View
```
@method_decorator(login_required, name='dispatch')
class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'add_event.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```
Class based view with login required for adding a new event to the site. It uses a `form_valid` method to check if the form is valid and add the author to the new event.

### Update Event View
```
@method_decorator(login_required, name='dispatch')
class UpdateEventView(UserPassesTestMixin, UpdateView):
    model = Event
    form_class = UpdateEventForm
    template_name = 'update_event.html'

    def test_func(self):
        return self.request.user.id == self.get_object().author.id
```
Class based view with login required to update an event.

### Delete Event View
```
@method_decorator(login_required, name='dispatch')
class DeleteEventView(UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'delete_event.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.id == self.get_object().author.id
```
Class based view with login required to delete an event.

## Django Project Forms
Another part in a django web app are the forms located in the `forms.py` file.

### Event Form (website app)
```
class EventForm(forms.ModelForm):
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
        super(EventForm, self).clean()
        
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            self._errors['description'] = self.error_class(['A minimum description of the event is required.'])
        return self.cleaned_data
```
The django form especifies the fields used from the model Event. It uses widgets to apply styling to the input fields. Finally, the `clean` method it is used to validate the input values.

### Update Event Form (website app)
```
class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'state', 'exerpt', 'description', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'exerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
```
This form is used to update an Event. 

### Create User Form (authentification app)
```
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
```
Form to create an user, it inherits from the django UserCreationForm.

### Create Profile Form (authentification app)
```
class SignUpProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')
    
    def __init__(self, *args, **kwargs):
        super(SignUpProfileForm, self).__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['profile_pic'].widget.attrs['class'] = 'form-control'
```
Form to create a new Profile

### Edit User Form (authentification app)
```
class EditUserForm(UserChangeForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
```
Form to edit a user information.

### Edit Profile Form (authentification app)
```
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'form-control'
```
Form to update the profile information

### Password Change Form (authentification app)
```
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
```
Form to update the user password. It inherits form the Django default PasswordChangeForm.

## Django Unit Tests
The unit test is used to test specifics parts of the django web app. The unit tests in this project are located in a `tests`folder inside the `website` folder. The test are organized in url tests, view tests, forms test and model tests. 

In total 30 unit tests that are runned with:
```
python3 manage.py test website
```

![Unit Tests](https://i.ibb.co/Zg7yYnh/Screenshot-2020-07-16-at-14-25-32.png)

## Django Functional Tests
As we said, the functional tests are separed in a differnt folder. The tests make use of the selenium-hub container and their nodes (chrome and firefox).

To run the functional tests:
```
python3 manage.py test functional_tests
```

The functional tests take around a minute or so.

## Frontend
In this section we will go through the frontend part of the project. 

### Theme Used
The project has been based in a `html` and `css`theme. The theme provides an html structure which is perfect to develop the Event Django project. 

Github of the theme can be found [HERE](https://github.com/puikinsh/ElaAdmin).

The theme basically uses Bootstrap 4 for styling. 

### Client Side
The project also has code executing in the clientside using `jquery`. 

```
$(document).ready(function() {
    var is_subscrived = $('#subs_func').attr("sub_stat") === 'True';
    if (is_subscrived) {
        $('#subs_func').removeClass("btn-primary").addClass("btn-outline-primary");
        $('#subs_func').html('<i class="fa fa-minus"></i>&nbsp; Unsubscrive');
        $('#description_sub').hide();
    }

    $('#subs_func').click(function(){
        var eventid;
        eventid = $(this).attr("data-eventid");
        var is_subscrived =  $(this).hasClass( "btn-outline-primary" ) === true;
        var subscription_comment = $('#description_sub').val()
        $.get("subscription", {event_id: eventid, subs_status:is_subscrived,subs_comment:subscription_comment}, function(data){
            console.log(data);
            $('#subs_count').html(data.num_subs);
            if (data.sub_status) {
                $('#subs_func').removeClass("btn-primary").addClass("btn-outline-primary");
                $('#subs_func').html('<i class="fa fa-minus"></i>&nbsp; Unsubscrive');
                $('#description_sub').hide();
                $( `<div class=\"card-body\" id=\"assistant_card\"><div class=\"stat-text\"><p><strong>Email: </strong>${data.email}</p></div><div class=\"stat-text\"><p><strong>Comment: </strong>${subscription_comment}</p></div></div>` ).insertBefore( "#assistant_card" );
            }else {
                $('#subs_func').removeClass("btn-outline-primary").addClass("btn-primary");
                $('#subs_func').html('<i class="fa fa-plus"></i>&nbsp; Subscrive');
                $('#description_sub').show();
            }
        });
        
         
    });

    $('#not_logged_subs').click(function(){
        console.log("HEYU");
        var eventid;
        eventid = $(this).attr("data-eventid");
        var subscription_comment = $('#description_not_log').val()
        var email = $('#email_not_log').val()
        console.log(email);
        $.get("subscription_not_logged", {event_id: eventid, subs_email:email,subs_comment:subscription_comment}, function(data){
            $('#subs_count').html(data.num_subs);
            $('#description_not_log').hide();
            $('#not_logged_subs').hide();
            $('#email_not_log').hide();

        });
        $( `<div class=\"card-body\" id=\"assistant_card\"><div class=\"stat-text\"><p><strong>Email: </strong>${email}</p></div><div class=\"stat-text\"><p><strong>Comment: </strong>${subscription_comment}</p></div></div>` ).insertBefore( "#assistant_card" );
         
    });


});
```
Those two functions are used in the Event details page for subscriving a user to an event without refreshing the page. It updates the people subscription count automatically and also the list of people going to the event.

Try it:

![jquery](https://i.ibb.co/gFyfH1g/Screenshot-2020-07-16-at-14-33-19.png)
![jquery](https://i.ibb.co/YBjZ5fS/Screenshot-2020-07-16-at-14-38-47.png)


## What's next?

So what's next? 

### Improving User Experience with React Components
Nowadays, the best user experiences are Django together with React. React components can be integrated to the django web app. 

### Scaling Django Web App
Another improvement would be to scale the django web app. Since the project is develop as a microservice we won't need to modify the django project. 

The first option would be to use NGINX and GUNICORN with a structure like this:
![scaling](https://rukbottoland.com/media/images/arquitectura-django-gunicorn-nginx-supervisor.jpg)

In the previous image we see supervisor, which makes sure that the Gunicorn workers keep working. 

Another option will be to scale using kubernates. 

## Author
My name is **Roger Almató Baucells** and you can contact me through email **r.almato.baucells@gmail.com**.


