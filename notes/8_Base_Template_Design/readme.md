# 🧩 Django Base Templates Guide

![Django](https://img.shields.io/badge/Django-Framework-green)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner-blue)
![Status](https://img.shields.io/badge/Progress-Learning-orange)

---

## 📌 What You'll Learn

* What are **Base Templates** in Django
* Why they are important
* How to use `{% extends %}` and `{% block %}`
* Build a clean, reusable layout

---

## 🧠 Concept in One Line

> **Write common code once → reuse it across all pages**

---

## ❌ The Problem (Without Base Template)

You create:

* `index.html`
* `detail.html`

Both need:

* Navbar 🍔
* Styling (Tailwind CSS)

👉 You copy-paste everything.

### Problems:

* ❗ Code duplication
* ❗ Hard to update
* ❗ Not scalable

---

## ✅ The Solution: Base Template

A **Base Template (`base.html`)** acts like a **main layout**.

All other pages:
👉 **inherit from it**

---

## 🏗️ Implementation Steps

### 1️⃣ Create `base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Food App{% endblock %}</title>
</head>

<body class="bg-gray-100">

    <!-- Navbar -->
    <nav class="bg-white shadow-md p-4 text-center">
        <h1 class="text-2xl font-bold text-orange-500">
            🍔 Food Menu
        </h1>
    </nav>

    <!-- Content -->
    <div class="max-w-5xl mx-auto mt-8 px-4">
        {% block content %}
        {% endblock %}
    </div>

</body>
</html>
```

---

### 2️⃣ Understand Blocks 🧱

```django
{% block content %}
{% endblock %}
```

👉 This is a **placeholder**
👉 Child templates will fill it

---

### 3️⃣ Extend Base Template

```django
{% extends 'myapp/base.html' %}
```

👉 This line connects your page to the base template

---

### 4️⃣ Example: Menu Page

```html
{% extends 'myapp/base.html' %}

{% block title %}Menu{% endblock %}

{% block content %}

{% for item in my_item %}
  {{ item }}
{% endfor %}

{% endblock %}
```

---

### 5️⃣ Example: Detail Page

```html
{% extends 'myapp/base.html' %}

{% block title %}Details{% endblock %}

{% block content %}

<h1>{{ item.item_name }}</h1>
<p>{{ item.item_desc }}</p>

{% endblock %}
```

---

## 🎯 Final Result

✔ Same navbar everywhere
✔ Clean structure
✔ No repetition
✔ Easy updates

---

## 🔑 Key Concepts

| Concept         | Meaning                    |
| --------------- | -------------------------- |
| `base.html`     | Main layout                |
| `{% extends %}` | Inherit layout             |
| `{% block %}`   | Replaceable section        |
| Reusability     | Write once, use everywhere |

---

## 🏠 Simple Analogy

* `base.html` = House structure 🏠
* Child templates = Rooms 🛏️
* Blocks = Space where you decorate

---

## 🚀 Pro Tips

* Add footer in base template
* Create multiple blocks:

  * `title`
  * `content`
  * `scripts`
* Keep base clean and minimal


---
