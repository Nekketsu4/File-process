FROM python:3.9-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /files
COPY req.txt /files
RUN pip install -r /files/req.txt
COPY . /files