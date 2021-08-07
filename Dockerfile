FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/yunzzu/djust.git

WORKDIR /home/djust/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-w2wkgjjb&ib1#+kqvjakqn+55am64b3-z^(uyt)v1c4^0dfw&w" > .env

# DB 연동
RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "testproject.wsgi", "--bind", "0.0.0.0:8000"]