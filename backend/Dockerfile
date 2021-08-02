FROM python:3.9.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/base.txt backend/requirements/base.txt
COPY requirements/production.txt backend/requirements/production.txt

WORKDIR /backend/

# TODO: Account for development and production mode
RUN pip3 install -r requirements/production.txt

COPY . /backend/

ENV PYTHONPATH "${PYTHONPATH}:/app/"

EXPOSE 8000

