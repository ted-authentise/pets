FROM python:3.11

WORKDIR /app
RUN pip install poetry

COPY ./backend /app

RUN poetry install
CMD poetry run start
