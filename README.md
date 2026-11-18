# Django Learning Journey

A hands-on Django project documenting my daily learning journey in Python web development. I am building a Student Management System while learning Django fundamentals, database operations, forms, validation, and ORM relationships.

**GitHub Repository:** [django-Learning](https://github.com/jaswantmp/django-Learning)

## Project Overview

The Student Management System is a Django web application that manages student records and their associated subjects. It supports CRUD operations, form validation, student result calculation, subject management, and student performance reports.

## Features

- **Student Management:** Create, view, update, and delete student records.
- **Form Validation:** Validate student names, ages, and marks using Django ModelForms.
- **Student Results:** Display Pass or Fail based on student marks.
- **Django Admin:** Manage student and subject records through the admin interface.
- **Admin Search and Filters:** Search student names and filter records.
- **Subject Management:** Associate subjects with students using `ForeignKey` relationships.
- **Subject CRUD:** Add, update, and delete subjects from the student edit page.
- **Duplicate Prevention:** Prevent duplicate subject names for the same student.
- **Django ORM:** Filter, sort, exclude, and retrieve database records.
- **Success Messages:** Display feedback after successful operations.
- **Responsive Dashboard:** Display student records, statistics, and search functionality.
- **Student Reports:** Display student statistics and marks distribution using charts.
- **CSV Export:** Export student records to a CSV file.
- **Automated Testing:** Practise testing Django models and views.

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- Django Template Language
- Git and GitHub
- Chart.js

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
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── students/
│           ├── student_home.html
│           ├── student_register.html
│           ├── student_delete.html
│           └── student_reports.html
├── templates/
├── screenshots/
├── daily-logs/
│   ├── Day-05/
│   ├── Day-06/
│   ├── Day-07/
│   ├── Day-08/
│   └── DAY9_LOG.md
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The project structure may evolve as development continues. Keep filenames and daily log paths consistent with the actual repository.*

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jaswantmp/django-Learning.git
cd django-Learning
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Admin Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the application:

- **Student Management:** [http://127.0.0.1:8000/students/](http://127.0.0.1:8000/students/)
- **Django Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

> **Note:** The local SQLite database and its records are not included in the repository. Run migrations and create your own data after setting up the project.

## Learning Progress

| Day | Topics Covered |
|---|---|
| Day 1 | Introduction to Django |
| Day 2 | Project setup and Django fundamentals |
| Day 3 | Apps, URLs, views, templates, and template context |
| Day 4 | Student Management System development |
| Day 5 | Django Forms, ModelForms, validation, and messages |
| Day 6 | CRUD operations and student table improvements |
| Day 7 | Django Admin customization and ORM queries |
| Day 8 | ForeignKey relationships and subject management |
| Day 9 | ORM relationships, uniqueness constraints, subject validation, and form validation |
| Day 10 | Dashboard UI improvements, modern student registration page, delete confirmation page, and student reports with charts |

## Day 10 — Work Completed

- Improved the student dashboard's overall presentation.
- Created a modern student registration interface with form validation.
- Designed a student deletion confirmation page with Delete and Cancel options.
- Reviewed the student reports page with statistics and marks distribution.
- Improved the visual consistency and usability of the application.

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
- Database uniqueness constraints
- Responsive HTML and CSS layouts
- Django messages and CSRF protection
- Displaying charts with Chart.js
- Git version control and GitHub
- Introduction to automated testing

## Tomorrow's Work

- Test student registration, updating, and deletion.
- Verify search and filtering functionality.
- Test CSV export and check the reports page.
- Validate displayed statistics and chart data.
- Identify and fix any errors or usability issues.
- Review the project structure and update documentation where necessary.

## Future Improvements

- Add authentication and role-based access.
- Improve responsive design across all pages.
- Add pagination and advanced student search.
- Expand automated tests for models, views, and form submissions.
- Improve error handling and security.
- Explore deployment.

## Author

**Jaswant MP**

- **GitHub:** [jaswantmp](https://github.com/jaswantmp)
- **LinkedIn:** [Jaswant MP](https://www.linkedin.com/in/jaswant-mp-a32b81378/)
- **LeetCode:** [jaswantmp](https://leetcode.com/u/jaswantmp/)

This repository is a learning project developed incrementally to build practical Django and web development skills.