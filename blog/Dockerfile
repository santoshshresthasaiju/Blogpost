FROM python:3.10-slim

WORKDIR /blog

ENV PYTHONDONTWRITEBYCODE 1

ENV PYTHONNUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /blog
RUN pip install -r requirements.txt

COPY . /blog

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]