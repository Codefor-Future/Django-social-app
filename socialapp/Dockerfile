# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.12.0-alpine3.17

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first

# ENV SECRET_KEY="django-insecure-jtr5_kc!5*zzm($45dyq3c$g$4&vyf07^ehr8q0n5p00u-@d1$"
# ENV CORS_ORIGIN_ALLOW_ALL=True
# ENV DB_NAME="myproject"
# ENV DB_PASSWORD="password"
# ENV DB_NAME="myproject"
# ENV DB_HOST="some-postgres"
# ENV DB_PORT=5432

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

ENTRYPOINT  python manage.py createsuperuser && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000