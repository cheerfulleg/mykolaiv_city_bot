FROM python:3.9

WORKDIR /backend

COPY poetry.lock pyproject.toml /backend/

RUN pip install poetry

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /backend

EXPOSE 8000

CMD ["python", "run.py"]
