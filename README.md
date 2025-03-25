# Django Task Management API

This project provides a simple API for managing tasks and assigning them to users using Django and Django REST Framework.


### **1. Clone the Repository**
```bash
$ git clone https://github.com/your-repo/task-management-api.git
$ cd task-management-api
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

### **4. Configure Environment Variables**
Create a **.env** file in the project's root directory and add the required environment variables:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Change this for production
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
## 📌 **API Endpoints**

### **1️⃣ User Authentication**
#### **Register a User**
**Endpoint:** `POST /api/v1/auth/register/`

**Request Body:**
```json
{
    "email": "user@example.com",
    "username": "john_doe",
    "password": "password123"
}
```

**Response:**
```json
{
    "message": "User registered successfully",
    "user": {
        "uid": "c8e2a0d2-0b60-4f58-b98f-dcc1d0f9b002",
        "email": "user@example.com",
        "username": "john_doe"
    }
}
```

#### **Login**
**Endpoint:** `POST /api/v1/auth/login/`

**Request Body:**
```json
{
    "email": "user@example.com",
    "password": "password123"
}
```

**Response:**
```json
{
    "user": {
        "uid": "c8e2a0d2-0b60-4f58-b98f-dcc1d0f9b002",
        "email": "user@example.com",
        "username": "john_doe"
    },
    "access_token": "your_access_token",
    "refresh_token": "your_refresh_token"
}
```

---
### **2️⃣ Task Management**

#### **Create a Task**
**Endpoint:** `POST /api/v1/task/tasks/`

**Headers:**
```json
{
    "Authorization": "Bearer your_access_token"
}
```

**Request Body:**
```json
{
    "name": "Fix Bug #123",
    "description": "Resolve the API timeout issue",
    "task_type": "Development"
}
```

**Response:**
```json
{
    "id": "a7f123d4-8a4f-4b8a-a23d-123456789abc",
    "name": "Fix Bug #123",
    "description": "Resolve the API timeout issue",
    "status": "pending",
    "created_at": "2024-07-22T12:00:00Z"
}
```

#### **Assign Task to Users**
**Endpoint:** `POST /api/v1/task/tasks/{task_id}/assign/`

**Request Body:**
```json
{
    "user_ids": ["b6c123d4-7e4f-4b8a-b89d-0987654321ef"]
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

**Super Admin:**
```plaintext
Email: admin@example.com
Password: admin123
```

**Regular User:**
```plaintext
Email: user@example.com
Password: password123
