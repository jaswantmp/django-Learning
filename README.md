
# Django Student Management System

A beginner-friendly Student Management System built using Python and Django. This project demonstrates Django fundamentals, database operations, form handling, validation, and CRUD functionality.

## Features

- View all registered students in an HTML table.
- Register new students.
- Update existing student details.
- Delete students with a confirmation page.
- Validate student names, ages, and marks.
- Display Pass or Fail based on student marks.
- Display success messages after registration, updates, and deletion.
- Manage student records through Django Admin.
- Styled interface with Create, Edit, and Delete buttons.

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Django Templates
- Django ModelForms

## Project Structure

```text
django-Learning/
├── daily-logs/
│   ├── Day-01-Django-Introduction.md
│   ├── Day-02/
│   ├── Day-03/
│   ├── Day-04/
│   ├── Day-05/
│   └── Day-06/
├── mysite/
│   ├── settings.py
│   └── urls.py
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── student_home.html
│   │       ├── student_form.html
│   │       └── student_confirm_delete.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

## Requirements

- Python installed on your system.
- pip, Python's package installer.
- Git (optional, for cloning the repository).

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jaswantmp/django-Learning.git
cd django-Learning
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**macOS or Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Create the database tables

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the following URL in your browser:

http://127.0.0.1:8000/

Student Management System:

http://127.0.0.1:8000/students/

Student Registration:

http://127.0.0.1:8000/students/register/

## Django Admin

To access the Django Admin panel, create an administrator account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your username and password.

Start the server and visit:

http://127.0.0.1:8000/admin/

## Student Data and Database

The project uses SQLite as its database.

The database file (`db.sqlite3`) is not included in the Git repository. When setting up the project for the first time, run:

```bash
python manage.py migrate
```

This creates the database tables. You can then register new students through the application.

## Daily Learning Log

This repository documents my Django learning journey.

- Day 1: Django Introduction
- Day 2: Project Setup and Fundamentals
- Day 3: Django Models and Database Operations
- Day 4: Student Management Features
- Day 5: Django Forms and Validation
- Day 6: CRUD Operations and Interface Improvements

See the `daily-logs/` directory for the corresponding notes and screenshots.

## Author

Jaswant MP

GitHub: https://github.com/jaswantmp

LinkedIn: https://www.linkedin.com/in/jaswant-mp-a32b81378/

LeetCode: https://leetcode.com/u/jaswantmp/
