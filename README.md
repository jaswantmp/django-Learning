# Django Student Management System

A beginner-friendly Django project for registering students, validating student details, viewing student records, and managing records through Django Admin.

## Features

- View registered students
- Register new students
- Validate student names, ages, and marks
- Display a success message after registration
- Store student data in an SQLite database
- Manage student records through Django Admin

## Requirements

- Python 3.10 or a compatible version supported by the installed Django release
- pip
- Git (optional, for cloning the repository)

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/jaswantmp/django-Learning.git
cd django-Learning
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install the required packages

```bash
python -m pip install -r requirements.txt
```

### 4. Create the database tables

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

The student registration page is available at:

http://127.0.0.1:8000/students/register/

### 6. Access Django Admin

Create a local administrator account:

```bash
python manage.py createsuperuser
```

Then open:

http://127.0.0.1:8000/admin/

Log in with the administrator credentials created on your own computer.

## Database Information

The project uses SQLite. Each person running the project has their own local database. Run the migrations to create the database tables.

Existing student records and administrator accounts are not included in the GitHub repository.

## Repository

https://github.com/jaswantmp/django-Learning
