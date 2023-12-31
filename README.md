# RealStick Estate
This is a full stack real estate application developed using React, Redux and Django with the Django Rest Framework. 
We use the JSON Web Token authentication scheme with Django and React.
We implemented pagination using Django Rest Framework.
We implemented a contact form for sending email.
Implemented custom styling using SASS.


In order to test out this project, follow these steps:
- clone the repository
- run: npm install, this will install the required frontend packages
- run: npm run build, this will make the production react build folder
- run: python3 -m venv venv
- then activate the virtual environment
- run: pip install -r requirements.txt
- in realest_estate/settings.py, under DATABASES, set the PASSWORD field to your database password
- in realest_estate/settings.py, under EMAIL_HOST_USER, set your email that you are using
- in realest_estate/settings.py, under EMAIL_HOST_PASSWORD, set your app password you are using
- in contacts/views.py, under the send_mail function, input the email you are using