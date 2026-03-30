# 🧩 Django Templates — Complete Guide

## 📌 What is a Template in Django?

A **template** in Django is an HTML file that can display **dynamic data** sent from the backend (views). It uses the **Django Template Language (DTL)** to insert variables, perform logic (loops, conditions), and render content dynamically.

👉 In simple words:
A template = **HTML + dynamic data + simple logic**

---

## 🎯 Why Use Templates?

### 1. Separation of Concerns

Django follows the **MTV (Model–Template–View)** pattern.

* **Model** → Database
* **View** → Logic
* **Template** → UI

✔ Keeps code clean and maintainable
✔ Frontend and backend stay independent

---

### 2. Dynamic Content Rendering

Templates allow you to:

* Display database data
* Show user-specific content
* Update UI without hardcoding values

---

### 3. Reusability

Using features like:

* Template inheritance
* Includes

You can reuse layouts like:

* Headers
* Footers
* Navigation bars

---

### 4. Cleaner HTML

Instead of mixing Python code inside HTML, Django provides:

* `{{ }}` for variables
* `{% %}` for logic

---

## 🧠 Django Template Syntax Basics

### 🔹 Variables

```html
{{ variable }}
{{ student.name }}
```

👉 Displays data passed from the view

---

### 🔹 Template Tags (Logic)

```html
{% for student in students %}
    {{ student.name }}
{% endfor %}
```

👉 Used for loops, conditions, etc.

---

### 🔹 Filters

```html
{{ name|upper }}
{{ name|lower }}
```

👉 Modify output data

---

## 🏗️ Creating a Template (Step-by-Step)

### 1. Create Templates Folder

Inside your app:

```
myapp/
    templates/
        home.html
```

---

### 2. Write Template Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student List</title>
</head>
<body>

    <h1>Student List</h1>

    {% for student in students %}
        <p>{{ student.name }} - {{ student.age }}</p>
    {% empty %}
        <p>No students available</p>
    {% endfor %}

</body>
</html>
```

---

## 🔗 Rendering a Template (Views)

### 1. Create View Function

```python
from django.shortcuts import render
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})
```

---

### 🧩 Understanding `render()`

```python
render(request, template_name, context)
```

| Parameter       | Meaning                 |
| --------------- | ----------------------- |
| `request`       | HTTP request            |
| `template_name` | HTML file               |
| `context`       | Data passed to template |

---

## 📦 What is Context?

**Context = Dictionary of data sent from view to template**

Example:

```python
{'students': students}
```

👉 Here:

* `students` (key) → used in template
* `students` (value) → actual data from database

---

## 🔄 Data Flow (Very Important)

```
Database (Model)
      ↓
View (Fetch Data)
      ↓
Context (Dictionary)
      ↓
Template (Render HTML)
      ↓
User sees output
```

---

## 🔍 How Data is Accessed in Template

### View:

```python
students = Student.objects.all()
```

### Template:

```html
{% for student in students %}
    {{ student.name }}
{% endfor %}
```

👉 Each `student` is an object from the database

---

## ⚡ Advanced Template Features

### ✅ Conditional Rendering

```html
{% if student.age > 18 %}
    Adult
{% else %}
    Minor
{% endif %}
```

---

### ✅ Loop with Counter

```html
{% for student in students %}
    {{ forloop.counter }}. {{ student.name }}
{% endfor %}
```

---

### ✅ Template Inheritance

**base.html**

```html
<!DOCTYPE html>
<html>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**home.html**

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Home Page</h1>
{% endblock %}
```

---

## ❌ Common Mistakes

### 1. Template Not Found

✔ Ensure correct structure:

```
app/templates/file.html
```

---

### 2. Context Not Passed

```python
return render(request, 'home.html')  # ❌ No data
```

---

### 3. Wrong Variable Name

```html
{{ student.name }}  ❌ if context key is different
```

---

## 🚀 Best Practices

✔ Keep templates logic simple
✔ Avoid heavy computations in templates
✔ Use template inheritance
✔ Organize templates properly
✔ Use meaningful variable names

---







