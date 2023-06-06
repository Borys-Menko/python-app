FROM python:3.11

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV DB_HOST=db
ENV DB_PORT=5432
ENV DB_NAME=mydatabase
ENV DB_USER=myuser
ENV DB_PASSWORD=mypassword

WORKDIR /app

CMD ["python", "app.py"]

EXPOSE 5000