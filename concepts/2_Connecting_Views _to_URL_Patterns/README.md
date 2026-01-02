# 🔗 Core Concept: Decoupling URLs in Django

## 📌 Best Practice

Instead of defining all URL patterns in the main project’s `urls.py`, each Django app should have its own `urls.py` file.  
This approach keeps the code **clean, modular, and scalable**.

---

## 🧩 Step 1: Create App-Level URLs

Each app should manage its own URL configuration.

### Create `urls.py` inside your app folder


### `myapp/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # Empty string '' represents the root of this app's path
    path('', views.index),
]

mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Forwards any request starting with 'myapp/' to myapp/urls.py
    path('myapp/', include('myapp.urls')),
]