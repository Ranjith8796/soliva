# soliva

This is a simple Django web application that uses custom database routers.

# Requirements

- Python 3.6 or higher
- Django 2.2 or higher

# Installation

To install this application, follow these steps:

- Clone the repository: `git clone https://github.com/Ranjith8796/soliva.git`
- Install the required packages: Django, djangorestframework
- Run the makemigrations: `python manage.py makemigrations`
- Run the migrations for default DB: `python manage.py migrate`
- Run the migrations for custom DB(soliva_db): `python manage.py migrate --database=soliva_db`
- Run the development server: `python manage.py runserver`
- Import the postman collection in postman and try to make api call(Attached with examples)
