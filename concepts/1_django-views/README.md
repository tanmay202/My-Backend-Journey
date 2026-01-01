# Creating a View in Django

## 📌 Core Concept

In Django, a **View** is a Python function that:
- Receives a web request
- Processes it
- Returns a web response

It acts as the **middle layer** between the URL configuration and the data sent back to the browser.

Views are typically defined in the `views.py` file inside a Django app  
(for example: `myapp/views.py`).

---

## 📌 Key Requirements

### 1️⃣ Input: `request` Object
- Every view function **must accept a `request` object** as its first parameter.
- The `request` object contains information such as:
  - HTTP method (GET, POST)
  - Browser and client details
  - Request metadata

---

### 2️⃣ Output: `HttpResponse`
- A Django view **must return an `HttpResponse` object**.
- Returning a plain string is **not valid**.
- The response content must be wrapped inside `HttpResponse`.

---

## 📌 Example: Simple Django View

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
