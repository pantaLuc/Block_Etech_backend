FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY  requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000