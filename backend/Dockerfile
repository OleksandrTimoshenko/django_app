#FROM python:3
# if I use python:3.8.3-alpine it doesn`t work corectly with psycopg2-binary==2.8.6
FROM python:3.8.6
#ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
#COPY . /code/
#WORKDIR /code/
#COPY requirements.txt /code/
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN apt update && apt install bash-completion
CMD [ "./entrypoint.sh" ]