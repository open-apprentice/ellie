FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /ellie

COPY ./ellie/backend /ellie/backend
COPY ./ellie/dashboard /ellie/dashboard