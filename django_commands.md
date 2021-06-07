# Django 

Notes from https://docs.djangoproject.com/en/3.2/intro/tutorial01/

## Create a Project

- Creat a project:
	$ django-admin startproject mysite

- Run the server. THIS IS FOR DEVELOPMENT NOT PRODUCTION:
	$ python manage.py runserver

- Visit the URL in stdout to see if it is working. New code is automatically reloaded.

- To run on a specified port (8080 here):
	$ python manage.py runserver 8080

- To specify port (0 is short for 0.0.0.0.):
	$ python manage.py runserver 0:8000


- To create an app within this project (in this case "polls"), from mysite dir:
	$ python manage.py startapp polls

...more stuff...

- The path() fn in urls.py. 
	- Required Arguments:
		- route: 
			- a url pattern as string; searched in order of appearance in urlpatterns list;
			- GET and POST parameters are not searched
		- view: 
	- Optional Arguments:
		- kwargs: a dict
		- name: allows calling from other parts of code base; allows global url pattern changes made from a single file that are propagated

## Database and Migrations

- To set up tables in database:
	- $ python manage.py migrate

	- To use sqlite3 (default):
		- $ sqlite3
		- $ .help
	- Show tables created:
		- $ .schema * 

- Define data models in models.py of the app. Then Django can generate:
	- database schema
	- database access API

- Add app to INSTALLED_APPS in project settings.py

_Migrations_ are the versions of your apps. View them in app_dir/migrations/

- To update changes and store as a _migration_:
	- $ python manage.py makemigrations name_of_app

- Check what migration will be run without running it:
	- $ python manage.py sqlmigrate app_name migration_number 

- To make the migration changes to the database:
	- $ python manage.py migrate


- 3 Steps to making model changes:
	- Change models in models.py
	- $ python manage.py makemigrations
	- $ python manage.py migrate

- To use the default API (using python manage.py sets DJANGO_SETTINGS_MODULE env variable):
	- $ python manage.py shell

## Views

A _view_ is a type of webpage represented by a Python fn. To translate a URL to a view, Django uses a `URLconf` 
- Each _view_ returns and HttpResponse or an Http exception.

Create `templates` dir in app dir. Django looks there automatically.

- `render(request_object, template_name[, context_dict]) -> HttpResponse`


- To avoid hard coded urls use, e.g. `<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>`, which looks up url definition in polls/urls.py

- With multiple apps, need to add `app_name="polls"` in polls/urls.py and use the namespace for the url reference: `<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>`


