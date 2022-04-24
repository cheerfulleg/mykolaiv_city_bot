FROM python:3.9

WORKDIR /bot

COPY poetry.lock pyproject.toml /bot/

RUN pip install poetry

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /bot

CMD ["python", "run.py"]
