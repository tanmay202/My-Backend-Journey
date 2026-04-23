## 🧩 Middleware Code

```python
class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print(f"[Middleware] request path :{request.path}")
        response = self.get_response(request)
        print(f"[Middleware] response status:{response.status_code}")
        return response
```

---

## 🔍 Code Explanation

### 1. Class Definition

```python
class LogRequestMiddleware:
```

Defines a custom middleware class.

---

### 2. Initialization Method

```python
def __init__(self, get_response):
    self.get_response = get_response
```

* `get_response` is the next layer (usually a view)
* Stored so we can call it later

---

### 3. Call Method

```python
def __call__(self, request):
```

* Runs on every request
* `request` contains user data (URL, headers, etc.)

---

### 4. Logging Request

```python
print(f"[Middleware] request path :{request.path}")
```

* Prints the URL path being accessed

---

### 5. Passing Request Forward

```python
response = self.get_response(request)
```

* Sends request to view
* Receives response back

---

### 6. Logging Response

```python
print(f"[Middleware] response status:{response.status_code}")
```

* Prints response status code (200, 404, etc.)

---

### 7. Returning Response

```python
return response
```

* Sends response back to the user

---

## 🧠 Key Concepts

* Middleware runs **before and after** the view
* You must always call `get_response(request)`
* Always return a response

---

## ⚙️ How to Add Middleware

Add it in `settings.py`:

```python
MIDDLEWARE = [
    'myapp.middleware.LogRequestMiddleware',
]
```

---

## 🚀 Output Example

```
[Middleware] request path : /home/
[Middleware] response status: 200
```

---

## 📌 Use Cases of Middleware

* Logging requests
* Authentication
* Security checks
* Modifying responses
* Performance monitoring

---

## 🧾 Summary

Middleware is a powerful way to run code globally for every request and response in Django.

---
