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
│   │   │       ├── background.jpg
│   │   │       ├── cat.jpg
│   │   │       ├── cat2.jpg
│   │   │       ├── cat3.jpg
│   │   │       ├── cat3.png
│   │   │       ├── contact-background.jpg
│   │   │       ├── experience-background.jpg
│   │   │       ├── github.svg
│   │   │       ├── linkedin.svg
│   │   │       ├── main-background.jpg
│   │   │       └── twitter.svg
│   │   ├── error_pages
│   │   │   └── css
│   │   │       └── style.css
│   │   └── website
│   │       ├── css
│   │       │   ├── cs-skin-elastic.css
│   │       │   ├── lib
│   │       │   │   ├── chosen
│   │       │   │   │   ├── chosen-sprite.png
│   │       │   │   │   ├── chosen-sprite@2x.png
│   │       │   │   │   ├── chosen.css
│   │       │   │   │   └── chosen.min.css
│   │       │   │   ├── datatable
│   │       │   │   │   ├── buttons.bootstrap.min.css
│   │       │   │   │   ├── buttons.dataTables.min.css
│   │       │   │   │   └── dataTables.bootstrap.min.css
│   │       │   │   └── vector-map
│   │       │   │       └── jqvmap.min.css
│   │       │   ├── style.css
│   │       │   └── style.css.map
│   │       ├── fonts
│   │       │   └── icomoon
│   │       │       ├── icomoon.eot
│   │       │       ├── icomoon.svg
│   │       │       ├── icomoon.ttf
│   │       │       ├── icomoon.woff
│   │       │       └── index.html
│   │       ├── images
│   │       │   ├── avatar
│   │       │   │   ├── 1.jpg
│   │       │   │   ├── 2.jpg
│   │       │   │   ├── 3.jpg
│   │       │   │   ├── 4.jpg
│   │       │   │   ├── 5.jpg
│   │       │   │   ├── 6.jpg
│   │       │   │   ├── 64-1.jpg
│   │       │   │   └── 64-2.jpg
│   │       │   ├── favicon.jpg
│   │       │   ├── favicon.png
│   │       │   ├── logo.jpg
│   │       │   ├── logo.png
│   │       │   ├── logo.psd
│   │       │   └── logo2.png
│   │       ├── js
│   │       │   ├── dashboard.js
│   │       │   ├── init
│   │       │   │   ├── chartjs-init.js
│   │       │   │   ├── datatables-init.js
│   │       │   │   ├── flot-chart-init.js
│   │       │   │   ├── fullcalendar-init.js
│   │       │   │   ├── gmap-init.js
│   │       │   │   ├── peitychart-init.js
│   │       │   │   ├── vector-init.js
│   │       │   │   └── weather-init.js
│   │       │   ├── jquery.js
│   │       │   ├── lib
│   │       │   │   ├── chosen
│   │       │   │   │   ├── chosen.jquery.js
│   │       │   │   │   ├── chosen.jquery.min.js
│   │       │   │   │   ├── chosen.proto.js
│   │       │   │   │   └── chosen.proto.min.js
│   │       │   │   ├── data-table
│   │       │   │   │   ├── buttons.bootstrap.min.js
│   │       │   │   │   ├── buttons.colVis.min.js
│   │       │   │   │   ├── buttons.flash.min.js
│   │       │   │   │   ├── buttons.html5.min.js
│   │       │   │   │   ├── buttons.print.min.js
│   │       │   │   │   ├── dataTables.bootstrap.min.js
│   │       │   │   │   ├── dataTables.buttons.min.js
│   │       │   │   │   ├── datatables.min.js
│   │       │   │   │   ├── jquery-1.12.4.js
│   │       │   │   │   ├── jquery.dataTables.min.js
│   │       │   │   │   ├── jszip.min.js
│   │       │   │   │   ├── pdfmake.min.js
│   │       │   │   │   └── vfs_fonts.js
│   │       │   │   └── gmap
│   │       │   │       ├── gmapApi.js
│   │       │   │       ├── gmaps.js
│   │       │   │       └── gmaps.min.js
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
### Docker

## Installation

### Requirements
### Installation
### Deployment

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


