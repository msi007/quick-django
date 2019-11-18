# Quick Django
A boilerplate Django project for quickly getting started.

---

## Features
- Styling with [Bootstrap](https://getbootstrap.com/) v4.1.3
- Custom user model
- Email/password for log in/sign up instead of Django's default username/email/password pattern
- Django debug toolbar
---
## SetUp

1. Clone the repository
```bash
$ git clone https://github.com/ifat-mohit/quick-django.git
$ cd quick-django
```
2. Create a virtualenv with virtualenv env and install dependencies
```bash
$ pip install -r requirements.txt
```

3. Rename your project

```bash
$ python manage.py rename <new-project-name>
```
4. Configure your .env variables in root directory

5. Set up the initial migration for our custom user models in users and build the database.
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
6. Create a superuser
```bash
$ python manage.py createsuperuser
```
7. Confirm everything work correctly
```bash
$ python manage.py runserver
```

Load the site at http://127.0.0.1:8000. :rocket:

![Homepage](/static/images/home.png)

![Homepage](/static/images/login.png)
