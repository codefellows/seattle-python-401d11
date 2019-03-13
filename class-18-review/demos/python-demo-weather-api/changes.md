# Flask Authentication / Authorization

---

## Big Change
- A big deal to secure your site

---

## Not too much code.
- Only 7 files created or modified
- Some changes only wafer thin

---


## Auth markup : base.html
- header / nav should differ when logged in
- conditional nav rendering based on g.user
- register, login, logout nav links
- conditional welcome in header

---

## Log In / Register Templates
* templates/auth/login.html
* templates/auth/register.html

---

## Auth Routes : auth.py

- /login
- /logout
- /register
- @login_required
- @app.before_request 


---

## App Routes : routes.py

- from .auth import login_required
- @login_required decorator on all routes

---

## AuthForm : forms.py

- class AuthForm(FlaskForm)
- email, password fields
            
---

## User Model : models.py

- class User(db.Model)
- check_password_hash class method

