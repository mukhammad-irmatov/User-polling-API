# Polling-system-api
This project API is used for user polling system. It gives an opportunity to create, update and delete Polls and inside questions.

Technical task is below:

- authorization in the system (registration is not required)
- add / change / delete polls. Poll attributes: title, start date, end date, description. After creation, the field "start date" for the survey cannot be changed
- adding / changing / deleting questions in the survey. Question attributes: question text, question type (text answer, single choice answer, multiple choice answer)

Functionality for system users:

- getting a list of active polls
- taking a survey: surveys can be completed anonymously, a numeric ID is passed to the API as a user identifier, by which the user's answers to questions are stored; one user can participate in any number of surveys
- getting the polls completed by the user with details on the answers (what is selected) by the unique user ID

<h2> Documentation of the API is builted in Swagger(drf-yasg) and you can see at http://127.0.0.1:8000/swagger/</h2>

<h5> Project environment:</h5>
- python 
- Django 
- djangorestframework

Clone the repository using git:
https://github.com/mukhammad-irmatov/Polling-system-api

Go to folder:
cd Poll_project

Install system dependencies from requirements.txt
pip install -r requirements.txt

Command for creating database application migrations:
<b><br>python manage.py makemigrations
<br>python manage.py migrate </b>

Create superuser
python manage.py createsuperuser

Enter username, email, password
<h4> default username - admin </h4>
<h4>default password - 12345</h4>
<h3>
Command to run the application: </h3>
<b>
python manage.py runserver
