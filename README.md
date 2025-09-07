# Django To-Do List API 📝

A simple and powerful RESTful API built with **Django** and **Django REST Framework** for managing tasks.  
This project demonstrates essential backend development skills including CRUD operations, authentication, filtering, and API design.

---

## 🚀 Features
- Create, Read, Update, and Delete tasks.
- Token Authentication (each user gets a token automatically).
- Filtering tasks by:
  - `completed`
  - `due_date`
- Search tasks by title or description.
- Ordering tasks by `created_in` or `due_date`.

---

## 🛠️ Tech Stack
- Python 3.x
- Django 5
- Django REST Framework
- SQLite (default DB, can be replaced with MySQL/PostgreSQL)
- Django Filters
- DRF Token Authentication

---

## 📌 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/django-todo-api.git
Navigate into the project:

bash
Copy code
cd django-todo-api
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # on Mac/Linux
venv\Scripts\activate      # on Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the server:

bash
Copy code
python manage.py runserver
## 🔑 Authentication
Obtain token:

bash
Copy code
POST /api_token/
Example request:

json
Copy code
{
  "username": "your_username",
  "password": "your_password"
}
Use token in headers for protected endpoints:

makefile
Copy code
Authorization: Token your_generated_token
## 📂 API Endpoints
GET /api/tasks/ → List all tasks

POST /api/tasks/ → Create a new task

GET /api/tasks/{id}/ → Retrieve a task

PUT /api/tasks/{id}/ → Update a task

DELETE /api/tasks/{id}/ → Delete a task

## Supports:

Filtering → ?completed=true

Search → ?search=meeting

Ordering → ?ordering=due_date

## 🤝 Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📧 Contact
Created by Abdelrahman Zein – feel free to connect with me on linkedin: [http://www.linkedin.com/in/abdelrahman-zein-35288b344].

