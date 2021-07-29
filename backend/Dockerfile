FROM python:3.9.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/base.txt backend/requirements/base.txt
COPY requirements/production.txt backend/requirements/production.txt

WORKDIR /backend/

RUN pip3 install -r requirements/production.txt

COPY . /backend/

EXPOSE 8000