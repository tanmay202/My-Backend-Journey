# Django Models & ORM – Basics Guide

This document explains Django Models, the ORM, database configuration, and the migration process in a simple and beginner-friendly manner.

I. What are Django Models?

A Django Model is a blueprint used to create a database table. It defines the structure of the data that will be stored in the database. Technically, a model is a Python class. Just as a View is a function, a Model is a class. Models are defined inside the models.py file of a Django app.

II. The Role of ORM (Object Relational Mapper)

Django provides an Object Relational Mapper (ORM) that allows developers to interact with the database without writing raw SQL queries. You define models using Python code, and the ORM automatically converts them into database tables and SQL queries. This makes database operations easier, safer, and independent of the database engine.

III. Default Database & Configuration

By default, Django uses SQLite3 as its database. The database file is named db.sqlite3 and comes pre-configured, requiring no manual setup. Database configuration is located inside the DATABASES dictionary in the settings.py file.

IV. Creating a Model (Step-by-Step)

To create a model, define a class inside models.py that inherits from models.Model.

Example:

from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()

Here, CharField is used to store text data and requires a max_length parameter, while IntegerField is used to store whole numbers.

V. Migration Process (Activating the Model)

Defining a model does not automatically create a table in the database. To activate the model, the following steps must be followed. First, register the app by adding it to the INSTALLED_APPS list in settings.py. The recommended way is to add the app configuration path, such as 'myapp.apps.MyappConfig'. Next, run the command python manage.py makemigrations. This command detects changes in models.py and creates migration files. Finally, run python manage.py migrate. This applies the migrations and creates the actual database tables.

VI. Important Django Console Commands

python manage.py runserver – Starts the Django development server  
python manage.py makemigrations – Creates migration files based on model changes  
python manage.py migrate – Applies migrations to the database

Summary

Django Models define the structure of database tables using Python classes. The ORM removes the need to write SQL queries manually. SQLite3 is the default database used by Django. Migrations are required to convert models into actual database tables.
