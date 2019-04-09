# Django Forms

## Form Handling in Django, and the Form-handling CBVs

* * *

We will need to work with the form system in Django if we want to add or
update books in our app.

[Django’s form system](https://docs.djangoproject.com/en/2.0/ref/forms/) has
a couple of layers to it.

We’ll make an analogy. “Models are to the Database as Forms are to
request/response cycle.”

The job of a model in Django is to translate data between python and the
database. The job of a form in Django is to translate data back and forth
between python and the request/response cycle. A form takes in information that
comes from the request and translates it into pythonic values.

Remember, every time you get information coming in on the request, that
information is coming in as a bytestring. When you pass a primary key back and
forth across a URL, that comes into your app as a bytestring. You want to turn
that into an integer so you can interact with the database. The Django form is
going to make that happen for you.

This can start to get weird because Models have fields, and Forms have fields.
They look similar, but they are very different from each other. The model
field holds the responsibility of translating a particular python value into
some sort of database query. Also it takes the return value and turns it back
into a python value. The form does the same thing except it does it with data
from the request and response. It turns one item of information into a
pythonic value.

Forms serialize and deserialize, meaning that they standardize and arrange
your data for output to some other medium. They do it with a structure called
a [widget](https://docs.djangoproject.com/en/2.0/ref/forms/widgets/). The
widget renders out HTML elements, visible or hidden, that then is rendered
into an HTML page.

Let’s say we have something that’s a `forms.CharField` field. It will have by
default use the `forms.TextInput` widget, that has a text input. When you call
the widget’s `render` method, it will give you `input[type="text"]` and
`value` = field contents (empty if `None`). This is the overall structure of
how form libraries everywhere work.

### Forms in Practice

So how do forms in Django work? A form is just a collection of fields.

Let’s start up our Django shell:


```python
In [4]: from django import forms

In [5]: class FooForm(forms.Form):
   ...:     name = forms.CharField(label="Your Name", max_length=100)
   ...:     description = forms.CharField(label="Describe Something", widget=forms.Textarea, max_length=2048)
   ...:

In [6]: FooForm
Out[6]: __main__.FooForm

In [7]: type(FooForm)
Out[7]: django.forms.forms.DeclarativeFieldsMetaclass

In [8]:  form1 = FooForm()

In [9]: form1
Out[9]: <FooForm bound=False, valid=Unknown, fields=(name;description)>

In [10]: type(form1_form)
Out[10]: __main__.FooForm

```

There are a few things to think about here. Our form can be in one of two
states: either bound or unbound. The difference: a bound form knows about
data. It has some information that has been passed into it. An unbound form
doesn’t have any data attached.

Now, we have a working form called `form1`. It tells us that it is unbound. It
doesn’t know if it is valid yet, and it has some fields.

If we just call `str()` on our `form1`, it will render out into raw HTML:


```python
In [11]: str(form1)
Out[11]: '<tr><th><label for="id_name">Your Name:</label></th><td><input type="text" name="name" maxlength="100" required id="id_name" /></td></tr>\n<tr><th><label for="id_description">Describe Something:</label></th><td><textarea name="description" cols="40" rows="10" maxlength="2048" required id="id_description">\n</textarea></td></tr>'
```

Note that the labels we specified for the fields we wanted rendered out for us
as well. It also rendered out a few things that we didn’t ask for, at least
not explicitly:

  * Each form field has an ID that’s a concatenation of the word `id` and the name of the field we gave
  * Each field’s `name` attribute corresponds to the actual name of the field we specified in `FooForm`
  * Each field is `required`, even though we didn’t ask for that

The `form1.as_p()` method will render our form with `<p>` tags:


```python
In [12]: form1.as_p()
Out[12]: u'<p><label for="id_name">Your Name:</label> <input type="text" name="name" maxlength="100" required id="id_name" /></p>\n<p><label for="id_description">Describe Something:</label> <textarea name="description" cols="40" rows="10" maxlength="2048" required id="id_description">\n</textarea></p>'
```

There are also `as_table()` and `as_ul()` methods. `as_table()` is the default
and the same as our `str()` rendering.

Notice that the `<form>` tag is missing. There is also no `<submit>` button.
That’s up to you.

### Bound Form

Let’s make another form. We’ll pass in some data as a dictionary, and then the
form will be bound.


```python
In [13]: form2 = FooForm({'name': 'Fellow', 'description': 'Instructor for the Python 401 course at Code Fellows'})

In [14]: form2
Out[14]: <FooForm bound=True, valid=Unknown, fields=(name;description)>
```

Now we can use that information to fill out the form with the data that
exists. Notice the `value="Fellow"` attribute:


```python
In [15]: form2.as_p()
Out[15]: u'<p><label for="id_name">Your Name:</label> <input type="text" name="name" value="Fellow" maxlength="100" required id="id_name" /></p>\n<p><label for="id_description">Describe Something:</label> <textarea name="description" cols="40" rows="10" maxlength="2048" required id="id_description">\nInstructor for the Python 401 course at Code Fellows</textarea></p>'
```

Forms are also iterators. These objects come out in the order that you specify
the attributes. If you want to change the ordering of a form, change it in the
Django form definition.


```python
In [16]: for field in form2:
   ....:     print(field)
   ....:
<input type="text" name="name" value="Fellow" maxlength="100" required id="id_name" />
<textarea name="description" cols="40" rows="10" maxlength="2048" required id="id_description">
Instructor for the Python 401 course at Code Fellows</textarea>
```

If you aren’t happy with the way Django is rendering `<p>` forms or whatever,
you can address the field properties directly and lay them out how you like:


```python
In [17]: field.id_for_label
Out[17]: u'id_description'

In [18]: field.label
Out[18]: u'Describe Something'

In [19]: field.value()
Out[19]: u'Instructor for the Python 401 course at Code Fellows'
```

It’s probably best to let Django render the fields for you.

The `valid` value of a form is also important. When a form is bound, you can
do validation checks on it.


```python
In [20]:  form2.is_valid()
Out[20]: True
```

This allows us access to `cleaned_data`:


```python
In [21]: form2.cleaned_data
Out[21]:
{'description': 'Instructor for the Python 401 course at Code Fellows',
 'name': 'Fellow'}
```

`cleaned_data` is a dictionary of key-value pairs that correspond to the field
names and the values those fields contain. It is **super important**. Why?
Because: ` form2` also has a `data` attribute:


```python
In [22]: form2.data
Out[22]:
{'description': 'Instructor for the Python 401 course at Code Fellows',
 'name': 'Fellow'}
```

It looks the same in this case, but the difference is that `cleaned_data` has
gone through validation. Thus you can be sure that if someone is trying to
inject malicious data, Django has already sterilized it and it is safe for
python to use.

Whenever you’re reading data from a form, always validate the data first. Then
use the `cleaned_data` attribute of your form to get access to the
information.

Let’s build one that might not be validated.


```python
In [23]: form3 = FooForm({'name': 'My name is reallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreally loooooooong', 'description': ''})

In [24]: form3
Out[24]: <NameForm bound=True, valid=Unknown, fields=(your_name)>
```

Notice it is bound, but we don’t know yet if it is valid. That `valid=Unknown`
flag will only get decided _after_ a manual check for validity. When we check
the validity:


```python
 In [23]: form3.is_valid()
Out[23]: False

In [24]: form3.cleaned_data
Out[24]: {}
```

This particular form will have an `errors` attribute now:


```python
In [25]: form3.errors
Out[25]:
{'description': ['This field is required.'],
 'name': ['Ensure this value has at most 100 characters (it has 113).']}
```

Notice how even though we specified the “description” field, Django interprets
the data as empty because we passed it an empty string as a value.

You can use the `errors` attribute to send error messages back to your forms.


```python
In [26]: for error_field in form3.errors:
    print("There's a mistake in field '{field}': {problem}".format(
        field=error_field,
        problem=form3.errors[error_field]
    ))
   ....:
There's a mistake in field 'name': <ul class="errorlist"><li>Ensure this value has at most 100 characters (it has 113).</li></ul>
There's a mistake in field 'description': <ul class="errorlist"><li>This field is required.</li></ul>
```

Django makes some nice default error messages for us with HTML markup too.
There is ample API documentation for forms, like how to substitute css classes
and things like that. Dig in when you get the chance!

### [`ModelForm`](https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/#django.forms.ModelForm)

There’s something else you should know about forms: **the way we built forms
above is not the only way.**

Your app is filled up model objects. One thing you would like to do is present
forms that allow you to create and edit those models directly. For this
purpose, Django provides a construct called a `ModelForm`.

What a `ModelForm` does is inspect your model and its fields. It then creates
a form that has all the equivalent form fields to your model’s fields.

To put a `ModelForm` to use:

  * Create a class that subclasses `ModelForm`.
  * Provide a `class Meta`
    * This informs the form object about some options that you can set for it.


```python
In [27]: from lender_books.models import Book

In [28]: Book
Out[28]: lender_books.models.Book

In [29]: class BookForm(forms.ModelForm):
  ....:     class Meta:
  ....:         model = Book
  ....:         exclude = []
  ....:

In [30]: BookForm
Out[30]: __main__.BookForm

In [31]: bkfm1 = BookForm()

In [32]: bkfm1
Out[32]: <BookForm bound=False, valid=Unknown, fields=(title;author;cover_image;status)>
```

This looks familiar. Our fields automatically include all of the fields on the
Book model.

Let’s grab ourselves an instance of the Book object:


```python
In [33]: Book.objects.all()
Out[33]: <QuerySet [<Book: Book object>]>

In [34]: bk1 = _[0]

In [35]: bk1
Out[35]: <Book: Book object>
```

When we create a BookForm, if we want to bind it to an instance, we can use
the instance keyword argument to instantiate our new BookForm:


```python
In [36]: lovely_form = BookForm(instance=bk1)

In [37]: lovely_form
Out[37]: <BookForm bound=False, valid=Unknown, fields=(title;author;cover_image;status)>

In [38]: lovely_form.as_p()
Out[38]: '<p><label for="id_title">Title:</label> <input id="id_title" maxlength="255" name="title" type="text" value="Catcher in the Rye" required /></p>\n<p><label for="id_author">Author:</label> <input id="id_author" maxlength="255" name="author" type="text" value="J.D. Salinger" required /></p>\n<p><label for="id_status">Status:</label> <select id="id_status" name="status" required>\n<option value="available" selected="selected">Available</option>\n<option value="checked out">Checked Out</option>\n</select></p>'
...'
```

Django gives us all sorts of options here that allows us to manipulate our
model.

Notice that `lovely_form` is not bound:


```python
In [39]: lovely_form
Out[39]: <BookForm bound=False, valid=Unknown, fields=(title;author;cover_image;status)>
```

Why do we suppose that is? Because we haven’t passed in any data. We use model
forms to take data from somewhere else and either create a new model instance
or edit an existing model form. Simply providing an instance doesn’t bind the
form to anything.

If we make a change, the form will become bound, and the `selected` attribute
will now be `'bob'` (our user 3 in this case):


```python
In [40]: changed_form = BookForm({'title': 'Malcolm X'}, instance=bk1)

In [41]: changed_form
Out[41]: <BookForm bound=True, valid=Unknown, fields=(title;author;cover_image;status)>

In [42]: str(changed_form)
Out[42]: '<tr><th><label for="id_title">Title:</label></th><td><input id="id_title" maxlength="255" name="title" type="text" value="Malcolm X" required /></td></tr>\n<tr><th><label for="id_author">Author:</label></th><td><ul class="errorlist"><li>This field is required.</li></ul><input id="id_author" maxlength="255" name="author" type="text" required /></td></tr>\n<tr><th><label for="id_cover_image">Cover image:</label></th>......
```

Let’s look at a bit of this:

`<input id="id_title" maxlength="255" name="title" type="text" value="Malcolm X" required />`

We see that our provided dictionary’s data takes precedence. The base instance
that was attached to the form will still provide its data to the form, but it
doesn’t take priority.

Is the form valid?


```python
In [43]: changed_form.is_valid()
Out[43]: False

In [44]: changed_form.errors
Out[44]: {'author': ['This field is required.'], 'status': ['This field is required.']}
```

So let’s fix our errors and inspect our book:


```python
In [45]: changed_form = BookForm({"author": "Alex Haley", "status": "available", "title": "Malcolm X"}, instance=bk1)

In [46]: changed_form.is_valid()
Out[46]: True

In [47]: bk1.title
Out[47]: 'Catcher in the Rye'
```

Even though the data provided to the form was valid, nothing changed about the
book object itself because the form wasn’t saved. Let’s remedy that.


```python
In [48]: changed_form.save()
Out[48]: <Book: Book object>

In [49]: bk1.title
Out[49]: 'Malcolm X'
```

Our instance has already been updated by the fact that we bound some data to a
form. Once we save the form, it will be updated in the database too.

## Forms and the WRRC

We saw how we passed in an instance of a form and some data. Where does the
data come from when we’re not working in terminal?

In Django you have a `request` object available within inside any view you
create. Amongst others, `request` will have 2 attributes of importance
attached. These attributes will contain any form data that got sent to you
from the browser. Depending on the type of request, data will either be in
`request.post` or `request.get`. Using forms you’ll probably want to use
`post`.

Most of this process will be similar to what you have done already with create
and update views.

`request.post` is a dictionary, and you can pass it in as part of the data
that comes to you. Provided that everything coming from the `request` is what
you need to create a new model instance or update one, you can pass it
directly.


```python
updated_book = BookForm(request.post)
```

If your data needs to be massaged at all, you’ll need to do that work and then
pass the resulting data into the BookForm.

### Forms and Files

You are going to want to upload books with images of their covers. This might
be a bit odd. That image data (and any other uploaded data) will be coming to
you not in `request.post` or `get`. They come in a completely different place
called `request.files`.

There’s one more trick to this. In order to get image data, you have to do
something to your HTML `<form>` tag. There’s an attribute to forms called the
[`enctype`](https://www.w3.org/TR/html401/interact/forms.html#adef-enctype).
**In order to upload images, you need to set the[` enctype="multipart/form-data"`](https://docs.djangoproject.com/en/2.0/topics/http/file-uploads/#basic-file-uploads) attribute**

On the other end, you need to make sure you bind your form with not only the
first dictionary, but also a second containing the file information:


```python
In [50]: changed_form = BookForm({"author": "Alex Haley", "status": "available", "title": "Malcolm X"}}, {'cover_image': <file upload object>}, instance=bk1)
```

Django is responsible for dealing with all of this. All you need to do is pass
in `request.post, request.files, instance=the_original_instance`. If you’re
creating a new instance, just don’t pass in an instance and Django will build
a new one for you when you call `form.save()`
