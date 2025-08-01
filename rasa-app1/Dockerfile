FROM python:3.9-slim

WORKDIR /app

RUN pip install poetry==1.7.1

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

EXPOSE 5005

CMD ["poetry", "run", "rasa", "run", "--enable-api", "--port", "5005", "--cors", "*"]
