# Django CBV Pagination Guide

A complete beginner-friendly guide to using **pagination with Class-Based Views (CBV)** in Django.

---

## 📌 What is CBV Pagination?

CBV (Class-Based View) pagination in Django allows you to **automatically split large datasets into multiple pages** using built-in generic views like `ListView`.

Instead of writing manual pagination logic, Django handles it for you.

---

## 🚀 Why Use CBV for Pagination?

Using CBV makes pagination:

* ✅ Faster to implement
* ✅ Cleaner code
* ✅ Less error-prone
* ✅ Built-in support

---

## 🧱 Basic Setup

### Step 1: Import ListView

```python
from django.views.generic import ListView
```

---

### Step 2: Create Your View

```python
from django.views.generic import ListView
from .models import Item

class IndexView(ListView):
    model = Item
    template_name = "myapp/index.html"
    context_object_name = "my_item"
    paginate_by = 6
```

---

## 🔍 Explanation

* `model = Item` → fetches all items
* `template_name` → HTML file
* `context_object_name` → variable used in template
* `paginate_by = 6` → **only 6 items per page**

Django automatically:

* splits data
* reads page number from URL
* sends correct data to template

---

## 🌐 URL Configuration

```python
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('db/', IndexView.as_view(), name='db'),
]
```

---

## 📄 Template Code (`index.html`)

### Display Items

```html
{% for item in my_item %}
    <h2>{{ item }}</h2>
{% endfor %}
```

---

### Add Pagination Controls

```html
{% if is_paginated %}
<div>

    {% if page_obj.has_previous %}
        <a href="?page=1">First</a>
        <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
    {% endif %}

    <span>
        Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
    </span>

    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Next</a>
        <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
    {% endif %}

</div>
{% endif %}
```

---

## 🧠 Important Objects (Auto Provided by Django)

When you use `paginate_by`, Django gives you:

* `page_obj` → current page data
* `is_paginated` → True/False
* `paginator` → total pages and data info

---

## ⚠️ Common Mistakes

### ❌ Forgetting `paginate_by`

Without this, pagination will not work.

---

### ❌ Looping wrong variable

Wrong:

```html
{% for item in items %}
```

Correct:

```html
{% for item in my_item %}
```

---

### ❌ Not checking `has_next` / `has_previous`

Always wrap navigation links properly.

---

## 🔄 Advanced Example (Custom Queryset)

```python
class IndexView(ListView):
    model = Item
    template_name = "myapp/index.html"
    context_object_name = "my_item"
    paginate_by = 6

    def get_queryset(self):
        return Item.objects.filter(is_active=True).order_by('-id')
```

---

## 🔍 Pagination with Search

```html
<a href="?page={{ page_obj.next_page_number }}&search={{ request.GET.search }}">
    Next
</a>
```

---

## 🎯 Key Points for Exam / Interview

* CBV pagination uses `ListView`
* `paginate_by` enables pagination
* `page_obj` contains current page data
* `is_paginated` checks if pagination exists
* No need to manually use `Paginator`

---

## 🏁 Conclusion

CBV pagination is the **simplest and most efficient way** to handle large datasets in Django. With just one line (`paginate_by`), Django manages everything automatically. It is ideal for blogs, product lists, dashboards, and any list-based views.

---

## 🔥 Summary

1. Use `ListView`
2. Add `paginate_by`
3. Use `page_obj` in template
4. Add navigation links

---

## 📁 Example Project Structure

```
myproject/
│
├── myapp/
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   └── models.py
│
├── myproject/
│   └── urls.py
│
└── manage.py
```

---



