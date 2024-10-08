# Stap 1: Basis Python-image gebruiken
FROM python:3.11-slim

RUN pip install uv

WORKDIR /src/todo_app

COPY ../../requirements.lock ./
# Installeren van Python dependencies
RUN uv pip install --no-cache --system -r requirements.lock

# Stap 4: Applicatie-bestanden kopiëren naar de container
COPY . .

# Poort instellen waarop de app draait (indien nodig)
EXPOSE 8000

# Stap 5: Command instellen om de applicatie te draaien
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]