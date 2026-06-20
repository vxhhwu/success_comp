FROM python:3.13.14


ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y curl && \
    pip install --upgrade pip

RUN pip install uuid django==5.1.4 psycopg2-binary python-dotenv uwsgi

COPY /django .

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
