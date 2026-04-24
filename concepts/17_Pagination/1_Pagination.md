# Django Pagination Guide


## What is Pagination?

Pagination means **splitting a long list of data into smaller pages**.

For example, instead of showing 100 blog posts on one screen, you can show:

* 10 posts on page 1
* 10 posts on page 2
* 10 posts on page 3
* and so on

This makes the page:

* faster to load
* easier to read
* cleaner in design
* better for users

---

## Why Use Pagination in Django?

If your website has a lot of data, showing everything at once is not a good idea.

Pagination helps you:

* reduce page load time
* improve user experience
* organize content neatly
* avoid long scrolling pages

Common examples:

* blog posts
* product lists
* user records
* comments
* search results

---

## Django Pagination Tools

Django provides a built-in pagination class called **`Paginator`**.

You do not need to install any extra package for basic pagination.

The main class is:

```python
from django.core.paginator import Paginator
```

---

## Basic Pagination Example

Suppose you have a list of posts.

### View Example

```python
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 5)  # 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_obj': page_obj})
```

### Explanation

* `Post.objects.all()` gets all records from the database
* `Paginator(posts, 5)` splits the posts into pages, 5 per page
* `request.GET.get('page')` reads the page number from the URL
* `get_page(page_number)` gives the correct page data
* `page_obj` is sent to the template

---

## Template Example

In your HTML template, you can display the paginated data like this:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Post List</title>
</head>
<body>
    <h1>Posts</h1>

    {% for post in page_obj %}
        <div>
            <h2>{{ post.title }}</h2>
            <p>{{ post.content }}</p>
        </div>
    {% endfor %}

    <div>
        {% if page_obj.has_previous %}
            <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
        {% endif %}

        <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Next</a>
        {% endif %}
    </div>
</body>
</html>
```

---

## Step by Step Explanation

### 1. Loop Through Current Page Data

```html
{% for post in page_obj %}
```

This loop shows only the items of the current page.

---

### 2. Show Previous Page Link

```html
{% if page_obj.has_previous %}
    <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
{% endif %}
```

This checks whether a previous page exists.

If yes, it shows the **Previous** link.

---

### 3. Show Current Page Number

```html
Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
```

* `page_obj.number` = current page number
* `page_obj.paginator.num_pages` = total number of pages

---

### 4. Show Next Page Link

```html
{% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}">Next</a>
{% endif %}
```

This checks whether there is a next page.

If yes, it shows the **Next** link.

---

## Important Pagination Methods

Here are the most useful methods and attributes of Django pagination:

* `Paginator(object_list, per_page)` → creates a paginator
* `page_obj.has_next()` → checks if next page exists
* `page_obj.has_previous()` → checks if previous page exists
* `page_obj.next_page_number()` → returns next page number
* `page_obj.previous_page_number()` → returns previous page number
* `page_obj.number` → current page number
* `page_obj.paginator.num_pages` → total number of pages
* `page_obj.paginator.count` → total number of objects

---

## Handling Invalid Page Numbers

Sometimes the user may enter a wrong page number like:

* `?page=abc`
* `?page=9999`
* `?page=-1`

Django's `get_page()` helps handle these safely.

### Example

```python
page_number = request.GET.get('page')
page_obj = paginator.get_page(page_number)
```

This is safer than using `paginator.page(page_number)` directly, because `get_page()` will return a valid page even if the input is invalid.

---

## Difference Between `page()` and `get_page()`

### `page()`

```python
page_obj = paginator.page(page_number)
```

* Raises an error if the page number is invalid
* Useful when you want strict control

### `get_page()`

```python
page_obj = paginator.get_page(page_number)
```

* Handles invalid input more safely
* Better for beginners
* Recommended for most cases

---

## Full Working Example

### views.py

```python
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_obj': page_obj})
```

### post_list.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Post List</title>
</head>
<body>
    <h1>All Posts</h1>

    {% for post in page_obj %}
        <div style="margin-bottom: 20px;">
            <h2>{{ post.title }}</h2>
            <p>{{ post.content }}</p>
        </div>
    {% empty %}
        <p>No posts available.</p>
    {% endfor %}

    <div>
        {% if page_obj.has_previous %}
            <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
        {% endif %}

        <span> Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }} </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Next</a>
        {% endif %}
    </div>
</body>
</html>
```

---

## Styling Pagination Links

You can make the pagination look better using CSS.

### Example

```html
<style>
.pagination {
    margin-top: 20px;
}

.pagination a {
    padding: 8px 12px;
    margin: 2px;
    text-decoration: none;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.pagination a:hover {
    background-color: #f0f0f0;
}

.pagination .current {
    padding: 8px 12px;
    font-weight: bold;
}
</style>
```

Then wrap your links like this:

```html
<div class="pagination">
    {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
    {% endif %}

    <span class="current">Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>

    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Next</a>
    {% endif %}
</div>
```

---

## Pagination with Search or Filters

If your page has search or filters, you should keep the query parameters while changing pages.

Example:

```html
<a href="?page={{ page_obj.previous_page_number }}&search={{ request.GET.search }}">Previous</a>
```

This is useful when users search for something and still want to move through the filtered results.

---

## Common Mistakes

### 1. Forgetting to pass `page_obj` to the template

If `page_obj` is not passed, the template cannot display pagination data.

### 2. Using the wrong variable in the loop

Use:

```html
{% for post in page_obj %}
```

Not:

```html
{% for post in posts %}
```

when you want only one page at a time.

### 3. Not checking for next/previous pages

Always use:

```html
{% if page_obj.has_next %}
```

and

```html
{% if page_obj.has_previous %}
```

### 4. Not handling invalid page input

Use `get_page()` so the app does not break.

---

## Interview / Exam Key Points

* Pagination divides a large set of data into smaller pages.
* Django provides the `Paginator` class.
* `get_page()` is safer for beginners.
* `page_obj` contains the current page data.
* `has_next` and `has_previous` help in navigation.
* Pagination improves performance and user experience.

---

## Conclusion

Pagination is one of the most useful features in Django when you work with large amounts of data. It keeps pages clean, fast, and easy to use. Django makes pagination simple with the built-in `Paginator` class, and the `get_page()` method helps avoid errors. Once you understand the basic flow, you can easily add pagination to blogs, product lists, dashboards, and search results.

---

## Next Step

Try creating a small Django project with a model like `Post` or `Product`, add 20 records, and apply pagination with 5 items per page.

---

## Example Project Structure

```text
myproject/
│
├── app/
│   ├── templates/
│   │   └── post_list.html
│   ├── views.py
│   └── models.py
│
├── myproject/
│   ├── settings.py
│   └── urls.py
│
└── manage.py
```

---

## Summary

Pagination = divide data into pages.

In Django:

1. Import `Paginator`
2. Get your queryset
3. Create paginator with items per page
4. Read page number from URL
5. Pass `page_obj` to template
6. Show Next / Previous links
