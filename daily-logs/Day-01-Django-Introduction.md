# Day 1 — Introduction to Django and Environment Setup

**Date:** 5 November 2026  
**Topic:** Django Fundamentals and Installation

## 1. Objective

To understand the fundamentals of Django, learn its purpose in web development, and set up a local Django development environment.

## 2. What I Learned

### What is Django?
Django is a high-level, open-source web framework written in Python. It helps developers build secure, maintainable, database-driven web applications.

### Why Django is Used
- To develop web applications using Python.
- To handle HTTP requests and responses.
- To connect applications to databases.
- To implement authentication and authorization.
- To perform CRUD operations.
- To create dynamic HTML pages and backend APIs.
- To use the built-in administration interface.

### Important Django Concepts
- **Project:** The overall configuration of a Django website.
- **App:** A component that provides a particular set of features.
- **URL routing:** Maps URL patterns to views.
- **View:** Python code that processes a request and returns a response.
- **Model:** Defines the structure of application data.
- **Template:** An HTML file used to render dynamic webpages.
- **ORM:** Allows database operations through Python objects and methods.
- **MVT:** Model-View-Template, Django's common application architecture.

## 3. Environment Setup

- Created a project folder on the E: drive.
- Created a Python virtual environment named `.venv`.
- Activated the virtual environment.
- Installed Django using pip.
- Verified the installed Django version: 6.1.3.
- Created a Django project named `mysite`.
- Started the local development server.
- Applied the initial database migrations successfully.

## 4. Commands Practised

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install Django
python -m django --version
django-admin startproject mysite .
python manage.py migrate
python manage.py runserver
```

## 5. Practical Work Completed

- Successfully opened the default Django welcome page in the browser.
- Learned the purpose of `manage.py`, `settings.py`, and `urls.py`.
- Understood that Django's development server runs locally at `http://127.0.0.1:8000/`.
- Learned that migrations prepare the database tables required by Django's built-in applications.

## 6. Outcome

Successfully installed Django and configured a working local development environment. Understood the basic purpose of Django and its role in backend web development.

## 7. Next Learning Goals

- Understand Django URL routing.
- Create and connect views.
- Build a custom webpage.
- Learn the difference between a Django project and an app.

