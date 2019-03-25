# Django: Model Basics
We’ve now spent some time getting to know how to write web applications using the Pyramid framework. We’ve learned the basics of Model construction, routing, views and renderers. We’ve learned how to authenticate users and how to authorize them to take certain actions. And we’ve created our own first projects using this powerful and flexible tool.

Now it’s time for us to move on to using the current undisputed champion of the Python web frameworks: Django

## Starting a Django Project
We’ll begin by creating a new virtualenv in which to learn on Django. This one is for a book-lending library, and just for exploring in class. Name it accordingly, and then install Django:
```sh
$ mkdir django_lender
$ cd django_lender
$ python3 -m venv ENV
...
$ source ENV/bin/activate
(ENV)$ pip install Django
Collecting Django
  Using cached Django-1.11-py2.py3-none-any.whl
Collecting pytz (from Django)
  Using cached pytz-2017.2-py2.py3-none-any.whl
Installing collected packages: pytz, Django
Successfully installed Django-1.11 pytz-2017.2
```

## `startproject`
Once Django is installed, we can create a “project” to explore a bit. Django uses the term “project” to refer to the code that will make up one entire website. You always begin work on a Django website by creating a project.
```sh
(ENV)$ django-admin startproject lending_library
The startproject command works a bit like the cookiecutter command for Pyramid. It creates a bit of boilerplate code structure to make starting a new site easier. Let’s take a moment to look over the lending_library directory it created.

(ENV)$ tree lending_library
lending_library
├── lending_library
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
Notice it creates both an outer lending_library directory and an inner `lending_library` directory. The outer one is your project home (or project root). You should consider the contents of this outer directory the root of the project repository. You can make that explicit by initializing a git repository in the project root.

Nested inside the project root is a directory we’ll call the configuration root. This directory must be a proper Python package (with an `__init__.py` file).

It contains your project settings file(s) `settings.py`. This file contains configuration settings for a project. It plays a role similar to the development/production.ini files we’ve seen in Pyramid.

It also contains a `wsgi.py` file, which exposes the wsgi application that contains your project. This file is roughly analogous to the `paste.app_factory` entry point in a Pyramid application. However, Django is not as closely tied to Python packaging as Pyramid. It makes much less use of packaging features like entry points, in favor of its own solutions.

Finally, the configuration root contains a `urls.py` file. This file contains the top-level configuration of urls for your project. We’ll talk more about this later on this week, but for now understand that Django urls are analogous to Pyramid’s routes. They provide the connection between the path of an incoming HTTP request and the code object that will generate an HTTP response.

## Setting up the Database
As noted above settings.py houses the project configuration. A part of that configuration is the location and form of the database. By default, Django sets you up with a connection to a sqlite3 database. We’re beyond that now though, so let’s just jump right to PostgreSQL.

Remove the data associated with the default key in the DATABASES dictionary. In its place, have the following:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': <your postgres database name>,
        'USER': <your postgres username>,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
```
}
If database access for you requires a password, include a PASSWORD field and the necessary password. You shouldn’t ever have a plain-text password sitting in files that will be in your repository, so at least make sure to bind your password to an environment variable that you can pull out with `os.environ`. In fact, just use environment variables for the NAME, USERNAME, PASSWORD, and HOST fields as need be.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': '5432',
    }
}
```
As with any other framework that hooks into PostgreSQL, you’ll need to actually pip install `psycopg2-binary` to get started. You’ll also have to create the database that you intend to use for your app with `createdb`.

Because we don’t write code without writing tests to accompany, we need to add this next bit as well.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': '5432',
        'TEST': {
            'NAME': <your testing database name>
        }
    }
}
```
Yes, you include your testing database here. No, you do not have to create your testing database. Django will do it for you when you run your tests.

## `manage.py`
The only other file created by `startproject` is `manage.py`, in the project root. The file contains code which locates your project’s settings.py file. It does this by setting the value of `DJANGO_SETTINGS_MODULE` in `os.environ`.

This file serves as a gateway to Django’s command system. It is an executable python script (notice the if `__name__ == "__main__":` block and the shebang line at the top).
```python
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lending_library.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
```

## Managing Django
Django’s management command system is accessed entirely through the manage.py script. When we execute this script, it uses additional values on the command line as command names and arguments for those commands. To get a list of the available management commands, run the script with no additional values:
```bash
(ENV)$ cd lending_library
(ENV)$ python manage.py

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser
    ...
```

## `shell`
The first command that will be important to you is `shell`. Running this command starts an interactive Python session with all of the packages in your Django project available for import. It’s the Django version of `pshell` from Pyramid. Like `pshell`, if you install iPython, it will automatically use the iPython interpreter (with tab completion and everything):
```bash
(ENV)$ pip install iPython
...
(ENV)$ python manage.py shell
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.0.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import django.contrib.auth
In [2]: django.contrib.auth.
django.contrib.auth.BACKEND_SESSION_KEY
django.contrib.auth.HASH_SESSION_KEY
...
```

## Exploring Django’s Models
Django comes with its own ORM, and relies entirely on the idea of models. It comes with quite a few of these models already present. Django requires that you place models in a Python module named `models.py`. We can use this knowledge to explore the models from Django’s auth app. Here we will find the User model, the core of Django’s authentication and authorization systems.
```bash
In [2]: django.contrib.auth.models.
django.contrib.auth.models.AbstractBaseUser
django.contrib.auth.models.AbstractUser
...
django.contrib.auth.models.User
...
```

## User
Let’s import and inspect the User model, so we can learn a bit about it.
```bash
In [2]: from django.contrib.auth.models import User
In [3]: User?
Init signature: User(*args, **kwargs)
Docstring:
Users within the Django authentication system are represented by this
model.

Username, password and email are required. Other fields are optional.
File:           .../ENV/lib/python3.6/site-packages/django/contrib/auth/models.py
Type:           ModelBase
```
The User model has, at the very least, username, password, and email fields. These are required attributes. But what else is there?
```bash
In [4]: dir(User)
Out[4]:
['DoesNotExist',
'Meta',
'MultipleObjectsReturned',
'REQUIRED_FIELDS',
'USERNAME_FIELD',
...
```
Wow, there’s all sorts of stuff on that object! It might be better for us to go and take a look at the source code so we can start to get an idea of how this thing is built. Lets see where the User file lives:
```bash
In [5]: django.contrib.auth.models.__file__
Out[5]: '.../ENV/lib/python3.6/site-packages/django/contrib/auth/models.py'
```
Reading the source file, we can find the User model. But the source for it is remarkably void of attributes. Where do all the attributes we saw in the shell come from?
```python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
```
## Subclassing
Django makes extensive use of subclassing to share attributes among models. The User model inherits from AbstractUser:
```python
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    ...
    """
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
        ...
        )
    ...
```

## Fields
AbstractUser inherits from `AbstractBaseUser` and `PermissionsMixin` too, but here we can see username. Notice the syntax used to define that attribute. It looks similar to SQLAlchemy, in that the attribute is bound to an instance of some kind of class.

In SQLAlchemy we called these things Columns. In Django, we call them Fields. It can get confusing because there are Model fields and Form fields, but they are not the same thing.

This username is a Model Field. Like SQLAlchemy’s Columns, model fields are responsible for communicating between Python and the database. The models.CharField defines a text field inside the database. Values we set for this attribute of instances of the User model We can create a new User instance. We can set a value for the username attribute on that instance. And we can persist that value into a database.

The biggest difference here from what we are used to has to do with the semantics of how we interact with the database. Django is model-centric as opposed to session-centric. Remember in SQLAlchemy we always started with a session. We would use statements like session.query(Entry) to query a model.

Django is different. We start with the model itself, User. That class object will have an attribute called objects. That attribute *is* the connection between the model class and the database. We will use that attribute to build queries.

Let’s create a new user bob:
```bash
In [1]: from django.contrib.auth.models import User
In [2]: bob = User()
In [3]: bob
Out[3]: <User: >
```
By default, bob has empty attributes:
```bash
In [4]: bob.username
Out[4]: u''

In [5]: bob.email
Out[5]: u''

In [6]: print(bob.id)
None
```
Let’s give bob some information. We saw before that username, password, and email are required. We’ll start by setting values for those attributes.
```bash
In [7]: bob.username = "bob"
In [8]: bob.password = "foobar"
In [9]: bob.email = "bob@bob_dobalina.com"
In [10]: bob
Out[10]: <User: bob>
```
Now we have bob with a representation: <User: bob>. Does bob have an ID now?
```bash
In [11]: bob.id

In [12]:
```
No. Nothing is returned. How did we add a new entry into our system in Pyramid? How did we make the database aware of something and preserve it?

```python 
session.add(instance)
```
But not in Django. Remember, here the semantics are based on the instance itself.

We can call save() on the bob user instance. But we have to create the database first.

In another terminal, we can create our database tables by running a “migration” command on our project. python manage.py migrate takes a look at every registered object that inherits from Model and checks the database to see if that migration has been applied. If it hasn’t it’ll apply the migration, sometimes creating new tables where they’re needed, or updating existing tables to be consistent with changes in the codebase.
```bash
$ source ENV/bin/activate
(ENV)$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, contenttypes, auth, sessions
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  ...
```
## Basic Query API
Now we can save bob:
```bash
In [12]: bob.save()
In [13]: bob.id
Out[13]: 1
```
And make even more users:
```bash
In [14]: sally = User(username="sally", email="sally@sally.com", password="secret")
In [15]: sally.save()
In [16]: sally.id
Out[16]: 2
```
How about a listing (note: not a list object) of all of our users?
```bash
In [17]: User.objects.all()
Out[17]: <QuerySet [<User: bob>, <User: sally>]>
```
We can filter the listing:
```bash
In [18]: User.objects.filter(username='bob')
Out[18]: <QuerySet [<User: bob>]>
```
## For Homework
One of the first things we want to do is create a User model. Something that represents the user in our system. However, we are strongly encourged to use Django’s own built in user model unless we have a very good reason not to. But the standard Django user model doesn’t have everything that we want. It does have:
```python
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    ...
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    ...
```

## Wrap Up
We’ve learned a bit now about how Django works. We learned about starting new applications, and managing them. We’ve learned about the Django ORM and how it works And we’ve learned about the built-in User model it provides. We’ve talked about how we can extend the functionality of this model using a Profile related to the User by a one-to-one relationship. You’ll use this knowledge now to create a profile for the users of our Django application.
