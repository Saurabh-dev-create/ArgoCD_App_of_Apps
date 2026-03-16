#  Stage 1: Builder 
FROM python:3.10-slim AS builder

WORKDIR /install

COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt


#  Stage 2: Runtime 
FROM python:3.10-slim

WORKDIR /app

# copy installed dependencies from builder stage
COPY --from=builder /install /usr/local

# copy application code
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]