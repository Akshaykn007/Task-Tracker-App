# Task-Tracker-App

Django-based webapp, used to track tasks assigned for members etc.

## Overview

* Language: Python (version:3)
* Platform: Windows / Ubuntu
* Framework: Django

### 1. Create python3 virtual environment and install requirements.txt
    `py -m venv <env>`
    `pip install django`
    `pip install pipreqs`
    `pipreqs location`

### 2. Performing Django Migrations
    Follow the below commands..
    `python3.6 manage.py makemigrations`
    `python3.6 manage.py migrate`

### 3. Create superuser/admin
    Follow the below commands..
    `python3.6 manage.py createsuperuser --username <username> --email <email-id>`

### 4. How to run
    Follow the below commands..
    `python3.6 manage.py runserver`

### 5. Sanity Check (Ping service)
    Follow the below commands..
    curl --location --request GET 'http://127.0.0.1:8000/ping' \
--header 'Cookie: csrftoken=VBEW2S4ukTkrwhzMKbeFA5ti5FZBO6vurCY9QhILDwGr2vk34a
2xPlDISPrqGd02'
