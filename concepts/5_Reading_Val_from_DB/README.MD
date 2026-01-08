# Reading Data from Database and Displaying on Web Page

Goal

The goal of this step is to read data from a database table using a Django model and display it on a web page to confirm that data is being fetched correctly.

Steps

First, open the `views.py` file inside your Django app. Import the model that you want to access from the database.

Example:

from .models import Item

Next, create or update a view function (for example, `index`). Inside this view, fetch all records from the database table using Django’s Object Manager.

Example:

item_list = Item.objects.all()

Then, return the fetched data using an HttpResponse. This is a temporary testing method to verify database connectivity.

Example:

return HttpResponse(item_list)

Result

After refreshing the web page, the browser will display a QuerySet output such as:

QuerySet [<Item: Pizza>, <Item: Burger>]

This confirms that data is being successfully retrieved from the database. The QuerySet output shows model objects returned by the database query.

Note

This method is only for testing purposes. For proper formatting, styling, and structured output, Django Templates should be used instead of returning raw QuerySets through HttpResponse.
