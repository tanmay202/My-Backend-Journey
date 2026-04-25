# Django Middleware

## 📌 What is Middleware?

Middleware is a **layer between request and response** in Django.

👉 It processes:
- Request (before it reaches view)
- Response (before it goes to user)

---

## 🔁 Simple Flow

User → Middleware → View → Middleware → User

---

## 🧠 Easy Definition

Middleware is like a **security guard or filter** that checks everything coming in and going out.

---

## 🎯 Why We Use Middleware?

We use middleware to:

- ✅ Check authentication (login/logout)
- ✅ Handle security (CSRF, sessions)
- ✅ Modify request or response
- ✅ Log user activity
- ✅ Add headers or custom logic

---

## ⚙️ How Middleware Works

### 1. Before View (Request Phase)

Middleware can:
- Check user login
- Block requests
- Modify request data

---

### 2. After View (Response Phase)

Middleware can:
- Modify response
- Add headers
- Log output

---

## 📦 Built-in Middleware Examples

Some common Django middleware:

- AuthenticationMiddleware → Handles user login
- SessionMiddleware → Manages sessions
- CsrfViewMiddleware → Protects from CSRF attacks

---

## 📁 Where Middleware is Defined?

In `settings.py`:

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]

---

## 🛠️ Simple Custom Middleware Example

    class SimpleMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            print("Before View")

            response = self.get_response(request)

            print("After View")

            return response

---

## 🔌 How to Add Custom Middleware

Add it in `settings.py`:

    MIDDLEWARE = [
        ...
        'myapp.middleware.SimpleMiddleware',
    ]

---

## 🔄 Real-Life Example

Think of middleware like:

🚪 Security check at a mall  
- Entry check (request)  
- Exit check (response)

---

## 🎯 Summary

- Middleware sits between **request and response**
- It runs **before and after the view**
- Used for security, authentication, logging, etc.
- Easy to customize and extend

---

## 🏁 Conclusion

Middleware helps control and manage how data flows in a Django app, making your app **secure and powerful**.
