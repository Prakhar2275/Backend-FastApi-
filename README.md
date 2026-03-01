# Production-Ready Backend APIs with FastAPI 🚀

This repository contains a collection of backend systems built using **FastAPI**, focusing on authentication, scalable API architecture, and real-world backend use cases.

Each project demonstrates production-style backend development with **JWT authentication**, **database integration**, and **modular architecture**.

---

## 📦 Projects Included

### 1. Mini Notes API

A REST API for creating and managing personal notes.

**Features**

* Create, read, update, delete notes
* User authentication with JWT
* User-specific data isolation
* Input validation using Pydantic

**Concepts Covered**

* CRUD operations
* Authentication middleware
* Request validation

---

### 2. User Authentication API

Secure authentication system built with FastAPI.

**Features**

* User registration and login
* Password hashing with bcrypt
* JWT access token authentication
* Protected routes

**Concepts Covered**

* Token-based authentication
* Security best practices
* Dependency injection

---

### 3. Task Management API

Backend for managing tasks and productivity workflows.

**Features**

* Create and manage tasks
* Task status updates
* User-based task ownership
* Secure endpoints

**Concepts Covered**

* RESTful API design
* Database relationships
* Modular architecture

---

### 4. E-commerce Management API

Backend foundation for an e-commerce platform.

**Features**

* Product management
* User authentication
* Order management (basic)
* Role-based access (admin/user)

**Concepts Covered**

* Scalable backend structure
* Role-based authorization
* Production backend design

---

## 🧠 Backend Concepts Implemented

* FastAPI async endpoints
* JWT authentication
* Dependency injection
* Database integration
* Modular project structure
* Secure password hashing
* Environment configuration
* Error handling

---

## 🛠 Tech Stack

* FastAPI
* Python
* PostgreSQL / SQLite
* SQLAlchemy
* Pydantic
* JWT Authentication
* Uvicorn

---

## 📁 Project Structure

```
fastapi-backend-projects/
│
├── notes-api/
├── auth-api/
├── task-api/
└── ecommerce-api/
```

Each project is independent and can be run separately.

---

## ▶️ Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run server:

```
uvicorn main:app --reload
```

API docs available at:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication

Most APIs use JWT authentication.

Include token in headers:

```
Authorization: Bearer <your_token>
```

---

## 🎯 Purpose

This repository demonstrates backend engineering skills using FastAPI and production-level API design principles.

---

## 📌 Future Improvements

* Refresh tokens
* Docker support
* Automated tests
* CI/CD integration
* API rate limiting

---

## 👤 Author

Prakhar Singh Chauhan
Backend Developer | FastAPI | REST APIs | Authentication Systems
