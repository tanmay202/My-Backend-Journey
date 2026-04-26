# 🚀 Django REST API 


## 📌 What is an API?

An **API (Application Programming Interface)** is a way for two programs to communicate with each other.

👉 Example:
- Your mobile app requests data  
- Server sends a response  
- API acts as the **bridge between them**

📖 According to the notes:  
> “An API is code which allows two programs to communicate.” :contentReference[oaicite:0]{index=0}

---

## 🌐 What is a REST API?

A **REST API** is a type of API that uses HTTP methods to perform operations like:

- Fetching data
- Creating data
- Updating data
- Deleting data

📖 Definition:
> “A RESTful API uses HTTP requests to GET, POST, PUT and DELETE data.” :contentReference[oaicite:1]{index=1}  

---

## 🧠 REST Full Form

**REST = Representational State Transfer**

👉 Meaning:
- Server stores data (resource)
- Client requests it
- Server sends **representation of that data (usually JSON)**

📖 From explanation:
> REST transfers the *representation of the resource*, not the actual resource itself. :contentReference[oaicite:2]{index=2}

---

## 🔄 How REST API Works

### Flow:

1. Client sends request  
2. API receives request  
3. Server processes it  
4. Response is returned  

📊 Example (from diagram on page 2):
- Mobile (Client) → API → Server → Database → Response back :contentReference[oaicite:3]{index=3}

---

## ⚙️ HTTP Methods (CRUD Operations)

| Method | Purpose | Example |
|------|--------|--------|
| GET | Retrieve data | Get all movies |
| POST | Create data | Add new movie |
| PUT | Update data | Edit movie |
| DELETE | Remove data | Delete movie |

📖 Source:
> GET retrieves data, POST creates, PUT updates, DELETE removes. :contentReference[oaicite:4]{index=4}  

---