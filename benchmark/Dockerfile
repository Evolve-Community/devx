FROM python:3.8-slim
RUN apt-get update && apt-get install -y less git
COPY requirements.txt /devx/requirements.txt
RUN pip install lox typer pandas matplotlib imgcat evolve-devx
RUN pip install --upgrade pip && pip install -r /devx/requirements.txt
WORKDIR /devx

