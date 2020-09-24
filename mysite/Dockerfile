FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
COPY . /code/
WORKDIR /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
CMD [ "./entrypoint.sh" ]