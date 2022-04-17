FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONBUFFERED 1
WORKDIR /usr/src/djangoApp

COPY ./req.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt
COPY . /usr/src/djangoApp

EXPOSE 8000
CMD python manage.py migrate && python manage.py loaddata data && python manage.py runserver 0.0.0.0:8000
