FROM python:3.11.6

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt && pip install gunicorn

COPY . .

RUN python manage.py collectstatic --noinput
RUN python manage.py generateimages --all || true

EXPOSE 8000

CMD ["gunicorn", "dogsite.wsgi:application", "--bind", "0.0.0.0:8000"]