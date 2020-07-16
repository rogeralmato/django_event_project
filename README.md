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
  - [System Architecture](#system-architecture)
    - [Project Container](#project-container)
    - [Postgress Container](#postgress-container)
    - [Selenium Hub Container](#selenium-hub-container)
    - [Desktop Chrome Selenium node](#desktop-chrome-selenium-node)
    - [Desktop Firefox Selenium node](#desktop-firefox-selenium-node)
  - [Project Arhitecture](#project-arhitecture)
    - [Website Django App](#website-django-app)
    - [Authentification Django App](#authentification-django-app)
    - [Functional tests Folder](#functional-tests-folder)
  - [Project Models](#project-models)
    - [Event Model (website)](#event-model-website)
    - [EventState  Model  (website)](#eventstate-model-website)
    - [EventSubscription Model (website)](#eventsubscription-model-website)
    - [Profile Model (website)](#profile-model-website)
    - [User Model (authentification)](#user-model-authentification)
  - [Project Views](#project-views)
  - [Project Forms](#project-forms)
  - [Unit Tests](#unit-tests)
  - [Functional Tests](#functional-tests)
  - [Frontend](#frontend)
    - [Theme Used](#theme-used)
    - [Client Side](#client-side)
  - [What's next?](#whats-next)
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

## System Architecture

### Project Container
### Postgress Container
### Selenium Hub Container
### Desktop Chrome Selenium node
### Desktop Firefox Selenium node

## Project Arhitecture
### Website Django App
### Authentification Django App
### Functional tests Folder

## Project Models 
### Event Model (website)
### EventState  Model  (website)
### EventSubscription Model (website)
### Profile Model (website)
### User Model (authentification)

## Project Views

## Project Forms

## Unit Tests

## Functional Tests

## Frontend
### Theme Used
### Client Side

## What's next?

## Author


