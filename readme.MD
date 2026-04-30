# steps 
1. systems plan (diagrams )
2. set up my virtual environment for the project
`python 3 -m venv venv` and activate with `source venv/bin/activate`
3. install django framework 
`pip isntall django`
>optionally verify the installation by running `djangonadmin --version` or `python3 -m django --version`
4. Create the django project `django-admin startproject taxes`
5. change the directory into the project folder  `cd taxes`
> optionally test your server  `python3 manage.py runserver`
6.Create the django app `django-admin startapp web`
7. register the django applictions in the `settings.py` under the `installed Apps` array

## working with the URLS views and templates 


## 📌 Project Checklist

### ⚙️ Setup Procedures
- [x] System Plan  
- [ ] Create and activate the virtual environment  
- [ ] Install Django  
- [ ] Create a Django Project and change directory into it  
- [ ] Create a Django app and register it in `settings.py`  

### 🧱 App Setup
- [ ] Create the Model  
- [ ] Make migrations  #migration is taking your model and moving it to the database
-`python3 manage.py makemigrations [appname](web)`
-`python3 manage.py migrate`
- [ ] Build the templates (HTML)  
- [ ] Create view functions  
- [ ] Map the View functions to the URLs 


Student Attendance System

 

For this assessment, you will create a single Django application to manage a simple student attendance system. This project will demonstrate your understanding of fundamental Django concepts, including virtual environments, projects and apps, models, URLs, views, templates, and the core CRUD principles.

Project Requirements

 

1. Virtual Environment:

Set up a dedicated Python virtual environment for your project.

2. Django Project and App:

Create a new Django project and a single Django application within it.

3. Data Model:

Create a single Django model to represent a student. This model should include the following fields:

name: A CharField to store the student's name.
student_id: A CharField to store a student ID.
is_present: A BooleanField to track attendance for a given day.
date: A DateField to record the date of attendance.