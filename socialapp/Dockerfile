# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.12.0-alpine3.17

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory to /music_service
WORKDIR /app

# Copy the current directory contents into the container at /music_service
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip uninstall -y decouple
RUN pip install python-decouple
RUN pip install psycopg2-binary
EXPOSE 8000

ENTRYPOINT python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000