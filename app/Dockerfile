FROM python:3.12-slim
WORKDIR /app

RUN pip install --no-cache-dir \
    fastapi==0.115.5 \
    uvicorn[standard]==0.32.0 \
    Jinja2==3.1.4 \
    PyMySQL==1.1.1 \
    python-multipart==0.0.12

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
