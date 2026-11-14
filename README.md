# Django Learning — Student Management System 🐍

Welcome to my Django learning journey! This repository documents my day-by-day progress in learning Django, Python web development, database operations, and practical backend development.

As part of this journey, I am building a **Student Management System** to practise Django concepts through a working project while preparing for technical interviews and placements.

**Repository:** [django-Learning](https://github.com/jaswantmp/django-Learning)

---

## 🎯 Project Overview

The Student Management System is a Django web application that allows users to manage student records. It demonstrates how Django connects Python code, databases, HTML templates, forms, and views to build a dynamic web application.

### Features

- Display student records in a structured table.
- Register new students.
- Update existing student details.
- Delete student records with a confirmation page.
- Validate form inputs using Django ModelForms.
- Display success messages after operations.
- Show student results based on marks.
- Manage student records through Django Admin.
- Customize Admin list columns.
- Search students by name in Django Admin.
- Filter student records by age and marks.
- Query, filter, sort, and aggregate database records using Django ORM.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Web framework |
| SQLite | Database |
| HTML | Page structure |
| CSS | Page styling |
| Django Templates | Dynamic HTML rendering |
| Django ORM | Database queries and operations |
| Git | Version control |
| GitHub | Source code and learning documentation |
| VS Code | Development environment |

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/jaswantmp/django-Learning.git
cd django-Learning
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

If you are using Command Prompt:

```cmd
.venv\Scripts\activate.bat
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

Follow the prompts to create your username and password.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

- Home page: `http://127.0.0.1:8000/`
- About page: `http://127.0.0.1:8000/about/`
- Student Management: `http://127.0.0.1:8000/students/`
- Django Admin: `http://127.0.0.1:8000/admin/`

**Note:** The development server runs locally. Create an admin account before accessing the Admin interface. Student records in the local SQLite database are not included when cloning the repository.

---

## 📚 Concepts Learned

### 1. Django Fundamentals

- Introduction to Django and its architecture.
- Difference between a Django project and an app.
- Project setup and virtual environment management.
- Django settings and URL configuration.
- Views and HTTP responses.
- Rendering HTML templates.
- Passing context data from views to templates.
- Template variables, conditions, loops, and inheritance.

### 2. Models and Database

- Creating Django models.
- Defining model fields.
- Applying database migrations.
- Understanding database records and primary keys.
- Retrieving records using Django ORM.
- Understanding the relationship between models and databases.

### 3. Forms and Validation

- Creating forms using `forms.ModelForm`.
- Handling GET and POST requests.
- Processing form submissions.
- Using CSRF protection.
- Adding custom validation methods.
- Displaying validation errors.
- Showing success messages after successful operations.

### 4. CRUD Operations

CRUD stands for Create, Read, Update, and Delete.

| Operation | Implementation |
|---|---|
| Create | Register a student |
| Read | Display student records |
| Update | Edit student details |
| Delete | Delete a student after confirmation |

Additional features include a styled student table, result calculation based on marks, action links, and success notifications.

### 5. Django Admin Customization

Customized the built-in Django Admin interface to make student records easier to manage.

Implemented features:

- `list_display` to display ID, name, age, and marks.
- `search_fields` to search student records by name.
- `list_filter` to filter student records by age and marks.

Example configuration in `students/admin.py`:

```python
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "marks")
    search_fields = ("name",)
    list_filter = ("age", "marks")
```

### 6. Django ORM Query Practice

Practised querying student records using the Django shell.

**Filtering and excluding records**

```python
Student.objects.filter(marks__gt=80)
Student.objects.filter(marks__gte=40)
Student.objects.filter(marks__lt=40)
Student.objects.exclude(age__gt=18)
```

**Combining conditions using `Q` objects**

```python
from django.db.models import Q

Student.objects.filter(
    Q(marks__gt=70) | Q(age__gt=20)
)
```

**Sorting and limiting results**

```python
Student.objects.order_by("age")
Student.objects.order_by("-marks")[:3]
Student.objects.order_by("-marks").first()
```

**Aggregate functions**

```python
from django.db.models import Max, Avg, Sum

Student.objects.aggregate(Max("marks"))
Student.objects.aggregate(Avg("marks"))
Student.objects.aggregate(Sum("marks"))
Student.objects.count()
```

These queries demonstrate filtering, exclusion, conditional logic, sorting, limiting results, and calculating database statistics.

---

## 📅 Daily Learning Logs

I maintain separate Markdown files and screenshots to document each day's learning.

| Day | Topics | Documentation |
|---|---|---|
| Day 1 | Django introduction and fundamentals | [Day 1](daily-logs/Day-01/Day-01.md) |
| Day 2 | Project setup and Django basics | [Day 2](daily-logs/Day-02/Day-02.md) |
| Day 3 | Django apps, URLs, views, templates, context, conditions, and loops | [Day 3](daily-logs/Day-03/Day-03.md) |
| Day 4 | Student management development | [Day 4](daily-logs/Day-04/Day-04.md) |
| Day 5 | Django forms and validation | [Day 5](daily-logs/Day-05/Day-05.md) |
| Day 6 | CRUD operations and student table improvements | [Day 6](daily-logs/Day-06/Day-06.md) |
| Day 7 | Django Admin customization and ORM query practice | [Day 7](daily-logs/Day-07/Day-07.md) |

Each daily log includes explanations, code examples, learning outcomes, and screenshots where applicable.

---

## 📁 Project Structure

```text
django-Learning/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── student_home.html
│   │       ├── student_form.html
│   │       └── student_confirm_delete.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── about.html
│
└── daily-logs/
    ├── Day-01/
    ├── Day-02/
    ├── Day-03/
    ├── Day-04/
    ├── Day-05/
    │   ├── Day-05.md
    │   └── screenshots/
    ├── Day-06/
    │   ├── Day-06.md
    │   └── screenshots/
    └── Day-07/
        ├── Day-07.md
        └── screenshots/
```

*The structure above represents the expected learning-project layout; optional files and folders may vary as development continues.*

---

## 🗄️ Database

The project uses SQLite, Django's default database for a new project.

The `Student` model contains:

| Field | Type | Description |
|---|---|---|
| `id` | Auto-generated primary key | Unique student identifier |
| `name` | `CharField` | Student name |
| `age` | `IntegerField` | Student age |
| `marks` | `IntegerField` | Student marks |

Database migrations are maintained in the app's `migrations/` directory. The local database file is excluded from version control.

---

## 🔒 Security and Best Practices

- Use Django's CSRF protection for POST forms.
- Validate user input before saving records.
- Use Django's ORM instead of constructing unsafe SQL queries manually.
- Keep virtual environments and local database files out of Git.
- Never commit passwords, secret keys, or other sensitive credentials.
- Use a development server only for local development, not production deployment.

---

## 🎯 Future Learning Goals

- Advanced Django ORM queries.
- Relationships between models using foreign keys.
- Pagination and improved search on website pages.
- User authentication and permissions.
- Django REST Framework and API development.
- Automated testing.
- Deployment and production configuration.
- Placement-oriented Django and Python interview practice.

---

## 👨‍💻 Author

**Jaswant MP**

- GitHub: [@jaswantmp](https://github.com/jaswantmp)
- LinkedIn: [Jaswant MP](https://www.linkedin.com/in/jaswant-mp-a32b81378/)

---

⭐ This repository is a continuous record of my Django learning journey, practical implementation, and preparation for backend development opportunities.
