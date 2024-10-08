# Stap 1: Basis Python-image gebruiken
FROM python:3.11-slim

RUN pip install uv

WORKDIR /src

COPY requirements.lock ./

RUN uv pip install --no-cache --system -r requirements.lock

COPY src .

EXPOSE 8000 

CMD ["fastapi", "run", "todo_app/main.py", "--port", "8000"]