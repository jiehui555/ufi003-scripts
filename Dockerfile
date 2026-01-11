FROM python:3.12-alpine AS builder
WORKDIR /app
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

COPY . .
CMD ["python", "main.py"]
