# Crunchr Assignment

To get some statistics from the data-set.

# Requirements
You need to install Python3.8 and Django3.0
```bash
pip install -r requirements.txt
```

# Run

    - python manage.py runserver


# API end-points details:
    - Q1. Static - http://127.0.0.1:8000/search/location/
    - Q1. Dynamic - http://127.0.0.1:8000/search/location/?location=Europe/Netherlands&percentage=10
    - Q2. Static - http://127.0.0.1:8000/search/age/
    - Q2. Dynamic - http://127.0.0.1:8000/search/age/?age=5

# Management command

To load the data into the database please use below command

    - python3 manage.py load_data <file-path>
