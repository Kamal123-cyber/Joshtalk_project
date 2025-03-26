# Django Task Management API

This project provides a simple API for managing tasks and assigning them to users using Django and Django REST Framework.


### **1. Clone the Repository**
```bash
$ git clone https://github.com/Kamal123-cyber/Joshtalk_project.git
$ cd Joshtalk_project
```

### **2. Create a Virtual Environment**
```bash
$ python3 -m venv env
$ source env/bin/activate  # On Windows: env\Scripts\activate
```

### **3. Install Dependencies**
```bash
$ pip install -r requirements.txt
```

### **5. Apply Migrations**
```bash
$ python manage.py migrate
```

### **6. Create a Superuser**
```bash
$ python manage.py createsuperuser
```
Follow the prompt to create a superuser account.

### **7. Run the Development Server**
```bash
$ python manage.py runserver
```
The API will be available at: **http://127.0.0.1:8000/**

---
## **API Endpoints**

### **1️⃣ User Authentication**
#### **Register a User**
**Endpoint:** `POST /api/v1/auth/register/`

**Request Body:**
```json
{
    "email": "kamal@gmail.com",
    "username": "kamal12",
    "first_name": "Kamal",
    "last_name": "Kumar",
    "mobile": "+1234567890",
    "password": "abcdefgh",
    "confirm_password": "abcdefgh"
}
```

**Response:**
```json
{
    "message": "User registered successfully!",
    "user_id": "344f0fa6-a518-42db-94fa-2b59c6fe41a9"
}
```

#### **Login**
**Endpoint:** `POST /api/v1/auth/login/`

**Request Body:**
```json
{
    "email": "abc@example.com",
    "password": "password123"
}
```

**Response:**
```json
{
    "refresh": "",
    "access": "",
    "email": "abc@gmail.com",
    "username": "abc"
}
```

---
### **2️⃣ Task Management**

#### **Create a Task**
**Endpoint:** `POST /api/v1/task/create/`

**Headers:**
```json
{
    "Authorization": "Bearer your_access_token"
}
```

**Request Body:**
```json
{
  "name": "Fix API Bug1",
  "description": "Resolve issue with user authentication API1",
  "task_type": "development1",
  "status": "pending"
}

```

**Response:**
```json
{
    "id": "cfaa2152-db23-445c-a12a-143c9b5d38cc",
    "name": "Fix API Bug1",
    "description": "Resolve issue with user authentication API1",
    "task_type": "development1",
    "status": "pending",
    "completed_at": null,
    "assigned_users": []
}
```

#### **Assign Task to Users**
**Endpoint:** `POST /api/v1/task/tasks/{task_id}/assign/`

**Request Body:**
```json
{
  "user_ids": [
    "9a8de32d-f350-49f6-8285-4ef15b54e806",
    "e3788f68-e378-4e2c-974d-b108c9504a7d"
  ]
}

```

**Response:**
```json
{
    "message": "Users assigned successfully"
}
```

#### **Get Tasks for a Specific User**
**Endpoint:** `GET /api/v1/task/tasks/user/{user_id}/`

**Response:**
```json
[
    {
        "id": "a7f123d4-8a4f-4b8a-a23d-123456789abc",
        "name": "Fix Bug #123",
        "description": "Resolve the API timeout issue",
        "status": "pending"
    }
]
```

---
## 🔑 **Test Credentials**
Use these credentials to test the API:

create the admin creds using python manage.py createsuperuser 
