
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /TP

COPY requirements.txt /TP/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/