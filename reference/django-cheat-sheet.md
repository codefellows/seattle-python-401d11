Cheat Sheet

- Create project folder and cd into it
    ```
    $ mkdir foo_site && cd $_
    $ pipenv install django
    $ pipenv shell
    $ django-admin startproject foo_project .
    ```
    - Note the . at end

- run it
    ```
    $ python manage.py runserver
    ```
    - Should see "The installer worked successfully!" at http://localhost:8000
    
---

## MV*
### Model, View, Template, Url (with settings.py to stitch it together)

- Create an app
    - `$ python manage.py startapp bars`
- Add `bars` (or alternately `bars.apps.BarsConfig`) to end of `INSTALLED_APPS` section in `settings.py`

---

- Create a View
    - edit `bars/views.py`
    ```
    from django.http import HttpResponse

    def homePageView(request):
        return HttpResponse('Hello, World!')
    ```
---
- Add the Url
    - `$ touch bars/urls.py`
    ```
    from django.urls import path
    from .views import homePageView

    urlpatterns = [
        path('', homePageView, name='home')
    ]
    ```
- add the urlpatterns to project urls
    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('bars.urls')),
    ]
    ```
    ---
    - Run it!
    `$ python manage.py runserver`