# Django Admin Panel Guide

The Django Admin Panel is a built-in dashboard used to manage and control the data of a Django web application.

1. Create a Superuser

To access the Django admin panel, an administrative account (superuser) is required. First, stop the running server by pressing Control + C. Then run the command `python manage.py createsuperuser`. You will be prompted to enter a username, email address (can be a dummy email), and password. After completing this process, the superuser account will be created.

2. Access the Admin Panel

Start the development server using the command `python manage.py runserver`. Open a web browser and go to `http://127.0.0.1:8000/admin/`. Log in using the superuser credentials created earlier. Once logged in, the Django admin dashboard will be visible.

3. Register Models

By default, custom models do not appear in the admin panel. To make them visible, they must be registered. Open the `admin.py` file inside your app directory. Import the model using `from .models import Item` and register it using `admin.site.register(Item)`. After registration, the model will appear in the admin panel.

4. Renaming Models (Best Practice)

It is a best practice to name Django models in singular form, such as `Item` instead of `Items`. If a model class name is changed in `models.py`, all references to that model must also be updated in files like `admin.py`. After renaming, run `python manage.py makemigrations` followed by `python manage.py migrate`. This ensures proper database table naming and correct plural labels in the admin panel, such as "Items" instead of incorrect forms like "Itemss".

5. Adding Data Using Admin Panel

In the admin dashboard, click on the registered model name, such as "Items". Click the Add button to insert new data. Fill in the required fields like Item Name, Description, and Price, then click Save. The entered data is stored in the database and can be viewed directly in the admin panel or verified using an SQLite database viewer.

Summary

The Django admin panel provides a powerful and easy way to manage application data. Creating a superuser allows access, registering models makes them visible, and the admin interface enables easy data entry, modification, and verification without writing additional code.
