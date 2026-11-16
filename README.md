# Django Learning Journey

A hands-on Django project documenting my daily learning journey in Python web development. I am building a Student Management System while learning Django fundamentals, database operations, forms, validation, and ORM relationships.

**GitHub Repository:** https://github.com/jaswantmp/django-Learning

## Project Overview

The Student Management System is a Django web application that manages student records and their associated subjects. It provides CRUD operations, form validation, student result calculation, and subject management.

## Features

- **Student Management:** Create, view, update, and delete student records.
- **Form Validation:** Validate student names, ages, and marks using Django ModelForms.
- **Student Results:** Automatically display Pass or Fail based on marks.
- **Django Admin:** Manage student and subject records through the admin interface.
- **Admin Search and Filters:** Search student names and filter records.
- **Subject Management:** Associate subjects with students using ForeignKey relationships.
- **Subject CRUD:** Add, update, and delete subjects from the student edit page.
- **Django ORM:** Filter, sort, exclude, and aggregate database records.
- **Success Messages:** Display feedback after successful operations.
- **Responsive Table:** Display student records in a styled HTML table.

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Django Template Language
- Git and GitHub

## Project Structure

```text
django-learning/
├── manage.py
├── mysite/
│   ├── settings.py
│   └── urls.py
├── students/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── students/
│           ├── student_home.html
│           ├── student_form.html
│           └── student_confirm_delete.html
├── templates/
├── daily-logs/
│   ├── Day-05/
│   ├── Day-06/
│   ├── Day-07/
│   └── Day-08/
├── requirements.txt
├── .gitignore
└── README.md
```

The exact files and daily-log folders may evolve as the project develops.

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

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your account.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application at http://127.0.0.1:8000/students/ and the admin interface at http://127.0.0.1:8000/admin/.

> **Note:** The local SQLite database and its records are not included in the repository. Create or register your own data when setting up the project.

## Learning Progress

| Day | Topics |
|---|---|
| Day 1 | Introduction to Django |
| Day 2 | Project setup and Django fundamentals |
| Day 3 | Apps, URLs, views, templates, and template context |
| Day 4 | Student Management System development |
| Day 5 | Django Forms, ModelForms, validation, and messages |
| Day 6 | CRUD operations and student table improvements |
| Day 7 | Django Admin customization and ORM queries |
| Day 8 | ForeignKey relationships and subject management |

Daily notes and screenshots are maintained in the `daily-logs/` directory when available.

## Key Concepts Learned

- Django project and app structure
- URL routing and view functions
- Rendering templates with context data
- Django Template Language loops and conditions
- Models and database migrations
- ModelForms and server-side validation
- CRUD operations
- Django Admin customization
- ORM filtering, sorting, exclusion, and aggregation
- ForeignKey relationships
- Git version control and GitHub

## Future Improvements

- Add authentication and role-based access.
- Improve form styling and responsive design.
- Add subject validation and duplicate prevention.
- Add pagination and advanced student search.
- Write automated tests.
- Improve error handling and security.
- Explore deployment.

## Author

**Jaswant MP**

- GitHub: https://github.com/jaswantmp
- LinkedIn: https://www.linkedin.com/in/jaswant-mp-a32b81378/
- LeetCode: https://leetcode.com/u/jaswantmp/

This repository is a learning project developed incrementally to build practical Django and web development skills.
