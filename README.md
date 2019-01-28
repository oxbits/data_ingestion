# data_ingestion

# Make Sure Everything Is Installed:

Using Python 3.7.2

---

`brew install sqlite3`

`brew install rabbitmq`

`pip3 install virtualenv`

`virtualenv -p python3 env`

`source env/bin/activate`

`pip3 install -r requirements.txt`

---

# RabbitMQ, Celery, Django Commands:

in top level of project run: (separate terminal or separate process)

`rabbitmq-server`

---

in virtualenv, in 1st level of data_ingestion, next to manage.py, run: (separate terminal or separate process)

`celery -A data_ingestion worker -l info`

---

in virtualenv, in 1st level of data_ingestion, next to manage.py, run: (separate terminal or separate process)

`python3 manage.py runserver`

---

# Django Admin

in your browser go here:

`http://127.0.0.1:8000/admin/`

---

login with either...

---

superuser username: `admin`

password: `iceberg9`

---

staff username: `staff9`

password: `iceberg9`

---

should take you here:

`http://127.0.0.1:8000/admin/`

---

click on `Data files`

click on `ADD DATA FILE`

click on `Choose File`

choose `ZKWDLhxw.txt` from top level of project

click on `SAVE`

---

go back to:

`http://127.0.0.1:8000/admin/`

---

explore other models:

Purchase types, Customers, Order records	

see that data was successfully ingested

---

I would love to share modeling thoughts.

Completed:

• Progress bar when uploading dat file.

• I am nearly certain that this can handle very large files > 3MB.

• Authentication.

---

please let me know if you have any issues or questions

