# 📄 Django Detail View 

## 📌 Overview

This guide explains how to build a **dynamic detail page** in Django.

👉 Goal:
Move from showing a simple text response → to displaying a **full HTML page with item details (name, price, description)** fetched from the database.

By the end, your app will:

* Show a list of items
* Allow users to click an item
* Open a **dedicated detail page** for that item

---

# 🧠 What You Will Learn

✔ Fetch a single object from the database
✔ Render a template using `render()`
✔ Pass data using **context**
✔ Display dynamic content in HTML
✔ Create clickable links between pages

---

# 🗄️ Step 1: Fetching a Single Item from Database

## ❌ Problem (Before)

Earlier, your view might look like this:

```python
def detail(request, id):
    return HttpResponse(f"This is item {id}")
```

👉 This only shows text — no real data.

---

## ✅ Solution

Use Django ORM to fetch a **specific object**:

```python
from .models import Item

def detail(request, id):
    item = Item.objects.get(id=id)
```

---

## 🔍 Explanation

* `Item.objects.get(id=id)`
  👉 Fetches **only one item** where ID matches

✔ Example:
If URL = `/myapp/3`
→ It fetches item with `id = 3`

---

# 🎨 Step 2: Creating and Rendering Template

## 📁 Create Template File

```
myapp/
    templates/
        myapp/
            detail.html
```

---

## 🧾 Write HTML Template

```html
<!DOCTYPE html>
<html>
<head>
    <title>Item Detail</title>
</head>
<body>

    <h1>{{ item.item_name }}</h1>
    <h3>Price: {{ item.item_price }}</h3>
    <p>{{ item.item_desc }}</p>

</body>
</html>
```

---

## 🔗 Update View to Render Template

```python
from django.shortcuts import render

def detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'myapp/detail.html')
```

---

## ❗ Problem Here

Template won't show data yet — because we didn’t pass it.

---

# 📦 Step 3: Passing Context to Template

## ✅ Add Context Dictionary

```python
def detail(request, id):
    item = Item.objects.get(id=id)
    context = {'item': item}
    return render(request, 'myapp/detail.html', context)
```

---

## 🧠 What is Context?

👉 A dictionary that sends data from **view → template**

```python
{'item': item}
```

* `item` (left) → used in template
* `item` (right) → actual database object

---

## 🖥️ Access Data in Template

```html
{{ item.item_name }}
{{ item.item_price }}
{{ item.item_desc }}
```

✔ Django replaces these with real values

---

# 🔗 Step 4: Make Item List Clickable

## 🎯 Goal

Clicking an item should open its detail page.

---

## 🧾 Modify `index.html`

```html
{% for item in items %}
    <a href="/myapp/{{ item.id }}">
        <h2>{{ item.item_name }}</h2>
    </a>
{% endfor %}
```

---

## 🔍 Explanation

* `<a href="/myapp/{{ item.id }}">`
  👉 Creates a **dynamic URL**

✔ Example:

* Item ID = 5
  → URL = `/myapp/5`

---

# 🔁 Complete Flow (Important)

```
User clicks item
      ↓
URL passes item ID
      ↓
View fetches item from DB
      ↓
Context sends item to template
      ↓
Template displays item details
```

---

# ⚙️ Behind the Scenes

### URL Example

```
/myapp/2
```

### View Receives:

```python
def detail(request, id=2):
```

### Database Query:

```python
Item.objects.get(id=2)
```

### Template Shows:

```
Item Name: Pizza
Price: 200
Description: Delicious cheese pizza
```

---

# ❌ Common Mistakes

## 1. Template Not Found

✔ Correct structure:

```
templates/myapp/detail.html
```

---

## 2. Forgot Context

```python
return render(request, 'detail.html') ❌
```

---

## 3. Wrong Variable Name

```html
{{ product.name }} ❌ if context uses 'item'
```

---

## 4. Object Does Not Exist

```python
Item.objects.get(id=id)
```

❌ Error if ID not found

✔ Better:

```python
from django.shortcuts import get_object_or_404

item = get_object_or_404(Item, id=id)
```

---

# 🚀 Final Result

✔ Index page shows list of items
✔ Each item is clickable
✔ Clicking opens detail page
✔ Detail page shows:

* Name
* Price
* Description

---
